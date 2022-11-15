print(' carade chango marango')
print(' ')
print(' ')
print(' ')
print(' ')
print('''Escriba 1) para suma de n numeros, #ya lo corregi angel era quitarle lo de arriba de este renglon y cmabiar una cosa de mas abajo.
      2) para producto de n numeros, 
      3) para division de 2 numeros, 
      4) para factorial, 
      5) para tablas, 
      6) para cuadrado y cubo, 
      7) para promedio, 
      8) para valor maximo y minimo''')
      
operacion = int(input("1, 2, 3, 4, 5, 6, 7, 8 "))# aqui te falto ponerle el "int" y los parenetesis recuerda que aqui para transformar una cadena de texto a entero se hace eso que te dije.
 
if operacion == 1:
      print(' No hay operacion')
elif operacion == 2:
      print(' no hay operacion')
elif operacion == 3:
      numero1=int(input("ingrese un numero"))
      numero2 = int(input("ingrese otro numero "))
      print(numero1 / numero2)
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
      num=int(input('Introducir un numero: '))
      cuadrado= num*num
      print('El cuadrado de',num,'es: ', cuadrado)
else:
    print(' caracter invalido')
