# FERNANDO TORRES MEDINA
# COMPONENTE DE sACTIVIDAD 4. 

# EJE 1 CREAR UNA LISTA DE NOTAS
# Complete la lista con cinco notas y muestre la cantidad de elementos.
# %%

notas = (4.5, 3.8, 4.0, 5.0)
print(len(notas))
print(notas)

# EJE 2 ACCEDER POR ÍNDICE 
# Use índices para imprimir la primera, la tercera y la última temperatura.
# %%
temperaturas = [18, 20, 19, 21, 22]

print(temperaturas[0])
print(temperaturas[2])
print(temperaturas[4])

#EJE 3 ACTUALIZAR UN ELEMENTO
# Corrija la segunda venta, que fue registrada como 80 pero debía ser 85.
# %%

ventas = [120, 80, 200, 50]
ventas[1] = 85
print(ventas)

# EJE 4 AGREGAR Y EXTRAER DATOS
# Agregue una nueva nota y extraiga la última nota registrada
# %%
notas= [3.5, 4.0, 2.8]
notas.append(4.6)
ultima = notas.remove(2.8)
print(ultima)
print(notas)

# EJE 5 CALCULAR PROMEDIO
# Complete el acumulador para calcular el promedio de una lista.
# %%
notas = [4.2, 3.8, 5.0, 2.9]
total = 0

for nota in notas:
    total = total + nota
promedio = total /len(notas)
print(round(promedio, 2))

# EJE 6 CONTAR APROBADOS
# Cuente cuántas notas son mayores o iguales a 3.0.
# %%
notas = [4.2, 2.5, 3.0, 1.8, 4.7]
aprobados = 0
for nota in notas:
    if nota >= 3.0:
        aprobados = aprobados + 1
print(aprobados)

# EJE 7 FILTRAR VALORES VALIDOS
# Construya una lista con las temperaturas que estén entre -10 y 50 grados.
# %%
lecturas = [18, 21, -99, 19, 22]
validas = []
for t in lecturas:
    if t >= -10 and t <= 50:
        validas.append(t)
print(validas)

# EJE 8 ORDENAR SIN PERDER EL ORIGINAL
# Use sorted() para crear una lista ordenada sin modificar la lista inicial.
# %%
montos = [120000, 85000, 210000, 50000]
ordenados = sorted(montos)
print(montos)
print(ordenados)

# EJE 9 COMPRENSIÓN DE LISTAS
# Complete la comprensión para obtener los cuadrados de los números pares.
# %%
numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n**2 for n in numeros if n%2==0]
print(cuadrados_pares)

# EJE 10 LISTA ANIDADA
# Complete el doble ciclo para sumar todos los elementos de una matriz.
# %%
matriz = [[1, 2, 3], [4, 5, 6]]
total = 0
for fila in matriz:
    for valor in fila:
        total += valor
print(total)

# EJE 11 CREAR UNA TUPLA FIJA
# Defina una tupla con la latitud y la longitud de una sede.
# %%
ubicacion =(20, 30)
print(ubicacion)
print(type(ubicacion))

# EJE 12 DESEMPAQUETAR UNA TUPLA
# Asigne los elementos de la tupla a variables con nombres significativos.
# %%
registro = ("A01", "Laura", 4.6)
Id, nombre, nota = registro
print(nombre)
print(nota) 

# EJE 13 TUPLA DE UN SOLO ELEMENTO
# Complete la sintaxis correcta de una tupla que contiene un solo código.
# %%
codigo = ("A01",)
print(codigo)
print(type(codigo))

# EJE 14 CONVERTIR LISTA A TUPLA
# Convierta una lista de columnas a tupla para evitar cambios accidentales.
# %%
columnas = ["fecha", "monto", "cliente"]
columnas_fijas = tuple(columnas)
print(columnas_fijas)

# EJE 15 Retorno múltiple
# Complete una función que retorne el mínimo y el máximo como una tupla implícita.
# %%
def resumen(valores):
    menor = min(valores)
    mayor = max(valores)
    return menor, mayor
minimo, maximo = resumen ([8, 3, 10, 5])
print(minimo, maximo)

# EJE 16 RECONOCER INMUTABILIDAD
# Ejecute mentalmente el código y explique qué error se produce.
# RESPUESTA: PRODUCE ERROR
# %%
punto = (10, 20)
punto[0] = 99
print(punto)

# EJE 17 TUPLA COMO CLAVE
# Use una tupla como clave para almacenar una lectura por coordenada.
# %%
lecturas ={}
coordenada = (4.65, -74.05)
lecturas[coordenada] = 18.5
print(lecturas[(4.65, -74.05)])

