from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon","Type"]
table.add_rows([
    ["Pikachu","Electric"],
    ["Charizard","Fire"],
    ["Gengar", "Ghost"]
    ])

print(table)