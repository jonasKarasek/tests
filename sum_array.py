# Escreva uma função que recebe um array não vazio de inteiros distintos e um inteiro representando uma soma alvo. Se quiser dois números no array de entrada somam a soma alvo, a função deve retorná-los no array de saída, em qualquer ordem. Se nenhum par de números no array de entrada somarem a soma alvo, a função deve retornar um array vazio.1Note que a soma alvo deve ser obtida somando dois inteiros diferentes do array, você não pode somar um inteiro com ele mesmo.1Você pode assumir que existirá no máximo um par de números somando a soma alvo.1Exemplo de entrada
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10
# Exemplo de saída
# [-1, 11]

def func(array: list, target_sum: int):
    output = []
    
    if(len(array) < 2):
        return output

    for value1 in array:
        for value2 in array:
            if target_sum == value1 + value2 and value1 != value2:
                output = [value1, value2]

    return output

target_sum = 10
list = [3, 5, -4, 8, 11, 1, -1, 6]
print(func(list, target_sum))