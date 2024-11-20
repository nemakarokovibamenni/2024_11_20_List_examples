# gyümölcsök kiíratása
gyumolcsok = ['alma', 'körte', 'szilva', 'barack']

print(gyumolcsok)
for gyumolcs in gyumolcsok:
    print(gyumolcs)

# hónapok kiíratása
honapok = ['január', 'február','március', 'április', 'május', 'június', 'július'] 

for honap in honapok:
    print(honap)
print()

# index megjelenítése:
    # 0 január
    # 1 február

honap_index = 0
for honap in honapok:
    print(f"{honap_index} {honap}")
    honap_index += 1
print()

# index felhasználása sorszámok megadásához:
    # 1. január
    # 2. február

honap_index = 1
for honap in honapok:
    print(f"{honap_index}. {honap}")
    honap_index += 1
print(f"---🗓️Ezek a hónapok🗓️---")