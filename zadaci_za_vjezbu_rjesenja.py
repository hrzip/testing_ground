## Zadatak 1: Kalkulator potrošnje goriva

'''Napišite program koji traži od korisnika da unese prijeđene kilometre i potrošeno gorivo u litrama. 
Program treba izračunati i ispisati potrošnju goriva u litrama na 100 km, formatiranu na jednu decimalu.
'''
#RJEŠENJE

prijedeni_kilometri = int(input('prijeđeni kilometri : '))
potroseno_gorivo = int(input('potrošeno gorivo u litrama : '))

potrosnja_goriva_na_100_km = potroseno_gorivo / prijedeni_kilometri * 100

print('Potrošnja goriva u litrama na 100km : {:.1f}'.format(potrosnja_goriva_na_100_km))







## Zadatak 2: Pretvarač vremena
'''
Napišite program koji traži od korisnika da unese vrijeme u sekundama. 
Program treba pretvoriti to vrijeme u sate, minute i sekunde te ispisati rezultat u formatu "h:mm:ss".'''

vrijeme_u_sekundama = int(input('Upišite vrijeme u sekundama: '))

sati = vrijeme_u_sekundama // 3600
preostale_sekunde = vrijeme_u_sekundama % 3600
minute = preostale_sekunde // 60
sekunde = preostale_sekunde % 60

print('{}:{:02d}:{:02d}'.format(sati, minute, sekunde))

#Ovdje je korišten 2d, a ne float da se ne prikazuju decimale u sekundama na primjer, ali da se vide prva dva cijela broja što nam i treba
