import json

with open('data.json', 'r') as file:
    data = json.load(file)

#Total Facturado

for listaventas, ventas in data.items():
    total_facturado = 0.0
    for venta in ventas:
        total_facturado = total_facturado + venta["precio_unitario"] * venta["cantidad"]
    print(f"El total facturado ha sido {total_facturado} €.")

#Ventas por categoria

for listaventas, ventas in data.items():
    ventas_por_categoria = {}
    for venta in ventas:
        categoria = venta["categoria"]
        cantidad = venta["cantidad"]
        if categoria not in ventas_por_categoria:
            ventas_por_categoria[categoria] = 0
        ventas_por_categoria[categoria] += cantidad
    print(f"Las ventas por categoria han sido {ventas_por_categoria}.")

#Producto más vendido

for listaventas, ventas in data.items():
    ventas_por_producto = {}
    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        if producto not in ventas_por_producto:
            ventas_por_producto[producto] = 0
        ventas_por_producto[producto] += cantidad

cantidadmasvendida = 0
productomasvendido = ""
for producto, cantidad in ventas_por_producto.items():
    if cantidad > cantidadmasvendida:
        cantidadmasvendida = cantidad
        productomasvendido = producto
print(f"El producto más vendido ha sido {productomasvendido} con {cantidadmasvendida} unidades.")
    
