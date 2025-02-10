import reflex as rx
import datetime
from web.styles.styles import Size as Size
from web.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"© 2025-{datetime.date.today().year} NeilzSimez",
                font_size=Size.MEDIUM.value
                ),
        rx.text(
                "Todos los derechos reservados",
                font_size=Size.MEDIUM.value,
                margin_top="0px !important"
                ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value,
        align="center"
    )