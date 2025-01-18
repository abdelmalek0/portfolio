from fasthtml import FastHTML
from fasthtml.common import Title
from portfolio.constants import css
from portfolio.constants import daisyui
from portfolio.constants import icon
from portfolio.constants import icons
from portfolio.constants import inter
from portfolio.constants import meta
from portfolio.constants import tailwindcss
from portfolio.contact import Contact
from portfolio.home import Home
from portfolio.projects import Projects
from portfolio.services import Services

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
