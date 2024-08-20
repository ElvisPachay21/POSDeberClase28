carrito = []
total = 0.0

def mostrar_menu():
    print("Bienvenido al POS")
    print("1. Agregar producto al carrito")
    print("2. Ver total del carrito")
    print("3. Eliminar producto del carrito")
    print("4. Pagar")
    print("5. Salir")

def agregar_producto():
    global total 
    
    producto = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico para el precio.")
    
    carrito.append({"producto": producto, "precio": precio})
    total += precio
    print(f"Has agregado {producto} al carrito por {precio:.2f}.")
    
def ver_total():
    print(f"El total de tu carrito es: {total:.2f}")

def eliminar_producto():
    global total
    
    if not carrito:
        print("El carrito está vacío. No hay productos para eliminar.")
        return
    
    print("Productos en el carrito:")
    for i, item in enumerate(carrito):
        print(f"{i + 1}. {item['producto']} - {item['precio']:.2f}")
    
    producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
    
    for i, item in enumerate(carrito):
        if item['producto'].lower() == producto_a_eliminar.lower():
            total -= item['precio']
            carrito.pop(i)
            print(f"Has eliminado {item['producto']} del carrito.")
            return
    
    print(f"El producto {producto_a_eliminar} no se encontró en el carrito.")
    
def pagar():
    global total, carrito 
    if total == 0:
        print("Tu carrito está vacío, no hay nada que pagar.")
    else: 
        print(f"El total a pagar es: {total:.2f}")
        while True:
            try:
                pago = float(input("Ingresa la cantidad con la que vas a pagar: "))
                break
            except ValueError:
                print("Por favor, ingresa un valor numérico para el pago.")
        
        if pago >= total:
            cambio = pago - total
            print(f"Pago realizado con éxito. Tu cambio es: {cambio:.2f}")
            
            carrito = []
            total = 0.0
        else:
            print("No tienes suficiente dinero para pagar.")
            
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_total()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            pagar()
        elif opcion == "5":
            print("Gracias por usar el POS. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

ejecutar()
 