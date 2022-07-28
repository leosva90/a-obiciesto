def imc(estatura, peso):
    return peso/ estatura**2

peso = float(input('Escriba su peso (kg):'))
estatura = float(input('Escriba su estatura (M):'))

indice = imc(estatura,peso)

print('Su Indice de masa corporal es: {}'.format(indice))





