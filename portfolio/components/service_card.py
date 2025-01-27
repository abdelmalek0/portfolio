from dataclasses import dataclass
from typing import List

from fasthtml.common import A
from fasthtml.common import Div
from fasthtml.common import H2
from fasthtml.common import P


@dataclass
class ServiceCard:
    title: str
    description: str
    skills: List[str]
    stack: List[str]

    def __ft__(self) -> A:
        return Div(
            Div(
                H2(
                    self.title,
                    cls="card-title",
                ),
                P(self.description, cls="text-xs"),
                Div(
                    *[
                        Div(tag, cls="badge badge-sm text-xs bg-gray-800 text-gray-200")
                        for tag in self.skills
                    ],
                    cls="card-actions justify-start pt-2",
                ),
                Div(
                    *[
                        Div(tag, cls="badge badge-sm text-xs badge-accent")
                        for tag in self.stack
                    ],
                    cls="card-actions justify-start pt-2",
                ),
                cls="card-body p-4",
            ),
            cls="card bg-base-100  h-[300px] sm:w-[45%] w-full shadow-xl hover:bg-gray-700",
        )
