from itertools import product

# Definindo todas as opções por coluna
familias = ["CR-UTA"]
modelos = ["0510","1010","1510","2010","2015","2020","2520","2540","3020","3025","3030","3035","3530","4030","4530"]
gabinete = ["S", "P","DD-S","DD-P"]
trocador = ["5,0/1","4R","6R"]
parceiros = ["SS", "TN", "DK", "LG"]
ventilador = ["LL","PF","EC"]
filtros = ["G4", "G4+M5", "G4+F9", "G4+F9+H14"]
finalizacoes = ["X"]

# Gerando todas as combinações
todas_combinacoes = product(
    familias, modelos, gabinete, trocador, parceiros, ventilador, filtros, finalizacoes
)

# Salvando em um arquivo CSV (opcional)
with open("codigos_uta.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Descricao da maquina\n")  # Cabeçalho
    for combo in todas_combinacoes:
        linha = "-".join(combo) + "\n"
        arquivo.write(linha)

print("Arquivo 'codigos_uta.csv' gerado com sucesso!")