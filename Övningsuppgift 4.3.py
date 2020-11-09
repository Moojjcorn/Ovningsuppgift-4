mål = int(input('Ange ett heltal antal kroner som är ditt mål: ')) #tar en input från användare som ger mål variabeln ett värde
mål = mål*100 # Konverterar kroner till öre
öre = 1 #startvärde på öre första dagen
dagar = 0 #dag räknare börjar på 0
while öre <= mål: #Loopa tills öre är lika mycket eller mer än ditt mål
    dagar = dagar + 1 #varje loop så lägger den till på dar räknaren
    öre = öre*2 #matten för att din lön dubblas varje dag
print(f'Det tog {dagar} dagar tills du uppnådde ditt mål på {mål/100:.0f} kr! ') #print som skriver ut dagar variablen och hur lång tid det tog för att nå ditt mål
