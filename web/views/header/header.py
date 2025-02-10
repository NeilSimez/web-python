import reflex as rx
from web.components.link_icon import link_icon
from web.components.info_text import info_text
from web.styles.styles import Size as Size
from web.styles.colors import TextColor as TextColor
def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.avatar(name="NeilSmez", fallback="NS",size="7",radius="full"),
        rx.vstack(
            rx.heading("Daniel Gómez",size="6",
                       color=TextColor.HEADER.value),
            rx.text(
                "@YakshaTian",
                margin_top="0px",
                color=TextColor.BODY.value
            ),
            rx.hstack(link_icon("https://x.com","facebook"),
            link_icon("https://x.com","instagram"),
            link_icon("https://x.com","twitch"),
            ),
            align_items="start",
            margin_top="1em"
        ),
       
       
        ),
        rx.flex(
            info_text("+3","Meses de experiencia"),
            rx.spacer(),
            info_text("+2","Aplicaciones Creadas"),
            rx.spacer(),
            info_text("+0","Seguidores"),
            width="100%"
        ), 
        
        rx.text("Actualmente estoy estudiando python por lo cual es es mi primera pagina web, espero que quede lo mejor posible experimentando con el framework: Reflex",color=TextColor.BODY.value),
        spacing="7",
        align_items="start",
        margin_bottom=Size.BIG.value
    )
    
    
