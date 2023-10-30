import random

# Função principal para verificar se é primo
def miller_rabin(n, k):
    # Se o número for menor ou igual a 1, não é primo.
    if n <= 1:
        return False
    # Se o número for 2 ou 3, é primo.
    if n <= 3:
        return True
    # Se o número for par (exceto 2), não é primo.
    if n % 2 == 0:
        return False

    # Fatorizar n - 1 em 2^r * d
    r, d = 0, n - 1 # r é o expoente e d é o fator
    while d % 2 == 0: # Enquanto d for par
        r += 1 # r = r + 1
        d //= 2 # d = d // 2

    # Função para verificar se 'a' é uma testemunha da composição de 'n'
    def witness(a, d, n):
        x = pow(a, d, n) # x = a^d mod n
        if x == 1 or x == n - 1:
            return False # n é provavelmente primo
        for _ in range(r - 1): # 0 <= i <= r - 2
            x = pow(x, 2, n)
            if x == n - 1:
                return False # n é provavelmente primo
        return True # n é composto

    for _ in range(k):
        a = random.randint(2, n - 2) # 2 <= a <= n - 2
        if witness(a, d, n):
            return False # n é composto

    return True # n é provavelmente primo

# Exemplo de uso:
n = 53  # Número a ser testado
k = 10  # Número de testemunhas
if miller_rabin(n, k):
    print(f"{n} é primo.")
else:
    print(f"{n} é composto.")
