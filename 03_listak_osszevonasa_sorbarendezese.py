"""
Hozz létre két listát: [3, 1, 4] és [9, 7, 2]. 
Egyesítsd a két listát, és rendezd a lista elemeit növekvő sorrendbe!
"""


# írasd ki az első és az utolsó elemet!

lista_egy = [3, 1, 4]
lista_ketto = [9, 7, 2]

osszevont = lista_egy + lista_ketto
osszevont.sort()
print(osszevont)