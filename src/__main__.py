"""
Code browser example.

Run with:

    python code_browser.py PATH
"""
import subprocess
import platform
import sys
import os

from rich.syntax import Syntax
from rich.traceback import Traceback

from textual import on
from textual.app import App, ComposeResult, BindingType, Binding
from textual.containers import Container, VerticalScroll
from textual.reactive import var
from textual.widgets import DirectoryTree, Footer, Header, Static, Tabs, Tab

css = """
Screen {
    background: $surface-darken-1;
}

#tree-view {
    display: none;
    scrollbar-gutter: stable;
    overflow: auto;
    width: auto;
    height: 100%;
    dock: left;
}

CodeBrowser.-show-tree #tree-view {
    display: block;
    max-width: 30%;
}


#code-view {
    overflow: auto scroll;
    min-width: 100%;
}
#code {
    width: auto;
}
"""


class CodeBrowser(App):
    """Textual code browser app."""

    path = "./src/tasks"

    CSS = css
    BINDINGS: list[BindingType] = [
        Binding("left", "previous_tab", "Previous tab", show=False),
        Binding("right", "next_tab", "Next tab", show=False),
        ("f", "toggle_files", "Toggle Files"),
        ("r", "run_file", "Run selected file"),
        ("q", "quit", "Quit"),
    ]

    show_tree = var(True)

    def watch_show_tree(self, show_tree: bool) -> None:
        """Called when show_tree is modified."""
        self.set_class(show_tree, "-show-tree")

    def compose(self) -> ComposeResult:
        """Compose our UI."""
        yield Header()
        yield Tabs(
            Tab("Tasks", id="tasks"),
            Tab("Examples", id="examples"),
            active="tasks",
        )

        with Container(id="first_container"):
            yield DirectoryTree(self.path, id="tree-view")
            with VerticalScroll(id="code-view"):
                yield Static(id="code", expand=True)
        yield Footer()

    @on(Tabs.TabActivated)
    def on_tab_clicked(self, event: Tabs.TabActivated) -> None:
        code_view = self.query_one("#tree-view", DirectoryTree)
        self.path = f"src/{event.tab.id}"
        self.sub_title = ""
        code_view.path = self.path

    def on_mount(self) -> None:
        target_folder = "__pycache__"

        for root, dirs, files in os.walk("src"):
            if target_folder in dirs:
                folder_path = os.path.join(root, target_folder)
                try:
                    for item in os.listdir(folder_path):
                        item_path = os.path.join(folder_path, item)
                        if os.path.isfile(item_path):
                            os.remove(item_path)
                        elif os.path.isdir(item_path):
                            os.rmdir(item_path)
                    os.rmdir(folder_path)
                except Exception:
                    pass

        self.query_one(DirectoryTree).focus()

    def on_directory_tree_file_selected(
        self, event: DirectoryTree.FileSelected
    ) -> None:
        """Called when the user click a file in the directory tree."""
        event.stop()
        code_view = self.query_one("#code", Static)
        try:
            syntax = Syntax.from_path(
                str(event.path),
                line_numbers=True,
                word_wrap=False,
                indent_guides=True,
                theme="github-dark",
            )
        except Exception:
            code_view.update(Traceback(theme="github-dark", width=None))
            self.sub_title = "ERROR"
        else:
            code_view.update(syntax)
            self.sub_title = str(event.path)

    def on_directory_tree_directory_selected(self, _: DirectoryTree.DirectorySelected):
        self.sub_title = ""

    def action_run_file(self) -> None:
        """Called in response to key binding."""
        path = self.sub_title
        python_executable = sys.executable
        if platform.system() == "Windows":
            command = f'start cmd /k "set PYTHONPATH=. && {python_executable} {path}"'
        elif platform.system() == "Darwin":  # macOS
            command = f"open -a Terminal.app {python_executable} {path}"
        else:  # Assume Linux
            command = f'gnome-terminal -- bash -c "PYTHONPATH="." {python_executable} {path} && read -p \\"Press Enter to exit...\\" "'
        if os.path.exists(path):
            subprocess.run(command, shell=True)

    def action_toggle_files(self) -> None:
        """Called in response to key binding."""
        self.show_tree = not self.show_tree


if __name__ == "__main__":
    CodeBrowser().run()
