import requests

TARJETA1 = "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-12gb-gddr6-pci-express-4-0-graphics-card/6468910.p?skuId=6468910&intl=nosplash"
TARJETA2 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440&intl=nosplash"
TARJETA3 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-ti-titanium-and-black/6502626.p?skuId=6502626&intl=nosplash"

CLASE_HTML = "c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"


HEADERS = {
    "User-Agent": "Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept": "/"
}

def guardar(contenido: str, nombre: str = "res.html" ) -> None:
    with open(nombre, "w") as f:
        f.write(contenido)


# JALAR LA PAGINA DEL PRODUCTO

def jalar_pagina(url: str) -> str:
    res = requests.get(url, headers=HEADERS)
    return res.text


html = jalar_pagina(TARJETA1)

guardar(html)

# VERIFICAR QUE EXISTE EL PRODUCTO



# INFORMAR SOBRE LA EXISTENCIA
