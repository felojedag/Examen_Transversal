productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}
#stock={modelo[precio][stock]}


def stock_marca(marca):
    total=0
    encontrado=False
    for modelo in productos:
        if productos[modelo]['marca'].lower()==marca.lower():
            total+=productos[modelo]
            encontrado=True
        if encontrado:
            print("Stock disponible ",total)
        else:
            print("La marca que ingreso no existe dentro del stock")

def busqueda_precio(p_min,p_max):
    modelos_en_rango=[]
    for modelo in productos:
        precio=stock[modelo]['precio']
        stock=stock[modelo]['stock']
        if precio>=0 and p_min<=precio<=p_max:
            modelo=stock['modelo']
            modelos_en_rango.append(modelo)
            modelos_en_rango.sort()
        if modelos_en_rango:
            print("Notebooks",list)


def actualizar_precio(modelo,precio_nuevo):
    if modelo in productos:
        productos[modelo]['precio']
        print("Precio actualizado!!")
        print(f"modelo:{modelo}precio:{stock[modelo]['precio']}")
    else:
        print("El modelo no existe!!")

def main():
    while True:
        print("***MENU PRINCIPAL***")
        print("1.-Stock marca.")
        print("2.-Busqueda por precio")
        print("3.-Actualizar precio.")
        print("4.-Salir")

        opcion=int(input("Ingresar una opción del menú(1-4): "))
        if opcion==1:
            marca=input("Ingresar la marca para revisar stock: ")
            stock_marca(marca)
        elif opcion==2:
            while True:
                try:
                    p_min=int(input("Ingresar el valor minimo a buscar: "))
                    p_max=int(input("Ingresar el valor máximo a buscar"))
                    busqueda_precio()
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
                    return
        elif opcion==3:
            modelo=input("Ingresar el modelo a actualizar")
            while True:
                try:
                    precio_nuevo=int(input("Ingresar el nuevo precio del producto: "))
                    actualizar_precio(modelo,precio_nuevo)
                except ValueError:
                    print("Ingresar solo números enteros")
        elif opcion==4:
            print("Programa finalizado")
            break
        else:
            print("Opción no valida")
main()