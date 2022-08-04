# Escreva uma função que recebe uma string não vazia e a comprims de forma a substituir as sequências de caracteres iguais por um contador seguido do caractere em si. Por exemplo, "AAA" deve ser cofidicado como "3A", "AABBB" como "2A3B" e assim por diante.0Para complicarmos um pouco, a astring de entrada pode conter qualquer caractere, incluindo números e caracteres especiais. E já que as strings codificadas devem ser decodificáveis, nós não podemos ingenuamente codificar uma string longa simplesmente pelo número de repetições. Por exemplo, "AAAAAAAAAAAA" não poderia ser codificada como "12A", uma vez que esta string poderia ser decodificada tanto como "AAAAAAAAAAAA" quanto "1AA". Logo, repetições de 10 ou mais caracteres, devem ser codificadas de forma dividida, ou seja, o exemplo acima deveria ser codificado como "9A3A".0Exemplo de entrada
# string = "BBBBBBBBBBBBBAACCCDD"
# Exemplo de saída
# "9b4b2a3c2d"

def codify(line: str):
    output = ''
    
    if len(line):
        for index, char in enumerate(line):
            char_sum = 1
            offset = 1
            
            if index > 0 and char == line[index - 1]:
                pass
            else:
                while index + offset < len(line) and char == line[index + offset]:
                    char_sum += 1
                    offset += 1
                    
                    if char_sum == 9:
                        output += f"{char_sum}{char}"
                        char_sum = 0
                
                if char_sum:
                    output += f"{char_sum}{char}"

    return output

string = "BBBBBBBBBBBBBBAACCCDD"
print(codify(string))