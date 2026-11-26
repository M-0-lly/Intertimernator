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
from textual.widgets import Button, Static, TextArea
from textual.app import App, ComposeResult
from textual.containers import Horizontal





class MsgEditor(App):

    def compose(self) -> ComposeResult:

        yield Static("\nEnter your text and press save!\n\n")
        yield TextArea(id="msgeditor")
        yield Horizontal(
            Button("Save", id="save"),
            Button("Preview", id="preview"),
            Button("Cancel", id="cancel"),
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
            Path("msg.txt").write_text(msg, encoding="utf-8")

        elif event.button.id == "preview":
            self.run_msg()

        elif event.button.id == "cancel":
            self.exit()





if __name__ == "__main__":
    MsgEditor().run()