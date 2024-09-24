from fasthtml.common import Script, Style, Meta, Link

tailwindcss = Script(src="https://cdn.tailwindcss.com")
daisyui = Link(
    rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.css"
)
css = Style(open("static/css/main.css").read())
inter = Link(href="https://fonts.googleapis.com/css?family=Inter", rel="stylesheet")
meta = Meta(name="viewport", content="width=device-width, initial-scale=1")
