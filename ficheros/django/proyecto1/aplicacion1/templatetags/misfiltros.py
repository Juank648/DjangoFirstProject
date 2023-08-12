from django import template

register = template.Library()

def recortar(texto, valor):
    nuevo_texto = texto.replace(valor, '')
    return nuevo_texto

register.filter('recortar', recortar)