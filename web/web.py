"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import web.styles.styles as styles
from rxconfig import config
from web.components.navbar import navbar
from web.views.header.header import header
from web.views.links.links import links
from web.components.footer import footer
from web.styles.styles import Size as Size

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_y=Size.BIG.value,
            padding=Size.BIG.value
            )
        ),
        footer()
    )

app = rx.App(
    style=styles.BASE_STYLE,
     stylesheets=[
        "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:wght@100;400;700;900&display=swap",
    ],
)
app.add_page(
    index,
    title="YakshaTian | Links interesantes",
    description="Pagina que actualizaré para luego poner links sobre estudio",
    image="avatar2.jpg"
    )
