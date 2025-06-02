from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key, '')

@register.filter
def replace_underscore(value):
    """
    Reemplaza guiones bajos por espacios y convierte a Título.
    Ej: "referencia_fabricante" → "Referencia Fabricante"
    """
    if isinstance(value, str):
        return value.replace('_', ' ').title()
    return value