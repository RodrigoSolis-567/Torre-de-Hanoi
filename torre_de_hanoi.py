
import time

def tiempo(n):

    print(f"Iniciando simulación para {n} discos...\n")
    
    # Capturar el tiempo de inicio
    tiempo_inicio = time.time()
    
    resolver_hanoi(n)
    
    # Capturar el tiempo de fin
    tiempo_fin = time.time()
    
    # Calcular la diferencia
    tiempo_total = tiempo_fin - tiempo_inicio
    print(f"\n Tiempo de ejecución para {n} discos: {tiempo_total:.6f} segundos.")

def Discos():
   
    #cantidad de discos
    while True:
        try:
            cantidad_discos = int(input("Ingresa la cantidad de discos a resolver: "))
            if cantidad_discos < 1:
                print("Por favor, ingresa un número mayor o igual a 1.\n")
                continue
            
            tiempo(cantidad_discos)
            break
        
        except ValueError:
            print("Error: Debes ingresar un número entero válido.\n")


#mwtodo principal
def resolver_hanoi(n):

    torres = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    #muestra de forma grafica las torres
    def grafica():

        for poste in ['A', 'B', 'C']:
            if torres[poste]:
                linea = " ".join([f"[{d}]" for d in torres[poste]])
            else:
                linea = "       | "
            print(f"Poste {poste}: {linea}")
        print("-" * 35)

    #mueve de posicion los discos y actualiza el metodo grafica()
    def mover(n_discs, origen, destino, auxiliar):
       
        if n_discs == 1:
            disco = torres[origen].pop()
            torres[destino].append(disco)
            print(f"Movimiento: Mover disco {disco} de [{origen}] ➔ [{destino}]")
            grafica()
            return
        
        mover(n_discs - 1, origen, auxiliar, destino)
        
        disco = torres[origen].pop()
        torres[destino].append(disco)
        print(f"Movimiento: Mover disco {disco} de [{origen}] ➔ [{destino}]")
        grafica()
        
        mover(n_discs - 1, auxiliar, destino, origen)

    # Mostrar la POSICIÓN INICIAL explícitamente antes de empezar
    print("=" * 10 + " POSICIÓN INICIAL " + "=" * 10)
    grafica()
    
    # Iniciar el proceso recursivo
    mover(n, 'A', 'C', 'B')

if __name__ == "__main__":
    Discos()

#Rodrikwk