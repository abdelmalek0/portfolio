from fasthtml.common import H1, Div, Img, P, Span, A
from components.navbar import Navbar


def Projects():
    return Div(
        Navbar(index=1),
        cls="flex flex-row mx-auto min-h-screen w-full max-w-5xl gap-20",
    )
