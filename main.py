import math 

base = None 
altura = None
radio = None

while True:
    try:
        base = float(input('Escribir base del triangulo:'))
        break
    except:
        print('Escriba un número')
        


while True:
    try:
        altura = float(input('Escribir altura del triangulo:'))
        break
    except:
        print('Escriba un número')  
        
        
area = base * altura /2

print('El area del triángulo es:{}'.format(area))              

while True:
    try:
        radio = float(input('Escribir radio del circulo:'))
        break
    except:
        print('Escriba un número')


        

area = math.pi*(radio*radio)        


print('El area del circulo es:{}'.format(area))            






