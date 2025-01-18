from fasthtml.common import Div
from portfolio.components.navbar import Navbar


def Services():
    return Div(
        Navbar(index=2),
        cls="flex flex-row mx-auto min-h-screen w-full max-w-5xl gap-20",
    )
