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





## Zadatak 3: Izračun indeksa tjelesne mase (BMI)
'''
Napišite program koji traži od korisnika da unese svoju težinu u kilogramima i visinu u metrima. 
Program treba izračunati indeks tjelesne mase (BMI = težina / visina²) i ispisati rezultat formatiran na jednu decimalu, 
zajedno s kategorizacijom (pothranjenost < 18.5, normalna težina 18.5-24.9, prekomjerna težina 25-29.9, pretilost ≥ 30).'''

tezina = float(input('Unesite težinu u kilogramima: '))
visina = float(input('Unesite visinu u metrima: '))


bmi = tezina / (visina ** 2)

if bmi < 18.5:
    kategorija = "pothranjenost"
elif bmi < 25:
    kategorija = "normalna težina"
elif bmi < 30:
    kategorija = "prekomjerna težina"
else:
    kategorija = "pretilost"

print(f'Vaš BMI je {bmi:.1f}, što spada u kategoriju: {kategorija}')