from fasthtml.common import H1, H2, Div, Img, P, Span, A, Figure
from components.navbar import Navbar
from components.card import Card


projects = [
    Card(
        "PausePal",
        "PausePal is a simple and intuitive desktop application designed to improve productivity and well-being by encouraging regular breaks.",
        "https://github.com/abdelmalek0/pausepal.git",
        ["Python", "GUI"],
        True,
    ),
    Card(
        "Arise",
        "Arise is a tool designed to simplify the setup process for new Python projects, especially for developers who prefer working with modern tools like Poetry for dependency management.",
        "https://github.com/abdelmalek0/arise.git",
        ["Python", "CLI"],
        False,
    ),
]


def Projects():
    return Div(
        Navbar(index=1),
        Div(
            Div(
                Span("Ventures", cls="text-lg font-semibold"),
                Span("Projects I worked on", cls="text-md text-gray-400"),
                cls="flex flex-col gap-2",
            ),
            Div(
                *projects,
                cls="flex flex-row flex-wrap gap-2 ",
            ),
            cls="flex flex-col h-full w-full py-16 px-8 gap-12",
        ),
        cls="flex flex-row mx-auto min-h-screen w-full max-w-5xl gap-20",
    )
