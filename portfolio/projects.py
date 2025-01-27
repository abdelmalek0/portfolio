from components.navbar import Navbar
from components.project_card import ProjectCard
from fasthtml.common import Div
from fasthtml.common import Span


projects = [
    ProjectCard(
        "PausePal",
        "PausePal is a simple and intuitive desktop application designed to improve productivity and well-being by encouraging regular breaks.",
        "https://github.com/abdelmalek0/pausepal.git",
        ["Python"],
        True,
    ),
    ProjectCard(
        "Portfolio",
        "Portfolio is a simple web application designed to showcase my work and skills and present the services I provide.",
        "https://github.com/abdelmalek0/portfolio.git",
        ["Python", "FastHTML"],
        False,
    ),
    ProjectCard(
        "Arise",
        "Arise is a tool designed to simplify the setup process for new Python projects, especially for developers who prefer working with modern tools like Poetry for dependency management.",
        "https://github.com/abdelmalek0/arise.git",
        ["Python"],
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
                cls="flex flex-col gap-2 pb-2",
            ),
            cls="flex flex-col w-full py-8 sm:py-16 px-8 gap-12",
        ),
        cls="flex flex-col sm:flex-row mx-auto min-h-screen w-full max-w-5xl gap-4 sm:gap-20 overflow-auto",
    )
