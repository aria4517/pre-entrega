productos=[]

while True:
    #menu
    print()
    print("Elija una opción:")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    #f ingresar datos
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        categoria = input("Ingrese la categoría del producto: ")
        productos.append([nombre, precio, categoria])
        print("Producto agregado exitosamente.")

    #f mostrar productos
    elif opcion==2:
        if len(productos) == 0:
            print("No hay productos para mostrar.")
        else:
            print("Lista de productos:")
            for i, producto in enumerate(productos):
                print(f"{i+1}. Nombre: {producto[0]}, Precio: {producto[1]}, Categoría: {producto[2]}")

    #f buscar un producto
    elif opcion==3:
        nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for producto in productos:
            if producto[0].lower() == nombre_buscar.lower():
                print(f"Producto encontrado: {producto[0]}, Precio: {producto[1]}, Categoría: {producto[2]}")
                encontrado = True
                break
        if not encontrado:
                print("Producto no encontrado.")

    #f eliminar un producto
    elif opcion==4:
        nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
        encontrado = False
        for i, producto in enumerate(productos):
            if producto[0].lower() == nombre_eliminar.lower():
                productos.pop(i)
                print("Producto eliminado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    #f salir
    elif opcion==5:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

