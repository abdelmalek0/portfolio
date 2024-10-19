from fasthtml.common import Div, H2, P, A
from dataclasses import dataclass
from typing import List


@dataclass
class Card:
    title: str
    description: str
    src: str
    tags: List[str]
    is_new: bool

    def __ft__(self) -> A:
        return A(
            Div(
                H2(
                    self.title,
                    Div("NEW", cls="badge badge-secondary") if self.is_new else (),
                    cls="card-title",
                ),
                P(self.description),
                Div(
                    *[Div(tag, cls="badge badge-accent") for tag in self.tags],
                    cls="card-actions justify-end",
                ),
                cls="card-body",
            ),
            cls="card bg-base-100 w-full shadow-xl hover:bg-gray-700",
            href=self.src,
        )
