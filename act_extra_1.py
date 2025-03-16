import os

inventario = [
    ('manzana',4),
    ('banana',3),
    ('zanahoria',0)
]

continue_program=True

while continue_program:

    os.system('cls')

    print("GESTIÓN DE INVENTARIOS")
    print("-"*35)

    #MENU
    print("1-AGREGAR PRODUCTO")
    print("2-ELIMINAR PRODUCTO")
    print("3-MOSTRAR INVENTARIO")
    print("4-SALIR")
    print()

    answer=int(input("Opción: "))
    print()

    match(answer):
        case 1:
            duplicate=False
            product_name=input("Ingrese el nombre del producto: ")
            for product in inventario:
                if product[0] == product_name.lower():
                    duplicate=True
            if duplicate:
                print("El producto ya existe en el inventario")
            else:
                amount=int(input("Ingrese la cantidad existente: "))
                inventario.append((product_name.lower(),amount))
                print("Producto agregado!")
            
        case 2:
            remove=False
            product_name=input("Ingrese el nombre del producto a eliminar: ")
            for product in inventario:
                if product[0] == product_name.lower():
                    inventario.remove(product)
                    remove=True
                    print("Producto removido del inventario")
                    break
            if not remove:
                print("El producto a eliminar no existe en el inventario")
        case 3:
            for product in inventario:
                print("Producto:",product[0]," Stock:",product[1])
        case 4:
            exit()
    print()
    input("Enter para continuar...")