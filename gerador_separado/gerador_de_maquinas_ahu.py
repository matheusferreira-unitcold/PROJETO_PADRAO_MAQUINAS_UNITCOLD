from itertools import product

# Definindo todas as opções por coluna
familias = ["CR-AHU"]
modelos = ["006", "013", "020", "027", "034", "051", "068", "102", "136", 
           "170", "204", "238", "272", "306", "340", "408"]
gabinete = ["S", "P", ""]  # Vazio possível
trocador = ["1,0/1", "4R"]
parceiros = ["SS", "TN", "DK", "LG"]
ventilador = ["", "LL", "PF", "EC"]  # Vazio possível
filtros = ["G4", "M5", "F8"]
finalizacoes = ["X"]

# Gerando todas as combinações
todas_combinacoes = product(
    familias, modelos, gabinete, trocador, parceiros, ventilador, filtros, finalizacoes
)

# Salvando em um arquivo CSV
with open("codigos_ahu.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Descricao da maquina\n")  # Cabeçalho
    for combo in todas_combinacoes:
        # Filtra campos vazios e junta os não-vazios com "-"
        linha = "-".join(valor for valor in combo if valor) + "\n"
        arquivo.write(linha)

print("Arquivo 'codigos_ahu.csv' gerado com sucesso!")