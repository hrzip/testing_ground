cijena1 = 10.5
cijena2 = 5.75
print("Prva cijena: {:.2f} kn, Druga cijena: {:.2f} kn".format(cijena1, cijena2))
# Ispisuje: Prva cijena: 10.50 kn, Druga cijena: 5.75 kn




cijena1 = 10.5
cijena2 = 5.75
print("Prva cijena: {:.2f} kn, Druga cijena: {:.2f} kn".format(cijena1, cijena2))
# Ispisuje: Prva cijena: 10.50 kn, Druga cijena: 5.75 kn




cijena = 10.5
popust = 0.2
konacna_cijena = cijena * (1 - popust)
print("Originalna cijena: {0:.2f} kn, Popust: {1:.2f}%, Konačna cijena: {2:.2f} kn".format(cijena, popust * 100, konacna_cijena))
# Ispisuje: Originalna cijena: 10.50 kn, Popust: 20.00%, Konačna cijena: 8.40 kn

'''`{0:.2f}` znači "uzmi prvi argument (indeks 0) iz `.format()` i formatiraj ga kao float s 2 decimale" - to je `cijena`
`{1:.2f}` znači "uzmi drugi argument (indeks 1) iz `.format()` i formatiraj ga kao float s 2 decimale" - to je `popust * 100`
`{2:.2f}` znači "uzmi treći argument (indeks 2) iz `.format()` i formatiraj ga kao float s 2 decimale" - to je `konacna_cijena`'''





print("Rezultat: {broj:.2f}".format(broj=123.456789))
# Ispisuje: Rezultat: 123.46





postotak = 0.12345
print("Postotak uspjeha: {:.2f}%".format(postotak * 100))
# Ispisuje: Postotak uspjeha: 12.35%





''' Zadatak 1: Izračun PDV-a

Napišite program koji traži od korisnika da unese cijenu proizvoda bez PDV-a, 
a zatim ispiše cijenu s PDV-om (25%) formatiranu na dvije decimale.
'''


# Početak koda
cijena_bez_pdv = float(input("Unesite cijenu bez PDV-a: "))
# Dovršite kod...


#Rješenje:
cijena_bez_pdv = float(input("Unesite cijenu bez PDV-a: "))
cijena_s_pdv = cijena_bez_pdv * 1.25  # Dodajemo 25% na osnovnu cijenu
print('Cijena s PDV-om: {:.2f} kn'.format(cijena_s_pdv))




'''### Zadatak 2: Kalkulator napojnice

Napišite program koji traži od korisnika da unese iznos računa u restoranu i postotak napojnice koji želi ostaviti. 
Program treba izračunati iznos napojnice i ukupni iznos za platiti, oba formatirana na dvije decimale.
'''
# Početak koda
iznos_racuna = float(input("Unesite iznos računa: "))
postotak_napojnice = float(input("Unesite postotak napojnice (npr. 10 za 10%): "))
# Dovršite kod...

#Rješenje
iznos_napojnice = iznos_racuna * (postotak_napojnice / 100)
iznos_racuna_sa_napojnicom = iznos_racuna + iznos_napojnice


print('Iznos napojnice: {:.2f} kn'.format(iznos_napojnice))
print('Ukupni iznos za platiti {:.2f}'.format(iznos_racuna_sa_napojnicom))




''' Zadatak 3: Konverter valuta

Napišite program koji traži od korisnika da unese iznos u eurima, 
a zatim ispiše taj iznos pretvoren u kune (tečaj: 1 EUR = 7.53450 HRK) i dolare (tečaj: 1 EUR = 1.09 USD), 
oba formatirana na dvije decimale.
'''

# Početak koda
iznos_eur = float(input("Unesite iznos u eurima: "))
# Dovršite kod...


#Rješenje

tecaj_eur_hrk = 7.53450
tecaj_eur_usd = 1.09

iznos_hrk = iznos_eur * tecaj_eur_hrk
iznos_usd = iznos_eur * tecaj_eur_usd

print("{:.2f} EUR = {:.2f} HRK".format(iznos_eur, iznos_hrk))
print("{:.2f} EUR = {:.2f} USD".format(iznos_eur, iznos_usd))







''' Zadatak 4: Izračun mjesečne rate kredita

Napišite program koji traži od korisnika da unese iznos kredita, godišnju kamatnu stopu i broj godina otplate. 
Program treba izračunati mjesečnu ratu kredita formatiranu na dvije decimale.'''

# Početak koda
iznos_kredita = float(input("Unesite iznos kredita: "))
godisnja_kamata = float(input("Unesite godišnju kamatnu stopu (npr. 5 za 5%): "))
godine_otplate = int(input("Unesite broj godina otplate: "))
# Dovršite kod...
# Formula za mjesečnu ratu: 
# rata = (iznos_kredita * mjesecna_kamata) / (1 - (1 + mjesecna_kamata)**(-ukupni_broj_mjeseci))


# RJEŠENJE
iznos_kredita = float(input("Unesite iznos kredita: "))
godisnja_kamata = float(input("Unesite godišnju kamatnu stopu (npr. 5 za 5%): "))
godine_otplate = int(input("Unesite broj godina otplate: "))

mjesecna_kamata = godisnja_kamata / 12 / 100
ukupni_broj_mjeseci = godine_otplate * 12

mjesecna_rata = (iznos_kredita * mjesecna_kamata) / (1 - (1 + mjesecna_kamata)**(-ukupni_broj_mjeseci))

print("Mjesečna rata kredita: {:.2f}".format(mjesecna_rata))