# BIPL Toets Oefening

Een desktop-oefenprogramma voor de theorie van het **BIPL**-vak (Netwerken & Platformen, weken 1–4). Gebouwd met Python en Tkinter — geen externe packages nodig.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey)
![Vragen](https://img.shields.io/badge/Vragen-235-green)
![Licentie](https://img.shields.io/badge/Licentie-MIT-yellow)

---

## Functies

- **235 vragen** over alle stof van weken 1 t/m 4
- **20 willekeurige vragen** per sessie uit de vragenbank
- Antwoordopties worden **elke keer opnieuw geschud** — geen vaste posities onthouden
- **Directe feedback** — juist antwoord groen, fout antwoord rood met het correcte antwoord zichtbaar
- **Scoreoverzicht** aan het einde met alle fout beantwoorde vragen en de correcte antwoorden
- Meteen **opnieuw spelen** of terug naar het hoofdmenu

---

## Onderwerpen

| Onderwerp | Vragen |
|---|---|
| Netwerken – Week 1 (OSI-model, Cisco IOS, CLI, LAN/WAN) | 37 |
| Netwerken – Week 2 (IPv4, subnetting, VLSM, binair rekenen) | 24 |
| Netwerken – Week 3 (Ethernet, ARP, switching, kabels) | 26 |
| Platformen – Week 1 (Windows Server, Linux-distributies, LVM) | 23 |
| Platformen – Week 2 (Linux-shell, redirection, Server Core) | 27 |
| Platformen – Week 3 (Active Directory, gebruikers, CSVDE) | 31 |
| Platformen – Week 3 Linux (gebruikersbeheer, sudo, /etc/shadow) | 18 |
| Platformen – Week 4 (NTFS-permissies, ReFS, shares) | 17 |
| Platformen – Week 4 Linux (bestandssystemen, LVM, chmod) | 32 |
| **Totaal** | **235** |

---

## Vereisten

- Python 3.x
- Tkinter (standaard meegeleverd met Python)

Geen `pip install` nodig.

> **Alleen Linux:** Als Tkinter ontbreekt, installeer het met:
> ```bash
> sudo apt install python3-tk        # Debian / Ubuntu
> sudo dnf install python3-tkinter   # Rocky Linux / RHEL / Fedora
> ```

---

## Gebruik

```bash
python3 bipl_quiz.py
```

---

## Hoe de vragen werken

Elke vraag staat als een tuple in de lijst `ALL_QUESTIONS` bovenaan het bestand:

```python
("Vraagtekst",
 ["Optie A", "Optie B", "Optie C", "Optie D"],
 2,                       # index van het juiste antwoord (0 = eerste optie)
 "Netwerken – Week 1")    # onderwerplabel
```

De correcte index verwijst naar de **originele, ongeschudde optielijst**. Bij het starten wordt de volgorde willekeurig geschud en bepaalt de code daarna welke geschudde positie het opgeslagen antwoord heeft gekregen.

---

## Vragen toevoegen

Open `bipl_quiz.py` en voeg een nieuwe tuple toe aan `ALL_QUESTIONS`:

```python
("Welk commando toont de routing-tabel op Cisco IOS?",
 ["show interfaces", "show ip route", "show arp", "show version"],
 1,
 "Netwerken – Week 1"),
```

Regels:
- De correcte index moet verwijzen naar het juiste antwoord in **jouw optielijst** (0 = eerste optie)
- Gebruik een bestaand onderwerplabel zodat de groepering klopt
- Herstart het programma — wijzigingen zijn direct van kracht

---

## Projectstructuur

```
bipl_quiz.py   # Alles in één bestand: vragenbank + GUI, geen externe afhankelijkheden
README.md
```
