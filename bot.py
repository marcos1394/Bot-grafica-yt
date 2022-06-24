from ast import Return
from cgitb import html
from turtle import ht
import requests

TARJETA1 = "https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-space-gray/5721600.p?skuId=5721600&intl=nosplash"
TARJETA2 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440&intl=nosplash"
TARJETA3 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-ti-titanium-and-black/6502626.p?skuId=6502626&intl=nosplash"

CLASE_HTML = "c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"


PRODUCTOS = [
    ("Mac Book", TARJETA1),
    ("RTX 3080", TARJETA2),
    ("RTX 3090", TARJETA3)
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept": "/"
}

def guardar(contenido: str, nombre: str = "res.html" ) -> None:
    with open(nombre, "w", encoding="utf8") as f:
        f.write(contenido)


# JALAR LA PAGINA DEL PRODUCTO

def jalar_pagina(url: str) -> str:
    res = requests.get(url, headers=HEADERS)
    return res.text

def hay_en_existencia(html: str) -> bool:
    return CLASE_HTML in html


def main()->None:
    for nombre, url in PRODUCTOS:
        html = jalar_pagina(url)
        if hay_en_existencia(html):
            print(f"Corre! hay {nombre} en existencia! compralo ya: {url}")
        else:
            print(f"no hay {nombre} en existencia")
      

if __name__ == "__main__":
    seconds = 60 * 10
    contador = 1
    while True:
        print(f"corrida #{contador}")
        main()
        time.sleep(seconds)
        contador += 1



# VERIFICAR QUE EXISTE EL PRODUCTO



# INFORMAR SOBRE LA EXISTENCIA
