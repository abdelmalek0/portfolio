from fasthtml.common import Script, Style, Meta, Link

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
    href="https://media.licdn.com/dms/image/v2/D4D03AQHnqC_0RuqD9w/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1731701414066?e=1737590400&v=beta&t=CKocGlzDlMtFfRvdYcYL078R_i9Z9beA0O-TPLkLSYc",
)
inter = Link(href="https://fonts.googleapis.com/css?family=Inter", rel="stylesheet")
meta = Meta(name="viewport", content="width=device-width, initial-scale=1")
