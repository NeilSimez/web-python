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
    style=styles.BASE_STYLE
)
app.add_page(index)
