from fasthtml.common import A
from fasthtml.common import Div
from fasthtml.common import I
from fasthtml.common import P
from fasthtml.common import Span
from portfolio.components.navbar import Navbar
def Contact():
    return Div(
        Navbar(index=3),
        Div(
            Div(
                Span("Connect", cls="text-lg font-semibold"),
                Div(
                    Span(
                        P("Reach me directly at"),
                        A(
                            "ga_djamaa@esi.dz",
                            cls="text-gray-200 hover:opacity-90",
                            href="mailto:ga_djamaa@esi.dz",
                        ),
                        P("or connect on social media below."),
                        cls="flex flex-wrap gap-1 text-gray-400",
                    ),
                    cls="flex flex-col gap-1",
                ),
                Div(
                    A(
                        I(cls="fa-brands fa-twitter fa-lg"),
                        href="https://x.com/_abdelmalek01",
                        cls="btn",
                    ),
                    A(
                        I(cls="fa-brands fa-linkedin fa-lg"),
                        href="https://www.linkedin.com/in/abdelmalek-djamaa-cs/",
                        cls="btn",
                    ),
                    A(
                        I(cls="fa-brands fa-github fa-lg"),
                        href="https://github.com/abdelmalek0",
                        cls="btn",
                    ),
                    cls="flex flex-row gap-4",
                ),
                cls="flex flex-col gap-8 pb-2",
            ),
            cls="flex flex-col w-full py-8 sm:py-16 px-8 gap-12",
        ),
        cls="flex flex-col sm:flex-row mx-auto min-h-screen w-full max-w-5xl gap-4 sm:gap-20 overflow-auto",
    )
