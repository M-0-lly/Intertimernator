# "Intertimernator" – a small TUI-Game in Python
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
        yield Static("A 15min interval Timer, to remind you of anything\n\nHit 'Configure' to customize your reminder-message!", id="desc")
        yield Container(
            Button("Start timer", id="start"),
            Button("Stop timer", id="stop", disabled=True),
            Button("Configure", id="conf"),
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

        elif event.button.id == "conf":
            self.timer.pause()
            self.query_one("#start", Button).disabled = False
            self.query_one("#stop", Button).disabled = True
            self.run_msgeditor()

        elif event.button.id == "close":
            self.exit()





if __name__ == "__main__":
    Timernator().run()
