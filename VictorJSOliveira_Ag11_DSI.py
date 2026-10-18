from colorama import Fore, Style, init

init()

niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Médio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto (alerta)"},
]

def obter_cor_nivel(nivel):
    """Retorna a cor correspondente a cada nível."""
    match nivel:
        case 1:
            return Fore.RED
        case 2:
            return Fore.YELLOW
        case 3:
            return Fore.GREEN
        case 4:
            return Fore.CYAN
        case 5:
            return Fore.BLUE
        case _:
            return Fore.WHITE

entrada = input("Qual o nível do Reservatório? (1 a 5): ")

if entrada.isdigit():
    nivel_escolhido = int(entrada)
    registro_encontrado = None
    for item in niveis_reservatorio:
        if item["nivel"] == nivel_escolhido:
            registro_encontrado = item
            break

    if registro_encontrado:
        cor = obter_cor_nivel(nivel_escolhido)
        situacao = registro_encontrado["situacao"]
        print(f"{cor}Nível {nivel_escolhido}: {situacao}{Style.RESET_ALL}")
    else:
        print("Nível inválido! Digite um número de 1 a 5.")
else:
    print("Por favor, digite apenas números inteiros.")