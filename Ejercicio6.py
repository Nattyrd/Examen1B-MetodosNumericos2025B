from numpy import pi, sin #Importamos solo lo necesario


def secante_metodo(f,x0,x1,tol=1e-6,max_iter=100):
    x_prev = x0
    x_curr = x1
    inter_count = 0
    while abs(f(x_curr)) > tol and inter_count < max_iter:
        
        x_next = x_curr - f(x_curr) * (x_curr - x_prev) / (f(x_curr) - f(x_prev))
        x_prev = x_curr
        x_curr = x_next
        inter_count += 1
    
    return x_curr, inter_count

cache = {} #diccionario de almacenamiento para reducir llamadas repetidas
i = 0 # contador 


#Funcion modificada con guardado en de los datos en cache
def func(x):
 global i
 if x in cache: #Revisa si el valor ya fue calculado para reutilizarlo.
  return cache[x]

 i += 1
 y = x**3 - 3 * x**2 + x - 1
 print(f"Llamada i={i}\t x={x:.5f}\t y={y:.2f}")
 cache[x] = y
 return y

# secante_metodo(func,2,3) #Logra reducir solo a 8 llamadas a la funcion en lugar de 25 del metodo original

#FUNCION PARA EL PRIMER EJECICIO

def func1(x):
 global i
 if x in cache: #Revisa si el valor ya fue calculado para reutilizarlo.
  return cache[x]

 i += 1
 y = x**3 + 2 * x**2 +3*x - 1
 print(f"Llamada i={i}\t x={x:.5f}\t y={y:.2f}")
 cache[x] = y
 return y

#EJECUCION DEL PRIMER EJERCICIO
# secante_metodo(func1,2,3) #Logra en 10 llamadas encontrar la raiz
 
 
#FUNCION PARA EL SEGUNDO EJERCICIO
cache2 = {} #diccionario de almacenamiento para EJE2
i2 = 0 # contador EJE2

def func2(x):
  global i2
  if x in cache2: #Revisa si el valor ya fue calculado para reutilizarlo.
   return cache2[x]

  i2 += 1
  y = 32 *sin(x/pi) + 10
  print(f"Llamada i={i2}\t x={x:.5f}\t y={y:.2f}")
  cache2[x] = y
  return y

#EJECUCION DEL SEGUNDO EJERCICIO
secante_metodo(func2,2,3) #Logra en 7 llamadas encontrar la raiz
