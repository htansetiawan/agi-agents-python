from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text


class Printer:
    def __init__(self, console: Console):
        self.console = console
        self.items = {}
        self.live = Live(self._make_panel(), console=console, refresh_per_second=4)
        self.live.start()

    def update_item(self, key: str, text: str, is_done: bool = False, hide_checkmark: bool = False):
        self.items[key] = {"text": text, "is_done": is_done, "hide_checkmark": hide_checkmark}
        self.live.update(self._make_panel())

    def mark_item_done(self, key: str):
        if key in self.items:
            self.items[key]["is_done"] = True
            self.live.update(self._make_panel())

    def end(self):
        self.live.stop()

    def _make_panel(self):
        text = Text()
        for key, item in self.items.items():
            if item["is_done"] and not item["hide_checkmark"]:
                text.append("✅ ")
            text.append(item["text"])
            text.append("\n")
        return Panel(text, title="College Admission Counselor", border_style="blue")
