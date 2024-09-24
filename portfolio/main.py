from fasthtml import FastHTML
from fasthtml.common import Title, serve
import uvicorn

from home import Home
from constants import css, tailwindcss, meta, daisyui, inter

app = FastHTML(
    debug=True, hdrs=(meta, tailwindcss, daisyui, css, inter), default_hdrs=False
)
rt = app.route


@rt("/")
def get():
    return (
        Title("Abdelmalek Djamaa - Data scientist, Software Engineer, & Solopreneur"),
        Home(),
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, reload=True)
