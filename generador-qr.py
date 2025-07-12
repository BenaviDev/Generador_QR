#!/usr/bin/env python3
import qrcode
# CONFIGURACIÓN (EDITAR ESTO)
URL_MALICIOSA = "https://url"  # URL
ARCHIVO_SALIDA = "sigueme.png"    #img
# Generar QR
qr = qrcode.make(URL_MALICIOSA)
qr.save(ARCHIVO_SALIDA)
print(f"[+] QR generado: {ARCHIVO_SALIDA}")
print(f"[!] Redirige a: {URL_MALICIOSA}")







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