def determinar_rango_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "VLAN del rango normal"
    elif 1006 <= vlan <= 4094:
        return "VLAN del rango extendido"
    else:
        return "Número de VLAN fuera de rango"

try:
    vlan = int(input("Introduce el número de VLAN: "))
    print(determinar_rango_vlan(vlan))
except ValueError:
    print("Por favor, introduce un número entero.")
