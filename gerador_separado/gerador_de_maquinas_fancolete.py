from itertools import product

# Definindo todas as opções por coluna
familias = ["CR-FTC", "CR-FTH", "CR-FTK", "CF-FCT"]
modelos = ["007", "010", "015", "020", "025", "030"]
trocador = ["0,7/1","1,0/1","2,0/1", "4R"]
parceiros = ["SS", "TN", "DK", "LG"]
ventilador = ["EC", "AC"]
filtros = ["G4", "G4+M5", "G4+F9", "G4+F9+H14"]
finalizacoes = ["X"]

# Gerando todas as combinações
todas_combinacoes = product(
    familias, modelos, trocador, parceiros, ventilador, filtros, finalizacoes
)

# Salvando em um arquivo CSV (opcional)
with open("codigos_fancolete.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("Descricao da maquina\n")  # Cabeçalho
    for combo in todas_combinacoes:
        linha = "-".join(combo) + "\n"
        arquivo.write(linha)

print("Arquivo 'codigos_fancolete.csv' gerado com sucesso!")