from bs4 import BeautifulSoup

def find_hidden_text(html):
    soup = BeautifulSoup(html, "html.parser")
    hidden_nodes = []

    for tag in soup.find_all(style=True):
        style = tag["style"].replace(" ", "").lower()
        if (
            "display:none" in style or
            "visibility:hidden" in style or
            "opacity:0" in style or
            "font-size:0" in style
        ):
            text = tag.get_text(strip=True)
            if text:
                hidden_nodes.append(text)

    return hidden_nodes
