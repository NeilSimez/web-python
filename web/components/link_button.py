import reflex as rx
import web.styles.styles as styles
from web.styles.styles import Size as Size


def link_button(ico:str,title:str,body:str,url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=ico,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin =Size.MEDIUM.value
                    
                ),
                rx.vstack(
                    rx.text(title,style=styles.button_title_style),
                    rx.text(body,style=styles.button_body_style),
                    spacing="2",
                    align_items="start",
                    margin="0px"
                )
                
            ),
            
        ),
        href=url,
        is_external=True,
        width="100%",
        
    )
    
    
