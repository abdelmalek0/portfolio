from components.navbar import Navbar
from components.service_card import ServiceCard
from fasthtml.common import Div
from fasthtml.common import Span

services = [
    ServiceCard(
        "Data science",
        "I help businesses leverage deep learning, computer vision, \
        and NLP with tailored AI solutions to improve efficiency and achieve their goals.",
        [
            "Image classification",
            "Object detection",
            "Object tracking",
            "Time series",
            "Reinforcement learning",
            "OCR",
            "LLM",
            "ChatLLM",
            "RAG",
        ],
        ["Python", "Tensorflow", "Pytorch"],
    ),
    ServiceCard(
        "Backend Development",
        "I provide backend development services using Python, with expertise in Flask, FastAPI, and Pydantic. \
        I build scalable and efficient APIs, ensuring robust and seamless server-side solutions \
        for your applications.",
        ["API", "Caching", "Database integration"],
        ["Python", "Flask", "FastAPI", "Pydantic", "Redis", "SQLite"],
    ),
    ServiceCard(
        "Android Development",
        "My skillset includes Android development as well allowing me to create feature-rich apps. \
        From UI/UX design to backend integration, I deliver end-to-end solutions tailored to your specific needs.",
        ["App", "Service", "Notification", "Camera", "Location"],
        ["Java", "XAML"],
    ),
]


def Services():
    return Div(
        Navbar(index=2),
        Div(
            Div(
                Span("Roles", cls="text-lg font-semibold"),
                Span("Services I provide", cls="text-md text-gray-400"),
                cls="flex flex-col gap-2",
            ),
            Div(
                *services,
                cls="flex flex-wrap gap-2 pb-2",
            ),
            cls="flex flex-col w-full py-8 sm:py-16 px-8 gap-12",
        ),
        cls="flex flex-col sm:flex-row mx-auto min-h-screen w-full max-w-5xl gap-4 sm:gap-20 overflow-auto",
    )
