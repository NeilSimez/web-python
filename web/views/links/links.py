import reflex as rx
from web.components.link_button import link_button
from web.components.title import title
from web.styles.styles import Size as Size
def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch","Directos de lunes a viernes", "https://twitch.com"),
        link_button("Youtube","Directos Semanales","https://www.youtube.com/"),
        link_button("Canal Secundario","Tutoriales Semanales","https://youtube.com"),
        link_button("Discord","Escribeme","https://discord.com"),
        title("Segundo"),
        link_button("Twitch","Directos de lunes a viernes", "https://twitch.com"),
        link_button("Youtube","Directos Semanales","https://www.youtube.com/"),
        link_button("Canal Secundario","Tutoriales Semanales","https://youtube.com"),
        link_button("Discord","Escribeme","https://discord.com"),
        width="100%",
        
        
       
    )