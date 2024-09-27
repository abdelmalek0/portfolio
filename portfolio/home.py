from fasthtml.common import H1, Div, Img, P, Span, A
from components.navbar import Navbar


def Home():
    return Div(
        Navbar(index=0),
        Div(
            Span("About", cls="text-lg font-medium"),
            P("💼 I work as a data scientist @SmartPrints.", cls="text-gray-500"),
            P(
                "I've been developing Computer vision systems for a while.",
                cls="text-gray-500",
            ),
            P(
                "I've been coding in 🐍 Python primarily for over 4 years.",
                cls="text-gray-500",
            ),
            P(
                "🌱 I’m currently working on RAG systems and learning Advanced concepts.",
                cls="text-gray-500",
            ),
            cls="flex flex-col h-full w-full py-12 px-8 gap-2",
        ),
        cls="flex flex-row mx-auto min-h-screen w-full max-w-5xl gap-20",
    )
