## Zadatak 1: Kalkulator potrošnje goriva

'''Napišite program koji traži od korisnika da unese prijeđene kilometre i potrošeno gorivo u litrama. 
Program treba izračunati i ispisati potrošnju goriva u litrama na 100 km, formatiranu na jednu decimalu.
'''
#RJEŠENJE

prijedeni_kilometri = int(input('prijeđeni kilometri : '))
potroseno_gorivo = int(input('potrošeno gorivo u litrama : '))

potrosnja_goriva_na_100_km = potroseno_gorivo / prijedeni_kilometri * 100

print('Potrošnja goriva u litrama na 100km : {:.1f}'.format(potrosnja_goriva_na_100_km))