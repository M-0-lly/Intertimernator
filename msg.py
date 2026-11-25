import time
from pathlib import Path
import sys
import subprocess
from textual.widgets import Button, Static
from textual.screen import Screen
from textual.app import App, ComposeResult





class Msg(App):

    def compose(self):

        with open("msg.txt", "r") as f:
            message = f.read()

        yield Static(message)
        yield Button("Close Message", id="close")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "close":
            self.exit()


Msg().run()