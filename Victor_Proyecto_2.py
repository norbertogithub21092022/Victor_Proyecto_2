from tkinter import Menu
Menu = '''Escriba 1) para suma de n numeros,
      2) para producto de n numeros, 
      3) para division de 2 numeros, 
      4) para factorial, 
      5) para tablas, 
      6) para cuadrado y cubo, 
      7) para promedio, 
      8) para valor maximo y minimo'''

print(Menu)
      
operacion = input("1, 2, 3, 4, 5, 6, 7, 8 ");
 
if operacion is 1:
      print(' ')
elif operacion is 2:
      print(' ')
elif operacion is 3:
      numero1=int(input("ingrese un numero"))
      numero2 = int(input("ingrese otro numero "))
      print(numero1 / numero2)
elif operacion is 4:
      print(' ')
      
elif operacion is 5:
      tabla=int(input(' Elige la tabla a imprimir selecciona el numero de la tabla del 1 al 10')) 
      if tabla is 1:
            i=1
            while i <=10:
                  print(i)
                  i += 1 
      elif tabla is 2:
            i=2
            while i <=20:
                  print(i)
                  i += 2
      elif tabla is 3:
            i=3
            while i <=30:
                  print(i)
                  i += 3
      elif tabla is 4:
            i=4
            while i <=40:
                  print(i)
                  i += 4
      elif tabla is 2:
            i=5
            while i <=50:
                  print(i)
                  i += 5
      elif tabla is 2:
            i=6
            while i <=60:
                  print(i)
                  i += 6
      elif tabla is 2:
            i=7
            while i <=70:
                  print(i)
                  i += 7
      elif tabla is 2:
            i=8
            while i <=80:
                  print(i)
                  i += 8
      elif tabla is 2:
            i=9
            while i <=90:
                  print(i)
                  i += 9
      elif tabla is 2:
            i=10
            while i <=100:
                  print(i)
                  i += 10

elif operacion is 6:
      num=int(input('Introducir un numero: '))
      cuadrado= num*num
      print('El cuadrado de',num,'es: ', cuadrado)
else:
    print(' caracter invalido')