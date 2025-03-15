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