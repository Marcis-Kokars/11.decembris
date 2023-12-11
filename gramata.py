import json

data = [
    
    {"nosaukums": "Dabas Stāsti", "autors": "John Smith", "žanrs": "daba", "izdošanas_gads": 2019},
    {"nosaukums": "Programmēšanas Pamati", "autors": "Alice Johnson", "žanrs": "tehnoloģijas", "izdošanas_gads": 2020},
    {"nosaukums": "Kriminālromāns", "autors": "John Smith", "žanrs": "kriminālromāns", "izdošanas_gads": 2018}
]

grāmatu_skaits = len(data)
print(f"Kopējais grāmatu skaits: {grāmatu_skaits}")

autora_vārds = input("Ievadiet autora vārdu:")
autora_grāmatas = [grāmata for grāmata in data if grāmata['autors'] == autora_vārds]

if autora_grāmatas:
    print(f"{autora_vārds} grāmatas:")
    for grāmata in autora_grāmatas:
     print (f"{grāmata['nosaukums']} ({grāmata['izdošanas_gads']})")
elese:
    print(f"{autora_vārds} grāmata nav atrasta sarakstā.")

žanru_skaits = {}
for grāmata in data:
    žanrs = grāmata['žanrs']  
    žanru_skaits[žanrs] = žanru_skaits.get(žanrs, 0) + 1
     print(f"{žanrs}: {skaits} grāmatas")

