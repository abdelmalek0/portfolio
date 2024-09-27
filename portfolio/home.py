from fasthtml.common import H1, Div, Img, P, Span, A
from components.navbar import Navbar

AI_SKILLS = [
    "Image classification",
    "Object detection",
    "Object tracking",
    "Time series forecasting",
    "Reinforcement learning",
    "OCR",
    "LLM",
    "ChatLLM",
    "RAG",
]
LANGUAGES = ["Python", "Java", "C"]
LIBRARIES = [
    "Tensorflow",
    "OpenCV",
    "Keras",
    "Numpy",
    "Pandas",
    "Matplotlib",
    "Pytorch",
    "Scikit-learn",
    "Flask",
    "Langchain",
]
OTHERS = ["Git", "Github", "SQL", "SQlite", "Redis"]


def Home():
    return Div(
        Navbar(index=0),
        Div(
            Div(
                Span("About", cls="text-lg font-medium"),
                Div(
                    P(
                        "💼 I work as a data scientist @SmartPrints.",
                        cls="text-gray-500",
                    ),
                    P(
                        "I've been developing Computer vision systems for a while.",
                        cls="text-gray-500",
                    ),
                    P(
                        "🌱 I'm currently working on RAG systems and learning its Advanced concepts.",
                        cls="text-gray-500",
                    ),
                    cls="flex flex-col gap-1",
                ),
                cls="flex flex-col gap-4",
            ),
            Div(
                Span("Skills", cls="text-lg font-medium"),
                Span("🦿AI", cls="font-medium text-gray-400"),
                Div(
                    *[
                        Div(skill, cls="badge bg-gray-500 text-gray-200 badge-md")
                        for skill in AI_SKILLS
                    ],
                    cls="flex flex-row flex-wrap gap-2",
                ),
                Span("🌐Languages", cls="font-medium text-gray-400"),
                Div(
                    *[
                        Div(skill, cls="badge bg-gray-500 text-gray-200 badge-md")
                        for skill in LANGUAGES
                    ],
                    cls="flex flex-row flex-wrap gap-2",
                ),
                Span("⚙️Libraries", cls="font-medium text-gray-400"),
                Div(
                    *[
                        Div(skill, cls="badge bg-gray-500 text-gray-200 badge-md")
                        for skill in LIBRARIES
                    ],
                    cls="flex flex-row flex-wrap gap-2",
                ),
                Span("🛟Others", cls="font-medium text-gray-400"),
                Div(
                    *[
                        Div(skill, cls="badge bg-gray-500 text-gray-200 badge-md")
                        for skill in OTHERS
                    ],
                    cls="flex flex-row flex-wrap gap-2",
                ),
                cls="flex flex-col gap-4",
            ),
            Div(
                Span("Hobbies & Interests", cls="text-lg font-medium"),
                Div(Span("⚽ Football", cls="badge"), Span("🎞️ Tv shows", cls="badge")),
                cls="flex flex-col gap-2",
            ),
            cls="flex flex-col h-full w-full py-12 px-8 gap-12",
        ),
        cls="flex flex-row mx-auto min-h-screen w-full max-w-5xl gap-20",
    )
