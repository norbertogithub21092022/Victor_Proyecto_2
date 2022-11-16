print(' ')
print(' ')
print(' ')
print(' ')

print('''Escriba 1) para suma de n numeros, 
      2) para producto de n numeros, 
      3) para division de 2 numeros, 
      4) para factorial, 
      5) para tablas, 
      6) para cuadrado y cubo, 
      7) para promedio, 
      8) para valor maximo y minimo''')
      
operacion = int(input("Escoja una opcion... ------> "))
 
if operacion == 1:
      print(' ')
      print(' ')
      print(' ')
      print(' ')
      n = 0
      c = 0
      suma = 0
      while n >= 0:
            n = int(input(' Ingresa un numero ----> '))
            if n != 0:
                  c = c + 1
                  suma = suma + n 
      print(' El total de la suma es ----> ', suma)
    
elif operacion == 2:
      x = 1
      producto = 0
      res = 1
      while x != 0:
            x = int(input(' Ingresa tu numero: '))
            if x != 0:
                  res = res * x
                  producto = res
      print(' La suma de la multiplicacion es: ',producto)
            
elif operacion == 3:
      print(' ')
      print(' ')
      print(' ')
      numero1=int(input("ingrese un numero ----> "))
      print(' ')
      print(' ')
      numero2 = int(input("ingrese otro numero ----> "))
      print('El resultado de la division es: ',numero1 / numero2)
elif operacion == 4:
      print(' ')
      
elif operacion == 5:
      tabla=int(input(' Elige la tabla a imprimir selecciona el numero de la tabla del 1 al 10')) 
      if tabla == 1:
            i=1
            while i <=10:
                  print(i)
                  i += 1 
      elif tabla == 2:
            i=2
            while i <=20:
                  print(i)
                  i += 2
      elif tabla == 3:
            i=3
            while i <=30:
                  print(i)
                  i += 3
      elif tabla == 4:
            i=4
            while i <=40:
                  print(i)
                  i += 4
      elif tabla == 5:
            i=5
            while i <=50:
                  print(i)
                  i += 5
      elif tabla == 6:
            i=6
            while i <=60:
                  print(i)
                  i += 6
      elif tabla == 7:
            i=7
            while i <=70:
                  print(i)
                  i += 7
      elif tabla == 8:
            i=8
            while i <=80:
                  print(i)
                  i += 8
      elif tabla == 9:
            i=9
            while i <=90:
                  print(i)
                  i += 9
      elif tabla == 10:
            i=10
            while i <=100:
                  print(i)
                  i += 10

elif operacion == 6:
      print(' ')
      print(' ')
      print(' ')
      print(' ')
      num=int(input('Introducir un numero: '))
      cuadrado= num*num
      print('El cuadrado de ',num,'es: ', cuadrado)
else:
    print(' Caracter invalido')