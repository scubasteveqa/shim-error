from shiny import App, render, ui, reactive
import datetime
import urllib.request
import random

# Check the gist at startup
webUrl = urllib.request.urlopen(f"https://gist.githubusercontent.com/scubasteveqa/a38a1cab0652f265c1199c661098d47f/raw?cachebust={random.randint(1,100000)}")
data = webUrl.read().decode("utf-8")

print(f"Success gist: {data}")
if data != "true":
    raise Exception("This is now broken")

app_ui = ui.page_fluid(
    ui.card(
        ui.card_header("Current Time"),
        ui.card_body(
            ui.output_text("current_time")
        )
    ),
    ui.card(
        ui.card_body(
            ui.p("これは日本人です")
        )
    )
)

def server(input, output, session):
    @reactive.effect
    def _():
        reactive.invalidate_later(1)  # Update every second
    
    @render.text
    def current_time():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

app = App(app_ui, server)
