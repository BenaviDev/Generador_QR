#!/usr/bin/env python3
import qrcode
#Configuracion /editar/
url= "https://ejemplo.com" #url
salida= "imagen.png" # imagen de salida
#Generar QR funcion
qr =qrcode.make(url)
qr.save(salida)
print(f" QR GENERADO !: {salida}") 
print(f" REDIRIGE A: {url}") 
