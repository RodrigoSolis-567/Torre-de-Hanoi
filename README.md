# Torre-de-Hanoi
Este programa recrea a, partir de código en lenguaje Python, el funcionamiento lógico-matemático del conocido juego de la Torre de Hanói, el cual consiste en una serie de discos apilados dentro de un poste, y otros dos postes donde deben de pasarse los discos, de tal forma de que solo se pase un disco de uno en uno y que ningún disco este sobre uno más pequeño. El programa simula los movimientos que se deben realizar para acomodar los discos de forma óptima, aparte de medir el tiempo que tarda el programa en hacer está operación.

Métodos
Método Discos()
Este método se encarga de solicitar al usuario la cantidad de discos, esto mediante una entrada a consola “input”, asegurando que sea un int, en caso de no serlo o ser menor a 1 el programa vuelve a preguntar el número de disco, así asegurando que la pila funcione correctamente y que no active el método tiempo() antes de requerirse.

Método tiempo()
Se encarga de la medición del tiempo de ejecución del programa, específicamente de la ejecución de la resolución de la torre de Hanói, ya que no toma en cuenta el tiempo transcurrido durante el método discos(), por lo que el tiempo que tardas en introducir la cantidad de discos no se contabiliza.

Método resolver_hanoi()
Es el método principal del programa. Utiliza un diccionario de pilas, llamadas ‘A’ ‘B’ y ‘C’, que actúan a modo de postes de la torre de Hanói, donde los datos se irán moviendo. Este método contiene los métodos grafico() y mover(), que constituyen el funcionamiento general de la torre de Hanói.
        
Método grafico()
Se encarga de imprimir en la consola la representación grafica de los discos de la torre de Hanói, mostrando el estado actual de la torre. Este representa a los discos como números entre corchetes “[n]” y a los postes vacíos como barras verticales “ | “, permitiendo entender de mejor manera la resolución de la Torre de Hanói.

Método mover()
Es el encargado del cálculo y resolución de la torre de Hanói, el mueve los datos, que representan los discos, entre las pilas, que representan los postes, según las reglas de una torre de Hanói real: solo mover un disco a la vez y evitar colocar un disco grande sobre uno más pequeño. Este proceso funciona según la cantidad de discos asignados en el método discos(), utilizando la recursividad para poder hacer el proceso hasta que se logre trasladar los discos de un poste a otro y actualizando el método grafica() cada que se realiza un movimiento.

Tiempos

Tiempo estimado con 5 discos
Con 5 discos el programa tardo un total de 0.007427 segundos el cronometro del programa, haciendo alrededor de 32 movimientos.

Tiempo estimado con 10 discos
Con 10 discos el programa tardo un total de 0.316064 segundos según el cronometro del programa, haciendo alrededor de 1024 movimientos.

Tiempo estimado con 30 discos
Luego de alrededor de 1 horas, el programa seguía ejecutándose, por lo cual y por cuestiones de tiempo se decidió parar la ejecución del programa. Con ayuda de la IA se calculó que el total de movimientos del programa debería hacer serian de 2^{30}-1 movimientos, alrededor de mil millones, y el tiempo de ejecución teórico seria de 6 horas continuas.

Tiempo estimado con 64 discos
Luego de alrededor de 2 horas, el programa seguía ejecutándose, por lo cual, al igual que el tiempo anterior,  por cuestiones de tiempo se decidió parar la ejecución del programa. Con ayuda de la IA se calculo que el total de movimientos del programa debería hacer serian de 2^{64}-1 movimientos, alrededor de 18 trillones, y el tiempo de ejecución teórico seria de 584,000 años, lo cual es imposible para la maquina por lo que terminaría de ejecutarse una vez la RAM alcance su límite de memoria
