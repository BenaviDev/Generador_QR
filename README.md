# 🚀 Generador de Código QR en Python (Solo 10 líneas!)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green)](https://opensource.org/licenses/MIT)

Un script minimalista en Python que genera códigos QR como imágenes PNG en segundos. ¡Perfecto para desarrolladores, educadores y entusiastas de la tecnología!
---

## ✨ Características Destacadas

- ⚡ **Generación instantánea** de códigos QR
- 🪶 **Solo 10 líneas** de código esencial
- 🎨 **Personalización flexible** de URL y nombre de salida
- 📁 **Salida en formato PNG** listo para usar
- 💻 **Multiplataforma** (Windows, Linux, macOS)

---


---

## 🛠️ Tecnologías Utilizadas
Python - Lenguaje base

qrcode - Librería de generación QR

Pillow - Procesamiento de imágenes

---

## 🖼️ Demo Visual
| Estilo 1 | Estilo 2 | Estilo 3 |
|-----------|-----------|------------|
| <img src="https://raw.githubusercontent.com/BenaviDev/Generador_QR/main/github_qr_pro.png" width="150"> | <img src="https://raw.githubusercontent.com/BenaviDev/Generador_QR/main/Tiktok.png" width="150"> | <img src="https://raw.githubusercontent.com/BenaviDev/Generador_QR/main/Tikto2.png" width="150"> |


<img src="(https://github.com/BenaviDev/Generador_QR/blob/main/elque%20es.png)" width="300">

Tambien es posible cambiar el tamaño de los codigos QR

## 🛠 Visual del codigo

```bash
#!/usr/bin/env python3
import qrcode

# Configuración EDITA TUS CODIGOS
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=4,  # TAMAÑ0 DEL CODIGO
    border=2, # BORDE EXTERIOR
)
qr.add_data("https://www.tiktok.com/@santiangobrz.5")
qr.make(fit=True)

img = qr.make_image(fill_color="#f5b041", back_color="#f0f0f0")  # Colores del QR 
img.save("img.png") #NOMBRE DEL FORMATO PNG QUE SE VA A GENERAR
```
---


## ⚙️ Instalación y Uso

### Prerrequisitos
- Python 3.10 o superior
- Gestor de paquetes `pip`

### Pasos rápidos
```bash
# 1. Instalar dependencia
pip install qrcode[pil]

# 2. Copiar y pegar el script

# 3. Ejecutar
python Generador_QR.py

```
---

## 📬 Contacto

**Santiago Benavidez Ramirez**  

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sbenavidezr29@gmail.com)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@HackeandoPatos)
[![TikTok](https://img.shields.io/badge/TikTok-%23000000.svg?style=for-the-badge&logo=TikTok&logoColor=white)](https://www.tiktok.com/@hackeadopatos(https://www.tiktok.com/@santiangobrz.5))


