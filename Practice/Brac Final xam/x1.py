cast = {'Friends': [('Joey', 'Matt'), ('Chandler', 'Matthew')],
         'BBT': [('Penny', 'Kaley'), ('Sheldon', 'Jim')],
         'Breaking Bad': [('Jesse', 'Aaron'), ('Walter', 'Bryan')]}

inp=input()
data = list(cast.values())

for series in cast:
    for couple in cast[series]:
        if inp==couple[1]:
            print(inp+" played the character "+couple[0]+" in "+series )
            



