from prettytable import PrettyTable


table = PrettyTable() 


table.add_column("Pokemon",[ "Charmander", "Squirtle","Bulbasur"])
table.add_column("Type", ["Fire", "Water","Grass"])
table.add_column("Items", [1,5,2])

table.align = "c"
print(table)