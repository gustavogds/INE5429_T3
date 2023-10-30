import random

def fermat(n, k):
    # Se o número for menor ou igual a 1, não é primo.
    if n <= 1:
        return False
    # Se o número for 2 ou 3, é primo.
    if n <= 3:
        return True
    # Se o número for par (exceto 2), não é primo.
    if n % 2 == 0:
        return False

    # Função para verificar se 'a' é uma testemunha da composição de 'n'
    def witness(a, n):
        if pow(a, n - 1, n) != 1: # a^(n-1) mod n != 1
            return True # n é composto
        return False # n é provavelmente primo

    for _ in range(k):
        a = random.randint(2, n - 2) # 2 <= a <= n - 2
        if witness(a, n):
            return False # n é composto

    return True # n é provavelmente primo

# Exemplo de uso:
n = 53  # Número a ser testado
k = 10  # Número de testemunhas
if fermat(n, k):
    print(f"{n} é primo.")
else:
    print(f"{n} é composto.")
