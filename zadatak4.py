## Zadatak 4: Kalkulator uštede
'''
Napišite program koji traži od korisnika da unese mjesečni iznos koji planira štedjeti, godišnju kamatnu stopu i broj godina štednje. 
Program treba izračunati i ispisati ukupni ušteđeni iznos nakon zadanog razdoblja, uzimajući u obzir složenu kamatu koja se obračunava mjesečno.
'''

mjesecni_iznos = float(input('Mjesečni iznos: '))
kamata = float(input('Godišnja kamatna stopa: '))
broj_godina = int(input('Broj godina: '))

mjesecna_kamatna_stopa = kamata / 100 / 12

ukupno_mjeseci = broj_godina * 12

ukupni_iznos = mjesecni_iznos * ((1 + mjesecna_kamatna_stopa)**ukupno_mjeseci - 1) / mjesecna_kamatna_stopa * (1 + mjesecna_kamatna_stopa)

print(f'Ukupni ušteđeni iznos: {ukupni_iznos:.2f}')