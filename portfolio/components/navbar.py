from fasthtml.common import Div, Span, Img, A, P
from dataclasses import dataclass


@dataclass
class Navbar:
    """
    A class to represent the navigation bar with selectable menu items.
    """

    index: int
    nb_menu_items: int = 4

    def __ft__(self) -> Div:
        text_colors = ["text-gray-400"] * self.nb_menu_items
        text_colors[self.index] = "text-white"
        return Div(
            Div(
                Div(
                    Div(
                        Img(
                            src="https://media.licdn.com/dms/image/v2/D4E03AQHFQVrjjbEZew/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1691311567568?e=1732752000&v=beta&t=xZyiOnLrVfZ3qdFewaqmkAUPk1qA39AtJE4N2gqnwjs"
                        ),
                        cls="w-16 rounded-full",
                    ),
                    cls="avatar",
                ),
                Div(
                    Span("Abdelmalek Djamaa", cls="text-lg font-medium"),
                    P("Data scientist", cls="text-gray-500"),
                ),
                cls="flex items-start flex-col w-full gap-4",
            ),
            Div(
                A(
                    Span("Home", cls="font-medium"),
                    href="/home",
                    cls="flex items-center py-1 gap-2 " + text_colors[0],
                ),
                A(
                    Span("Projects", cls="font-medium"),
                    href="/projects",
                    cls="flex items-center py-1 gap-2 " + text_colors[1],
                ),
                A(
                    Span("Services", cls="font-medium"),
                    href="/services",
                    cls="flex items-center py-1 gap-2 " + text_colors[2],
                ),
                A(
                    Span("Contact", cls="font-medium"),
                    href="/contact",
                    cls="flex items-center py-1 gap-2 " + text_colors[3],
                ),
                cls="flex flex-col h-full w-full px-2 py-8 gap-4",
            ),
            cls="flex flex-col h-full w-64 px-2 py-12 gap-8",
        )
