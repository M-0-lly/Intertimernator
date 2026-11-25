from pathlib import Path
import sys
import subprocess
from textual.widgets import Button, Static
from textual.app import App
from textual.containers import Container





class Timernator(App):

    CSS = """
        #interface {
            align: center middle;
        }
        #headline {
            text-align: center;
        }
        
        #desc {
            text-align: center;
        }
        """

    def compose(self):
        yield Static("\nINTERTIMERNATOR\nby M-0-lly\n\n", id="headline")
        yield Static("A 15min interval Timer, to remind you of anything\n\nEdit the 'msg.txt'-file to customize your reminder-message!", id="desc")
        yield Container(
            Button("Start timer", id="start"),
            Button("Stop timer", id="stop", disabled=True),
            Button("Close App", id="close"), id="interface"
        )

    def run_msg(self) -> None:
        app_dir = Path(sys.executable).resolve().parent
        msg_exe = app_dir / "msg.exe"

        subprocess.Popen(
            [str(msg_exe)],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )

    def on_mount(self) -> None:
        self.timer = self.set_interval(900, self.run_msg, pause=True)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.timer.resume()
            self.query_one("#start", Button).disabled = True
            self.query_one("#stop", Button).disabled = False
        elif event.button.id == "stop":
            self.timer.pause()
            self.query_one("#start", Button).disabled = False
            self.query_one("#stop", Button).disabled = True
        elif event.button.id == "close":
            self.exit()



Timernator().run()