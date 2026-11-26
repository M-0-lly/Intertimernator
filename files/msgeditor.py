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
from textual.widgets import Button, Static, TextArea, Input
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.validation import Number





class MsgEditor(App):

    CSS = """
            #headline {
                color: red;
                text-align: center;
            }
            #buttons {
                align: center middle;
            }
            #intervals {
                align: center middle;
            }
            #set {
                align: center middle;
            }
            """

    def compose(self) -> ComposeResult:

        headline = r"""
         (                                   
 )\ )        )   )                   
(()/(  (  ( /(( /((        (  (      
 /(_))))\ )\())\())\  (    )\))( (   
(_)) /((_|_))(_))((_) )\ )((_))\ )\  
/ __(_)) | |_| |_ (_)_(_/( (()(_|(_) 
\__ Y -_)|  _|  _|| | ' \)) _` |(_-< 
|___|___| \__|\__||_|_||_|\__, |/__/ 
                          |___/      """ + "\n"

        yield Static(headline, id="headline")
        yield Input(placeholder = "Intervals in Minutes", type="integer", id="intervals")
        yield Button("Set", id="set")
        yield Static()
        yield TextArea(id="msgeditor", placeholder="Type in your message and hit safe!")
        yield Horizontal(
            Button("Save", id="save"),
            Button("Preview", id="preview"),
            Button("Back", id="cancel"), id="buttons"
        )



    def run_msg(self) -> None:

        app_dir = Path(sys.executable).resolve().parent
        msg_exe = app_dir / "msg.exe"

        subprocess.Popen(
            [str(msg_exe)],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )



    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "save":
            msg = self.query_one("#msgeditor", TextArea).text
            Path("_internal/msg.txt").write_text(msg, encoding="utf-8")

        elif event.button.id == "preview":
            self.run_msg()

        elif event.button.id == "cancel":
            self.exit()

        elif event.button.id == "set":
            value = self.query_one("#intervals", Input).value
            Path("_internal/intervals.txt").write_text(value, encoding="utf-8")





if __name__ == "__main__":
    MsgEditor().run()