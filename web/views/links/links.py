import reflex as rx
from web.components.link_button import link_button
from web.components.title import title
from web.styles.styles import Size as Size
def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("twitch","Twitch","Directos de lunes a viernes", "https://twitch.com"),
         link_button("youtube","Youtube","Directos Semanales","https://www.youtube.com/"),
         link_button("youtube","Canal Secundario","Tutoriales Semanales","https://youtube.com"),
         link_button("headset","Discord","Escribeme","https://discord.com"),
         title("Segundo"),
         link_button("twitch","Twitch","Directos de lunes a viernes", "https://twitch.com"),
         link_button("Youtube","Directos Semanales","https://www.youtube.com/","youtube"),
         link_button("youtube","Canal Secundario","Tutoriales Semanales","https://youtube.com"),
         link_button("headset","Discord","Escribeme","https://discord.com"),
         title("Contacto"),
         link_button(
             "mail",
             "My Public inbox",
             "Respuesta rapida y con preferencia",
             "https://discord.com"
         ),
         link_button(
             "mail",
             "Email",
             "Respuesta rapida y con preferencia",
             "https://discord.com"
         ),
        width="100%",
        
        
       
    )