# EJE 18 COMBINAR LISTAS CON ZIP
# Cree pares estudiante-nota usando zip() y conviértalos a lista.
# %%
nombres = ["Ana", "Luis", "Marta"]
notas = [4.2, 3.8, 5.0]
pares = list(zip(nombres, notas))
print(pares)

# EJE 19 CREAR UN DICCIONARIO
# Complete las claves necesarias para representar a un estudiante.
# %%
estudiante ={"Id": "A01", "nombre": "Laura", "nota": "4.6" }
print(estudiante)

# EJE 20 ACCESO SEGURO CON GET() 
# Use get() para consultar una clave que podría no existir.
# %%
cliente = {"nombre": "Carlos", "puntaje": 720}
saldo = cliente.get("saldo", 0)
print(saldo)

# EJE 21 ACTUALIZAR VALORES
# Actualice el stock de un producto después de una venta de 3 unidades.
# %%
producto = {"codigo": "P01", "stock": 8}
producto["stock"] = producto["stock"] -3
print(producto["stock"])

# EJE 22 RECORRER PARES CLAVE-VALOR
# Complete el recorrido para imprimir cada atributo con su valor.
# %%
producton = {"codigo": "P01", "precio": 12000, "stock": 8}
for clave, valor in producto.items():
    print(clave, valor)

# EJE 23 CONTAR POR CATEGORIA
# Use un diccionario acumulador para contar los tipos de transacción.
# %%
tipos = ["Debito", "Credito", "Debito", "Debito", "Credito"]
conteo = {}
for tipo in tipos:
    conteo[tipo] = conteo.get(tipo, 0) + 1
print(conteo)

#EJE 24 DICCIONARIO ANIDADO
# Acceda a la nota de Laura dentro de una estructura anidada.
# %%
grupo = {"A01": {"nombre": "Laura", "nota": 4.6}, "A02": {"nombre": "Luis", "nota": 3.8}}
print(grupo["A01"]["nota"])

# EJE 25 LISTA DE DICCIONARIOS
# Calcule el total de los montos en una lista de transacciones.
# %%
transacciones = [{"id": "T01", "monto": 120000}, 
                 {"id": "T02", "monto": 85000}, 
                 {"id": "T03", "monto": 210000}]
total = 0
for t in transacciones:
    total += t["monto"]
print(total)

# EJE 26 BUSCAR POR CODIGO
# Complete una búsqueda lineal sobre una lista de diccionarios.
# %%
estudiantes = [{"codigo": "A01", "nombre": "Laura"}, {"codigo": "A02", "nombre": "Luis"}]
buscado = "A02"
resultado = None
for e in estudiantes:
    if e ["codigo"] == "A02":
        resultado = e["nombre"]

        print(resultado)

# EJE 27 FILTRAR DICCIONARIOS
# Construya una lista con los nombres de los estudiantes aprobados.
# %%
estudiantes = [{"nombre": "Ana", "nota": 4.2},
               {"nombre": "Luis", "nota": 2.8}, 
               {"nombre": "Marta", "nota": 3.5}]
aprobados = []
for e in estudiantes:
    if e["nota"] >= 3.0:
        aprobados.append(e["nombre"])
print(aprobados)

# EJE 28 AGRUPAR POR ESTADO
# Agrupe los nombres de los clientes según su nivel de riesgo.
# %%
clientes = [{"nombre": "Ana", "riesgo": "bajo"},
            {"nombre": "Luis", "riesgo": "alto"},
            {"nombre": "Marta", "riesgo": "bajo"}]
grupo = {}

for c in clientes:
    riesgo = c["riesgo"]
    if riesgo not in grupo:
        grupo[riesgo] = []
    grupo[riesgo].append(c["nombre"])

print(grupo)

# EJE 29 INVENTARIO ACADEMICO
# Complete el reporte de los productos con stock bajo.
# %%
inventario = [
        {"producto": "Macador", "stock": 4},
        {"producto": "Cuaderno", "Stock": 20},
        {"producto": "Borrador", "stock": 2}
]

bajos = []

for item in inventario:
    if item["stock"] < 10:
        bajos.append(item["producto"])

print(bajos)

# EJE 30 MINI CASO INTEGRADOR
# Complete el algoritmo que calcula el total de los créditos mayores o iguales a 100000 y
# registra los clientes correspondientes.
# %%
transacciones = [
    {"cliente": "Ana", "tipo": "Credito", "monto": 120000},
    {"cliente": "Luis", "tipo": "Debito", "monto": 85000},
    {"cliente": "Marta", "tipo": "Credito", "monto": 210000}
]
total_creditos = 0
clientes = []

for t in transacciones:
    if t ["tipo"] == "Credito" and t ["monto"] >= 100000:
        total_creditos += t["monto"]
        clientes.append(t["cliente"])
print(total_creditos)
print(clientes) 
# %%
