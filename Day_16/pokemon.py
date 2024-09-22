from prettytable import PrettyTable
table = PrettyTable()
table.align = "l"


table.field_names = ["Pokemon","Type","Number"]
table.add_rows([
    ["Pikachu","Electric","xxx"],
    ["Charizard","Fire","xxx"],
    ["Gengar", "Ghost","xxx"]
    ])

print(table)