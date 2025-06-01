import re

contraseña = input("Ingresa una contraseña: ")

if len(contraseña) >= 8:
    print("La contraseña es suficientemente larga.")
else:
    print("La contraseña es muy corta. Debe tener al menos 8 caracteres.")



contraseña = input("Ingresa una contraseña: ")

def es_segura(pwd):
    if len(pwd) < 8:
        return "❌ Muy corta (mínimo 8 caracteres)"
    if not re.search(r"[A-Z]", pwd):
        return "❌ Debe tener al menos una letra mayúscula"
    if not re.search(r"[a-z]", pwd):
        return "❌ Debe tener al menos una letra minúscula"
    if not re.search(r"[0-9]", pwd):
        return "❌ Debe tener al menos un número"
    if not re.search(r"[!@#$%^&*()_+=-]", pwd):
        return "❌ Debe tener un carácter especial"
    return "✅ Contraseña segura"

resultado = es_segura(contraseña)
print(resultado)
