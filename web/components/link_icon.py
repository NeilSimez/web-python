import reflex as rx
import web.styles.styles as styles


def link_icon(url,ico:str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=ico,
            href=url,
            is_external=True,
            size=20
        )
    )