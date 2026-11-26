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


Msg().run()