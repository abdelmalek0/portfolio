from fasthtml import FastHTML
from fasthtml.common import Title, serve
import uvicorn

from home import Home
from projects import Projects
from services import Services
from contact import Contact
from constants import meta, icon, tailwindcss, daisyui, css, inter

app = FastHTML(
    debug=True, hdrs=(meta, icon, tailwindcss, daisyui, css, inter), default_hdrs=False
)
rt = app.route


@rt("/")
@rt("/home")
def get_home():
    return (
        Title("Abdelmalek Djamaa - Data scientist, Software Engineer, & Solopreneur"),
        Home(),
    )


@rt("/projects")
def get_projects():
    return (
        Title("Abdelmalek Djamaa - Data scientist, Software Engineer, & Solopreneur"),
        Projects(),
    )


@rt("/services")
def get_services():
    return (
        Title("Abdelmalek Djamaa - Data scientist, Software Engineer, & Solopreneur"),
        Services(),
    )


@rt("/contact")
def get_contact():
    return (
        Title("Abdelmalek Djamaa - Data scientist, Software Engineer, & Solopreneur"),
        Contact(),
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, reload=True)
