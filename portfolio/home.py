from fasthtml.common import H1, Div, Img, P, Span, A


def Home():
    return Div(
        Div(
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
                A(Span("Home", cls="font-medium"), cls="flex items-center py-1 gap-2"),
                A(Span("About", cls="font-medium"), cls="flex items-center py-1 gap-2"),
                A(
                    Span("Projects", cls="font-medium"),
                    cls="flex items-center py-1 gap-2",
                ),
                A(
                    Span("Contact", cls="font-medium"),
                    cls="flex items-center py-1 gap-2",
                ),
                cls="flex flex-col h-full w-full px-2 py-8 gap-4",
            ),
            cls="flex flex-col h-full w-64 px-2 py-12 gap-8",
        ),
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
