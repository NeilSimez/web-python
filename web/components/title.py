import reflex as rx
import web.styles.styles as styles


def title(text:str) -> rx.Component:
    return rx.heading(
       text,
       size="8",
       style=styles.title_style
      
    )