from itertools import product

# Definindo todas as opções por coluna
familias = ["CR-UTV"]
modelos = ["010", "020", "030", "040", "050", "075", "100", "150", "200"]
gabinete = ["S", "P"]
trocador = ["1,0/1","4R"]
parceiros = ["SS", "TN", "DK", "LG"]
ventilador = ["EC"]
filtros = ["G4", "G4+M5", "G4+F9", "G4+F9+H14"]
finalizacoes = ["X"]

# Gerando todas as combinações
todas_combinacoes = product(
    familias, modelos, gabinete, trocador, parceiros, ventilador, filtros, finalizacoes
)

# Salvando em um arquivo CSV (opcional)
with open("codigos_utv.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Descricao da maquina\n")  # Cabeçalho
    for combo in todas_combinacoes:
        linha = "-".join(combo) + "\n"
        arquivo.write(linha)

print("Arquivo 'codigos_utv.csv' gerado com sucesso!")