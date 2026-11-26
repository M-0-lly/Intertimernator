# "Intertimernator" – a small TUI-Interval-Timer
# Copyright (C) 2026 Tom Steinbach
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see https://www.gnu.org/licenses/.




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
            color: red;
        }
        #desc {
            text-align: center;
        }
        """



    def __init__(self) -> None:
        super().__init__()
        self.timer = None



    def compose(self):

        headline = r"""
             (                                                                                   
     )╲ )           )               )                                        )           
    (()╱(        ( ╱(   (   (    ( ╱( (      )      (   (              )  ( ╱(      (    
     ╱(_)) (     )╲()) ))╲  )(   )╲()))╲    (      ))╲  )(    (     ( ╱(  )╲()) (   )(   
    (_))   )╲ ) (_))╱ ╱((_)(()╲ (_))╱((_)   )╲  ' ╱((_)(()╲   )╲ )  )(_))(_))╱  )╲ (()╲  
    │_ _│ _(_╱( │ │_ (_))   ((_)│ │_  (_) _((_)) (_))   ((_) _(_╱( ((_)_ │ │_  ((_) ((_) 
     │ │ │ ' ╲))│  _│╱ ─_) │ '_││  _│ │ ││ '  ╲()╱ ─_) │ '_││ ' ╲))╱ _` ││  _│╱ _ ╲│ '_│ 
│___││_││_│  ╲__│╲___│ │_│   ╲__│ │_││_│_│_│ ╲___│ │_│  │_││_│ ╲__,_│ ╲__│╲___╱│_│
"""

        yield Static(headline + "\nby M-0-lly\n\n", id="headline")
        yield Static("An interval Timer, to remind you of anything!\n\nHit 'Settings' to configure the intervals.", id="desc")
        yield Container(
            Button("Start timer", id="start"),
            Button("Stop timer", id="stop", disabled=True),
            Button("Settings", id="conf"),
            Button("Close App", id="close"), id="interface"
        )



    def run_msg(self) -> None:

        app_dir = Path(sys.executable).resolve().parent
        msg_exe = app_dir / "_internal/msg.exe"

        subprocess.Popen(
            [str(msg_exe)],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )



    def run_msgeditor(self) -> None:

        app_dir = Path(sys.executable).resolve().parent
        msgeditor_exe = app_dir / "_internal/msgeditor.exe"

        subprocess.Popen(
            [str(msgeditor_exe)],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id

        if button_id == "start":
            interval = Path("_internal/intervals.txt").read_text(
                encoding="utf-8"
            ).strip()

            self.timer = self.set_interval(
                int(interval) * 60,
                self.run_msg,
                pause=True,
            )
            self.timer.resume()

            self.query_one("#start", Button).disabled = True
            self.query_one("#stop", Button).disabled = False

        elif button_id == "stop":
            if self.timer is not None:
                self.timer.stop()

            self.query_one("#start", Button).disabled = False
            self.query_one("#stop", Button).disabled = True

        elif button_id == "conf":
            if self.timer is not None:
                self.timer.stop()

            self.query_one("#start", Button).disabled = False
            self.query_one("#stop", Button).disabled = True
            self.run_msgeditor()

        elif button_id == "close":
            self.exit()





if __name__ == "__main__":
    Timernator().run()
