import sys
from datetime import datetime

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Digits, Footer, Input, Label, Static


class HelloTextualApp(App):
    CSS_PATH = "position.tcss"

    def __init__(self, customs_titles: str = "Scaning...", **kwargs):
        super().__init__(**kwargs)
        self.customs_titles = customs_titles

    def compose(self) -> ComposeResult:
        yield Label(self.customs_titles, id="title_lable")
        yield Digits("")
        # yield is draw me the things

    # thây đổi dữ kiện có sẵn của Textual
    def on_mount(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    # lấy thời gian hiện tại và cập nhật
    def update_clock(self) -> None:
        clock = datetime.now()
        self.query_one(Digits).update(f"{clock:%X}")


if __name__ == "__main__":
    # default
    input_title = "Welcome to Jimmy channel"
    # get title in the terminal
    if len(sys.argv) > 1:
        input_title = sys.argv[1]

    # run the program
    app = HelloTextualApp(customs_titles=input_title)
    app.run()
