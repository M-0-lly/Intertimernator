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




from textual.widgets import Button, Static
from textual.app import App, ComposeResult
from textual.containers import Container





class Msg(App):

    CSS = """
            #msg {
                text-align: center;
            }
            #interface {
                align: center middle;
            }
            """



    def compose(self) -> ComposeResult:

        with open("msg.txt", "r") as f:
            message = f.read()

        yield Static("\n\n\n\n" + message, id="msg")
        yield Container(
            Button("Close Message", id="close"), id="interface"
        )



    def on_button_pressed(self, event: Button.Pressed) -> None:

        if event.button.id == "close":
            self.exit()





if __name__ == "__main__":
    Msg().run()
