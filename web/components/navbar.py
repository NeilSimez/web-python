import reflex as rx
from web.styles.styles import Size as Size
import web.styles.styles as styles
from web.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text.span("Yaksha",color=Color.PRIMARY.value),
            rx.text.span("Tian",color=Color.SECONDARY.value),
            style=styles.navbar_title_style
            ),
       
           
       
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )