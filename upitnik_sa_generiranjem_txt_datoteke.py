# Ovaj program prikuplja i upravlja informacijama o klijentima putem sučelja naredbenog retka

# Definiramo klasu Client za organizaciju i pohranu informacija o klijentu
# Klase nam pomažu grupirati povezane podatke i funkcionalnosti
class Client:
    # Metoda __init__ je posebna metoda koja se poziva pri stvaranju novog Client objekta
    # Ona inicijalizira objekt s pruženim vrijednostima
    def __init__(self, name, phone, email, business_type, additional_info=None):
        # Ovo su varijable instance koje pohranjuju informacije o klijentu
        # self se odnosi na specifičnu instancu Client-a koja se stvara
        self.name = name                    # Pohrani ime klijenta
        self.phone = phone                  # Pohrani telefonski broj klijenta
        self.email = email                  # Pohrani e-mail klijenta
        self.business_type = business_type  # Pohrani vrstu poslovanja klijenta
        # Ako nije pružen additional_info, inicijaliziraj ga kao prazan rječnik
        self.additional_info = additional_info or {}
    
    # Metoda __str__ se poziva kada ispišete Client objekt
    # Vraća string reprezentaciju informacija o klijentu
    def __str__(self):
        # Stvori formatirani string s osnovnim informacijama o klijentu
        info_str = f"""
Informacije o klijentu:
----------------------
Ime: {self.name}
Telefon: {self.phone}
Email: {self.email}
Vrsta poslovanja: {self.business_type}
"""
        # Ako postoje dodatne informacije, dodaj ih u string
        if self.additional_info:
            info_str += "Dodatne informacije:\n"
            # Prođi kroz svaki par ključ-vrijednost u additional_info rječniku
            for key, value in self.additional_info.items():
                # Dodaj svaki dio dodatnih informacija u string
                info_str += f"{key}: {value}\n"
        
        # Vrati kompletan formatirani string
        return info_str

# Ova funkcija provjerava je li e-mail adresa valjana
# Izvodi jednostavnu validaciju provjerom znakova @ i .
def validate_email(email):
    """Jednostavna validacija e-maila"""
    # E-mail mora sadržavati @ i imati barem jednu . u dijelu domene
    # email.split("@")[1] dohvaća dio nakon @ simbola
    return "@" in email and "." in email.split("@")[1]

# Ova funkcija provjerava je li telefonski broj valjan
# Osigurava da telefonski broj sadrži samo dopuštene znakove
def validate_phone(phone):
    """Jednostavna validacija telefona - provjerava sadrži li samo brojeve, razmake i neke posebne znakove"""
    # Definiraj koji su znakovi dopušteni u telefonskom broju
    valid_chars = set("0123456789+()- ")
    # Provjeri jesu li svi znakovi u telefonskom broju u skupu valid_chars
    # Također provjeri je li telefonski broj (bez razmaka) dugačak najmanje 7 znakova
    return all(char in valid_chars for char in phone) and len(phone.strip()) >= 7

# Ova funkcija dohvaća unos od korisnika i validira ga ako je potrebno
def get_valid_input(prompt, validator=None, error_message=None):
    """Dohvati korisnički unos s validacijom"""
    # Nastavi tražiti unos dok se ne pruži valjani unos
    while True:
        # Dohvati unos od korisnika s danim upitom
        user_input = input(prompt)
        # Ako nije pružen validator ili unos prolazi validaciju
        if not validator or validator(user_input):
            # Vrati valjani unos
            return user_input
        # Ako validacija ne uspije, prikaži poruku o pogrešci i pitaj ponovno
        print(error_message or "Nevažeći unos. Molimo pokušajte ponovno.")

