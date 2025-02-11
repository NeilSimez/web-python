from enum import Enum
import reflex as rx
from web.styles.colors import Color as Color
from web.styles.colors import TextColor as TextColor
from web.styles.fonts import Font as Font
#constans
MAX_WIDTH = "600px"

#sizes
STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css?family=Comfortaa:wght@300;500&display=swap"
]


class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    EXTRA = "1.3em"
    LARGE="1.5em"
    BIG="2em"
    
    
# Styles

BASE_STYLE = {
    "font_family":Font.DEFAULT.value,
    "font_weight":"300",
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding": Size.SMALL.value,
        "border_radius":Size.DEFAULT.value,
        "cursor":"pointer",
        "color":TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "_hover":{
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.link: {
        "text_decoration":"none",
        "_hover":{}
    },
    "html, body": {
        "margin": "0",
        "padding": "0",
        "height": "100%",
        "overflow-x": "hidden",
    },
    "main": {  # Asegurar que el contenido principal no cause desbordamiento
        "display": "flex",
        "flex_direction": "column",
        "min_height": "100vh",
    }
}

navbar_title_style = dict(
    # font_family=Font.LOGO.value,
    font_size =Size.LARGE.value
   
)

title_style = dict(
    color = TextColor.HEADER.value,
    width="100%",
    padding_top=Size.DEFAULT.value,
    font_family=Font.TITLE.value,
    font_weight="500"
   
)

button_title_style = dict(
    font_size = Size.EXTRA.value,
    color = TextColor.HEADER.value,
    font_weight="500"
)

button_body_style = dict(
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value,
    font_weight="300"
)

