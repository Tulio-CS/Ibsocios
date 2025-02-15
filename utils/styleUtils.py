from config import *


def get_style(color,title,status,text):
    text = f'<div style="background-color:{colors[color]["background"]}; padding:10px; border-radius:10px;">
            <b style="color:{colors[color]["background"]};">{title}</b> <span style="float:right;">{status}</span><br>
            {text}</div>'
    return text