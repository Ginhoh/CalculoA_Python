import sympy as sp

def calcular_limites():
    x = sp.symbols('x') # Definindo a variável simbólica
    f = input("Digite a função: ")# Função a ser analisada
    i = input('Digite o limite da função (use "oo" para infinito): ') # Ponto onde o limite será calculado

    limite = sp.limit(f,x,i) # Calculando o limite
    return(f'O limite de {f} quando x tende a {i} é: {limite}')


def limites_laterais():
    x = sp.symbols('x')
    f = input("Digite a função: ")
    i = input('Digite o limite da função (use "oo" para infinito): ')

    limite_direita = sp.limit(f,x,i, dir='+') # Calculando o limite pela direita
    limite_esquerda = sp.limit(f,x,i, dir='-') # Calculando o limite pela esquerda 

    
    return(f'''O limite de {f} quando x tende a {i} para a DIREITA é: {limite_direita}
O limite da de {f} quando x tende a {i} para a ESQUERDA é: {limite_esquerda}''')

    
def limites_infinito():
    x =sp.symbols('x')
    f = input('Digite a função: ')
    limite_direita = sp.limit(f,x,sp.oo) # Calculando o limite pelo infinito POSITIVO
    limite_esquerda = sp.limit(f,x,-sp.oo) # Calculando o limite pelo infinito NEGATIVO

    return(f'''O limite de {f} quando x tende a +oo é: {limite_direita}
O limite de {f} quando x tende a -oo é: {limite_esquerda}''')


print(limites_infinito())