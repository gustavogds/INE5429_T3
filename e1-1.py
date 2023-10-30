import time

# Parâmetros do LCG
seed = int(time.time())  # Semente inicial baseada no tempo atual
a = 1664525
c = 12345
m = 2**64

# Essa função gera um número pseudo-aleatório com o tamanho especificado.
def generate_pseudo_random(bit_len):
    x = seed
    # Inicializa o número aleatório com 0.
    random_number = 0
    # O tamanho final do número pode não ser um múltiplo de 64, portanto, é preciso acompanhar os bits gerados.
    remaining_bits = bit_len

    # Aqui entra em um loop até que todos os bits tenham sido gerados (remaining_bits = 0).
    # Ele gera números aleatórios de 64 bits de cada vez, podendo ser menor de acordo com "remaining_bits".
    # Em seguida, é atualizado o número pseudo-aleatório com os bits gerados deslocando à esquerda em "random_bits"
    # e realizando uma operação OR bit a bit entre "random_number" deslocado e os bits mais significativos de "x" 
    # deslocado à direita em "64 - random_bits
    while remaining_bits > 0:
        x = (a * x + c) % m
        random_bits = min(remaining_bits, 64)  # Gere no máximo 64 bits de cada vez
        random_number = (random_number << random_bits) | (x >> (64 - random_bits))
        remaining_bits -= random_bits

    return random_number

# Tamanhos desejados em bits
bit_lens = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

# Gerar números pseudo-aleatórios e medir o tempo para cada tamanho
for bit_len in bit_lens:
    start_time = time.time()
    random_number = generate_pseudo_random(bit_len)
    end_time = time.time()
    generation_time = end_time - start_time

    print(f"Tamanho: {bit_len} bits")
    print(f"Número binário: {bin(random_number)[2:]}")  # Exibir o número em binário
    print(f"Número decimal: {random_number}")  # Exibir o número em decimal
    print(f"Tempo de geração: {generation_time:.6f} segundos\n")