# Ovo je glavna funkcija koja prikuplja sve informacije o klijentu
def collect_client_info():
    # Prikaži zaglavlje programa
    print("=== Sustav za prikupljanje informacija o klijentu ===")
    
    # Prikupi osnovne informacije o klijentu
    # Za svaki dio informacija, pozivamo get_valid_input s odgovarajućim parametrima
    
    # Dohvati ime klijenta (validacija nije potrebna)
    name = get_valid_input("Unesite ime klijenta: ")
    
    # Dohvati telefonski broj klijenta s validacijom
    phone = get_valid_input(
        "Unesite telefonski broj klijenta: ",  # Upit za prikaz
        validate_phone,                        # Funkcija za validaciju unosa
        "Nevažeći telefonski broj. Molimo koristite brojke, razmake i znakove poput +()-"  # Poruka o pogrešci
    )
    
    # Dohvati e-mail klijenta s validacijom
    email = get_valid_input(
        "Unesite e-mail klijenta: ", 
        validate_email, 
        "Nevažeći format e-maila. Molimo unesite valjanu e-mail adresu."
    )
    
    # Dohvati vrstu poslovanja klijenta (validacija nije potrebna)
    business_type = get_valid_input("Unesite vrstu poslovanja: ")
    
    # Stvori rječnik za pohranu dodatnih informacija
    additional_info = {}
    
    # Prikaži upute za dodatne informacije
    print("\nDodatne informacije (opcionalno)")
    print("Unesite prazan odgovor za preskakanje bilo kojeg polja")
    
    # Definiraj popis dodatnih polja za prikupljanje
    fields = [
        "Veličina tvrtke (broj zaposlenika)",
        "Godine poslovanja",
        "Web stranica",
        "Primarni proizvodi/usluge",
        "Ciljano tržište"
    ]
    
    # Prođi kroz svako polje i prikupi informacije
    for field in fields:
        # Dohvati unos za trenutno polje
        value = input(f"Unesite {field}: ")
        # Ako je korisnik unio nešto (ne samo razmake)
        if value.strip():
            # Dodaj polje i vrijednost u additional_info rječnik
            additional_info[field] = value
    
    # Omogući korisniku dodavanje prilagođenih polja
    while True:
        # Pitaj za naziv prilagođenog polja
        custom_field = input("\nDodati prilagođeno polje? (Unesite naziv polja ili ostavite prazno za završetak): ")
        # Ako korisnik nije ništa unio, izađi iz petlje
        if not custom_field.strip():
            break
        # Dohvati vrijednost za prilagođeno polje
        value = input(f"Unesite {custom_field}: ")
        # Dodaj prilagođeno polje i vrijednost u additional_info rječnik
        additional_info[custom_field] = value
    
    # Stvori novi Client objekt sa svim prikupljenim informacijama
    client = Client(name, phone, email, business_type, additional_info)
    
    # Prikaži prikupljene informacije ispisivanjem client objekta
    # Ovo poziva __str__ metodu klase Client
    print("\n" + str(client))
    
    # Pitaj želi li korisnik spremiti informacije
    save = input("Želite li spremiti ove informacije? (d/n): ").lower()
    # Ako korisnik unese 'd', spremi informacije u datoteku
    if save == 'd':
        # Stvori naziv datoteke na temelju imena klijenta
        # Zamijeni razmake s donjim crtama i pretvori u mala slova
        filename = f"{name.replace(' ', '_').lower()}_info.txt"
        # Otvori datoteku u načinu pisanja
        # 'with' izjava osigurava da se datoteka pravilno zatvori nakon pisanja
        with open(filename, 'w') as f:
            # Zapiši string reprezentaciju klijenta u datoteku
            f.write(str(client))
        # Obavijesti korisnika da su informacije spremljene
        print(f"Informacije spremljene u {filename}")

# Ovo je ulazna točka programa
# __name__ je posebna varijabla koja je postavljena na "__main__" kada se skripta izravno pokreće
if __name__ == "__main__":
    # Pozovi funkciju za prikupljanje informacija o klijentu
    collect_client_info()
    # Prikaži poruku zahvale kada program završi
    print("Hvala što koristite Sustav za prikupljanje informacija o klijentu!")
