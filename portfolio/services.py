from components.navbar import Navbar
from fasthtml.common import Div


def Services():
    return Div(
        Navbar(index=2),
        cls="flex flex-col sm:flex-row mx-auto min-h-screen w-full max-w-5xl gap-4 sm:gap-20 overflow-auto",
    )
