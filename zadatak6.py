## Zadatak 6: Izračun prosječne brzine

'''
Napišite program koji traži od korisnika da unese prijeđenu udaljenost u kilometrima i vrijeme putovanja u minutama. Program treba izračunati i ispisati prosječnu brzinu u kilometrima na sat.
'''

udaljenost = float(input('Upišite udaljenost u likometrima : '))
minute = float(input('Vrijeme putovanja u minutama : '))

sat = minute / 60
brzina = udaljenost / sat
print(f'Prosječna brzina: {brzina:.2f} km/h')
