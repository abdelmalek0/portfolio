from fasthtml import FastHTML
from fasthtml.common import Title, serve
import uvicorn

from home import Home
from projects import Projects
from services import Services
from contact import Contact
from constants import meta, icon, tailwindcss, daisyui, css, inter, icons

app = FastHTML(
    debug=True,
    hdrs=(meta, icon, tailwindcss, daisyui, css, inter, icons),
    default_hdrs=False,
)
rt = app.route


@rt("/")
async def get_home():
    return (
        Title("Abdelmalek Djamaa - Data scientist, Software Engineer, & Solopreneur"),
        Home(),
    )


@rt("/projects")
async def get_projects():
    return (
        Title("Projects | Abdelmalek Djamaa"),
        Projects(),
    )


@rt("/services")
async def get_services():
    return (
        Title("Services | Abdelmalek Djamaa"),
        Services(),
    )


@rt("/contact")
async def get_contact():
    return (
        Title("Contact | Abdelmalek Djamaa"),
        Contact(),
    )


