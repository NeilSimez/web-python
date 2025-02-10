import reflex as rx
from web.styles.styles import Size as Size
from web.styles.colors import TextColor as TextColor
from web.styles.colors import Color as Color

def info_text(title:str,body:str) -> rx.Component:
    return rx.hstack(
        rx.text(title,
                font_weight="bold", 
                color=Color.PRIMARY.value
                ),
        body, 
        font_size= Size.MEDIUM.value,
        color=TextColor.BODY.value
    )