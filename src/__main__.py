"""
Code browser example.

Run with:

    python code_browser.py PATH
"""

import os

from rich.syntax import Syntax
from rich.traceback import Traceback

from textual import on
from textual.app import App, ComposeResult, BindingType, Binding
from textual.containers import Container, VerticalScroll
from textual.reactive import var
from textual.widgets import DirectoryTree, Footer, Header, Static, Tabs, Tab


class CodeBrowser(App):
    """Textual code browser app."""

    path = "./src/tasks"

    CSS_PATH = "code_browser.css"
    BINDINGS: list[BindingType] = [
        Binding("left", "previous_tab", "Previous tab", show=False),
        Binding("right", "next_tab", "Next tab", show=False),
        ("f", "toggle_files", "Toggle Files"),
        ("r", "run_file", "Run selected file"),
        ("q", "quit", "Quit"),
    ]

    show_tree = var(True)

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
        code_view = self.query_one("#code", Static)
        path = self.sub_title
        if os.path.exists(path):
            ...

    def action_toggle_files(self) -> None:
        """Called in response to key binding."""
        self.show_tree = not self.show_tree


if __name__ == "__main__":
    CodeBrowser().run()
