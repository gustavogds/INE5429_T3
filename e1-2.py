import time

# classe do gerador Xorshift32
class Xorshift32:
    def __init__(self, seed):
        self.state = seed

    def random(self):
        # Aqui é feito um deslocamento/shift de 13 bits para a esquerda no estado atual, e realiza um XOR entre o estado original e o estado deslocado.
        self.state ^= (self.state << 13)
        # Aqui é feito um deslocamento/shift de 17 bits para a direita no estado atual, e realiza um XOR entre o estado original e o estado deslocado.
        self.state ^= (self.state >> 17)
        # Aqui é feito um deslocamento/shift de 5 bits para a esquerda no estado atual, e realiza um XOR entre o estado original e o estado deslocado.
        self.state ^= (self.state << 5)
        # Retorna o estado atual com os 32 bits menos significativos.
        return self.state & 0xFFFFFFFF

# Essa função gera um número pseudo-aleatório com o tamanho especificado.
def generate_pseudo_random(bit_len):
    # Cria uma instância do gerador Xorshift32 com a semente baseada no tempo atual.
    rng = Xorshift32(seed=int(time.time()))
    # Inicializa o número aleatório com 0.
    random_number = 0
    # O tamanho final do número pode não ser um múltiplo de 32, portanto, é preciso acompanhar os bits gerados.
    remaining_bits = bit_len

    # Aqui entra em um loop até que todos os bits tenham sido gerados (remaining_bits = 0).
    # Ele gera números aleatórios de 32 bits (random_part) e adiciona esses bits ao número aleatório (random_number)
    # usando uma operação de deslocamento/shift para a esquerda e um operador OR bit a bit.
    while remaining_bits > 0:
        random_bits = min(remaining_bits, 32)
        random_part = rng.random()
        random_number = (random_number << random_bits) | random_part
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