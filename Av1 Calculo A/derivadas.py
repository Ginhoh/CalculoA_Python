import sympy as smp
#Derivada simbólica
def dersim():
    x = smp.symbols('x')
    f = input("Digite a função: ")
    derivada = smp.diff(f,x)
    return(f'A derivada de {f}\n é igual a: \n{derivada}')

print(dersim())