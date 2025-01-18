from fasthtml.common import Link
from fasthtml.common import Meta
from fasthtml.common import Script
from fasthtml.common import Style

# Libraries
tailwindcss = Script(src="https://cdn.tailwindcss.com")
daisyui = Link(
    rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.css"
)
css = Style(open("static/css/main.css").read())
icons = Script(src="https://kit.fontawesome.com/91207e5ccc.js", crossorigin="anonymous")

# Metadata
icon = Link(
    rel="icon",
    href="https://pbs.twimg.com/profile_images/1736776347899351040/jfVfEDen_400x400.jpg",
)
inter = Link(href="https://fonts.googleapis.com/css?family=Inter", rel="stylesheet")
meta = Meta(name="viewport", content="width=device-width, initial-scale=1")
