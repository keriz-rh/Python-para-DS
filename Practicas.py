# Python para DS  -introducción al lenguaje

nombre = 'Armando';

edad = 26

# Mi primera Función.

print(f'Mi nombre es {nombre} y tengo {edad} años');

def saludar () :
  nombre = input('Digite su nombre');
  print(f'Hola {nombre} es placer saludarte')

saludar()

saludar()
Parametros
[ ]
Nombre = 'Andrea'
[ ]
def Saludar_con_parametro(nombre) :
  print(f'Hola {Nombre} es un gusto')
[ ]
Saludar_con_parametro(Nombre)
output
Hola Andrea es un gusto
[ ]
def Velocidad(distancia, tiempo) :
  v = distancia / tiempo ;
  print(f'Velocidad {v} m/s');


[ ]
Velocidad(100,20)
output
Velocidad 5.0 m/s
[ ]
