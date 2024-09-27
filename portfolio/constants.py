from fasthtml.common import Script, Style, Meta, Link

# Libraries
tailwindcss = Script(src="https://cdn.tailwindcss.com")
daisyui = Link(
    rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@4.11.1/dist/full.css"
)
css = Style(open("static/css/main.css").read())

# Metadata
icon = Link(
    rel="icon",
    href="https://media.licdn.com/dms/image/v2/D4E03AQHFQVrjjbEZew/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1691311567568?e=1732752000&v=beta&t=xZyiOnLrVfZ3qdFewaqmkAUPk1qA39AtJE4N2gqnwjs",
)
inter = Link(href="https://fonts.googleapis.com/css?family=Inter", rel="stylesheet")
meta = Meta(name="viewport", content="width=device-width, initial-scale=1")
