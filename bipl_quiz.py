import tkinter as tk
from tkinter import ttk, messagebox
import random

# ─────────────────────────────────────────────
# QUESTION BANK  (question, [options], correct_index)
# correct_index is 0-based index into options list
# ─────────────────────────────────────────────
ALL_QUESTIONS = [

    # ══════════════════ WEEK 1 – Netwerken ══════════════════
    ("Welke van de volgende is een voorbeeld van een End-Device (eindapparaat) in een netwerk?",
     ["Router", "Switch", "PC / Laptop", "Access Point"], 2, "Netwerken – Week 1"),

    ("Wat slaat Cisco IOS op in het Flash-geheugen?",
     ["De running-configuratie", "De startup-configuratie", "De IOS-software zelf", "Het werkgeheugen (RAM)"], 2, "Netwerken – Week 1"),

    ("Waar wordt de running-config opgeslagen op een Cisco-apparaat?",
     ["Flash", "NVRAM", "RAM", "ROM"], 2, "Netwerken – Week 1"),

    ("Waar wordt de startup-config opgeslagen op een Cisco-apparaat?",
     ["RAM", "Flash", "ROM", "NVRAM"], 3, "Netwerken – Week 1"),

    ("Wat is het verschil tussen een fysieke topologietekening en een logische topologietekening?",
     ["Fysiek toont IP-adressen; logisch toont kabels",
      "Fysiek toont locaties en kabels (L1/L2); logisch toont adressen en poorten (L3+)",
      "Ze zijn identiek",
      "Logisch toont alleen draadloze verbindingen"], 1, "Netwerken – Week 1"),

    ("Wat is een LAN?",
     ["Een netwerk dat continenten verbindt",
      "Een netwerk over een klein geografisch gebied",
      "Een draadloos netwerk buiten een gebouw",
      "Een verbinding tussen twee providers"], 1, "Netwerken – Week 1"),

    ("Welk Cisco IOS-commando versleutelt alle wachtwoorden in de configuratie?",
     ["enable secret", "password encryption", "service password-encryption", "encrypt all"], 2, "Netwerken – Week 1"),

    ("Welk commando gebruik je om de interface-status op een Cisco-apparaat snel te controleren?",
     ["show version", "show ip interface brief", "show running-config", "ipconfig"], 1, "Netwerken – Week 1"),

    ("Wat doet het commando 'ping' in een netwerk?",
     ["Het zoekt MAC-adressen op",
      "Het test de end-to-end verbinding door ICMP-pakketten te sturen",
      "Het configureert een IP-adres",
      "Het herstart een interface"], 1, "Netwerken – Week 1"),

    ("Welke laag van het OSI-model is verantwoordelijk voor het routeren van pakketten?",
     ["Laag 1 – Fysiek", "Laag 2 – Datalink", "Laag 3 – Netwerk", "Laag 4 – Transport"], 2, "Netwerken – Week 1"),

    ("Wat is een Switched Virtual Interface (SVI) op een switch?",
     ["Een fysieke uplink-poort",
      "Een virtuele interface die een IP-adres draagt voor remote beheer",
      "Een VLAN-trunk",
      "Een loopback naar de router"], 1, "Netwerken – Week 1"),

    # ══════════════════ WEEK 1 – Platformen ══════════════════
    ("Welke Windows Server-installatie heeft een volledige grafische interface (GUI)?",
     ["Nano Server", "Server Core", "Desktop Experience", "Hyper-V Server"], 2, "Platformen – Week 1"),

    ("Welke bewering is JUIST over Windows Server Core?",
     ["Server Core is een speciaal OS",
      "Server Core is een minimale installatie-optie van Windows Server 2008 of later",
      "Server Core is alleen te installeren op ARM",
      "Server Core heeft een volledig grafische interface"], 1, "Platformen – Week 1"),

    ("Wat is een Linux-distributie?",
     ["Alleen de Linux-kernel",
      "De Linux-kernel gecombineerd met andere software tot een compleet OS",
      "Een versie van Windows voor servers",
      "Een type hypervisor"], 1, "Platformen – Week 1"),

    ("Welke distributie is een zakelijke variant afgeleid van Red Hat Enterprise Linux (RHEL)?",
     ["Ubuntu", "Fedora", "Rocky Linux", "openSUSE"], 2, "Platformen – Week 1"),

    ("Wat is een voordeel van Server Core ten opzichte van de Desktop Experience?",
     ["Betere grafische ondersteuning",
      "Kleiner aanvalsoppervlak (reduced attack surface)",
      "Hogere RAM-vereisten",
      "Betere gaming-prestaties"], 1, "Platformen – Week 1"),

    ("Welke twee commando's herstart een Windows Server Core-systeem? (kies het meest complete antwoord)",
     ["restart-computer en reboot",
      "restart-computer en shutdown -r -t 0",
      "shutdown --now en reboot",
      "poweroff en shutdown /r"], 1, "Platformen – Week 1"),

    ("Welk menu-gestuurd commando helpt bij de basisconfiguratie van Server Core?",
     ["mmc", "mms", "sconfig", "script"], 2, "Platformen – Week 1"),

    ("Wat is het doel van Sysprep bij virtuele machines?",
     ["Het verwijderen van alle gebruikersdata",
      "Het standaardiseren van een VM-image zodat klonen unieke identiteiten krijgen",
      "Het vergroten van de RAM-toewijzing",
      "Het installeren van drivers"], 1, "Platformen – Week 1"),

    # ══════════════════ WEEK 2 – Netwerken (IPv4 / Subnetting) ══════════════════
    ("Hoeveel bits heeft een IPv4-adres?",
     ["8", "16", "32", "64"], 2, "Netwerken – Week 2"),

    ("Wat is het netwerkadres van 192.168.10.10 /24?",
     ["192.168.10.1", "192.168.10.0", "192.168.10.255", "192.168.0.0"], 1, "Netwerken – Week 2"),

    ("Wat is het broadcast-adres van het netwerk 192.168.10.0 /24?",
     ["192.168.10.0", "192.168.10.1", "192.168.10.254", "192.168.10.255"], 3, "Netwerken – Week 2"),

    ("Welke privé-adressen horen bij het 10.0.0.0/8-blok?",
     ["10.0.0.0 – 10.0.255.255", "10.0.0.0 – 10.255.255.255",
      "10.0.0.0 – 10.0.0.255", "10.0.0.0 – 10.10.255.255"], 1, "Netwerken – Week 2"),

    ("Wat is het subnetmasker bij een /26 prefix?",
     ["255.255.255.0", "255.255.255.128", "255.255.255.192", "255.255.255.224"], 2, "Netwerken – Week 2"),

    ("Hoeveel bruikbare hostadressen heeft een /26-subnet?",
     ["30", "62", "126", "254"], 1, "Netwerken – Week 2"),

    ("Wat betekent VLSM?",
     ["Virtual LAN Subnet Method",
      "Variable Length Subnet Mask",
      "Very Large Switch Module",
      "Virtual Link Subnet Management"], 1, "Netwerken – Week 2"),

    ("Wat is de eerste stap bij het ontwerpen met VLSM?",
     ["Bepaal het subnetmasker",
      "Sorteer de subnetten van groot naar klein",
      "Wijs IP-adressen toe aan hosts",
      "Kies het standaard-gateway-adres"], 1, "Netwerken – Week 2"),

    ("Welk speciaal IPv4-adres wordt gebruikt voor loopback-tests?",
     ["192.168.0.1", "172.16.0.1", "127.0.0.1", "169.254.0.1"], 2, "Netwerken – Week 2"),

    ("Wat is het link-local adresblok (APIPA)?",
     ["127.0.0.0/8", "192.168.0.0/16", "169.254.0.0/16", "10.0.0.0/8"], 2, "Netwerken – Week 2"),

    # ══════════════════ WEEK 2 – Platformen (Shell / Server Core) ══════════════════
    ("Wat doet de standaard output-redirection operator '>' in Linux?",
     ["Verwijst de uitvoer naar een ander programma (pipe)",
      "Stuurt de uitvoer naar een bestand en overschrijft dit",
      "Leest invoer vanuit een bestand",
      "Verwijdert het bestand"], 1, "Platformen – Week 2"),

    ("Welk Linux-commando navigeert naar de home-directory van de huidige gebruiker?",
     ["cd /", "cd ..", "cd ~", "cd /home"], 2, "Platformen – Week 2"),

    ("Wat doet het commando 'grep error /var/log/messages'?",
     ["Verwijdert regels met 'error' uit het bestand",
      "Toont alle regels in het bestand waar 'error' in voorkomt",
      "Kopieert het bestand naar /error",
      "Start de error-log service"], 1, "Platformen – Week 2"),

    ("Welk commando maakt een lege directory aan in Linux?",
     ["touch", "mkdir", "mkfile", "newdir"], 1, "Platformen – Week 2"),

    ("Welk commando verwijdert een directory inclusief alle subdirectories in Linux?",
     ["rmdir", "rm -r", "del -r", "remove -all"], 1, "Platformen – Week 2"),

    ("Wat is het verschil tussen de shells 'bash' en 'sh'?",
     ["Bash is alleen voor root; sh is voor gewone gebruikers",
      "Bash (Bourne Again Shell) is een uitgebreidere versie van de originele Bourne Shell (sh)",
      "Sh is uitgebreider dan bash",
      "Ze zijn identiek"], 1, "Platformen – Week 2"),

    # ══════════════════ WEEK 3 – Active Directory ══════════════════
    ("Wat is authenticatie?",
     ["Het toewijzen van rechten aan een gebruiker",
      "Het controleren of iemand is wie hij/zij beweert te zijn",
      "Het versleutelen van wachtwoorden",
      "Het aanmaken van een gebruikersaccount"], 1, "Platformen – Week 3"),

    ("Wat is autorisatie?",
     ["Het verifiëren van een gebruikersidentiteit",
      "Het controleren of een geauthenticeerde gebruiker toegang heeft tot een resource",
      "Het aanmaken van een SID",
      "Het synchroniseren van wachtwoorden"], 1, "Platformen – Week 3"),

    ("Welke Windows Server-rol moet geïnstalleerd zijn voor Active Directory?",
     ["DHCP", "DNS", "AD DS (Active Directory Domain Services)", "IIS"], 2, "Platformen – Week 3"),

    ("Wat wordt er automatisch aangemaakt bij het aanmaken van een gebruikersaccount in een domein?",
     ["MAC-adres", "DHCP-adres", "SID", "Ticket"], 2, "Platformen – Week 3"),

    ("Wat staat er NIET op een Access Token in Windows?",
     ["User SID", "Group SID", "List of privileges", "Computer SID"], 3, "Platformen – Week 3"),

    ("Waarvoor staat de afkorting DACL?",
     ["Domain Access Control List", "Discretionary Access Control List",
      "Dynamic Access Control Layer", "Default Access Control Limit"], 1, "Platformen – Week 3"),

    ("Waarvoor staat de afkorting SACL?",
     ["System Access Control List", "Secure Access Control Layer",
      "Standard Access Control List", "Share Access Control Limit"], 0, "Platformen – Week 3"),

    ("Wat is de functie van een SACL?",
     ["Toegangsrechten beheren voor gebruikers en groepen",
      "Toegangs- en wijzigingspogingen monitoren en auditen",
      "Netwerkverbindingen beveiligen",
      "Bestands- en mapstructuren organiseren"], 1, "Platformen – Week 3"),

    ("Wat is geen geldige objectnaam in Active Directory?",
     ["User Logon name: Henk", "UPN: Ali@bmc.local",
      "Authentication Name", "LDAP Distinguished Name"], 2, "Platformen – Week 3"),

    ("Waar staat CN voor in een LDAP Distinguished Name?",
     ["Client Name", "Common Name", "Cursor Name", "Coupled Name"], 1, "Platformen – Week 3"),

    ("Waar staat DC voor in een LDAP Distinguished Name?",
     ["Domain Controller", "Domain name", "Domain Client", "Domain Component"], 3, "Platformen – Week 3"),

    ("Welke tool importeert gebruikers vanuit een CSV-bestand in Active Directory?",
     ["LDIFDE", "DSMove", "CSVDE", "DSQuery"], 2, "Platformen – Week 3"),

    ("Kan CSVDE wachtwoorden importeren?",
     ["Ja, altijd", "Nee, CSVDE ondersteunt geen wachtwoorden",
      "Ja, maar alleen versleuteld", "Ja, via een beveiligd kanaal"], 1, "Platformen – Week 3"),

    ("Welke optie gebruik je bij CSVDE om door te gaan bij een fout?",
     ["-v", "-b", "-k", "-F"], 2, "Platformen – Week 3"),

    ("Wat kan LDIFDE wat CSVDE NIET kan?",
     ["Gebruikers importeren",
      "Bestaande objecten wijzigen en verwijderen",
      "Wachtwoorden importeren",
      "Verbinding maken met een domein"], 1, "Platformen – Week 3"),

    ("Wat kan DSADD NIET aanmaken?",
     ["Users", "OU's", "Groups", "DHCP-scope"], 3, "Platformen – Week 3"),

    ("Welk commando maakt een OU aan in PowerShell?",
     ["MakeOU studenten", "New-ADOrganizationalUnit studenten",
      "MkOU Studenten", "Create-OU studenten"], 1, "Platformen – Week 3"),

    ("Welk profiel gaat mee ongeacht op welke computer je inlogt?",
     ["Local profile", "Remote profile", "Roaming profile", "Mandatory profile"], 2, "Platformen – Week 3"),

    ("Welk profiel kan een gewone gebruiker NIET zelf aanpassen?",
     ["Local profile", "Remote profile", "Roaming profile", "Mandatory profile"], 3, "Platformen – Week 3"),

    ("Wat is geen Windows-accounttype?",
     ["Domain account", "Local account", "Superuser account", "Builtin account"], 2, "Platformen – Week 3"),

    ("Hoe heet een OU die binnen een andere OU staat?",
     ["Child OU", "Tree OU", "Nested OU", "Parent OU"], 2, "Platformen – Week 3"),

    ("Welke OU wordt automatisch aangemaakt bij het promoveren van een server tot DC?",
     ["Users OU", "Client OU", "Domain Controllers OU", "Everyone OU"], 2, "Platformen – Week 3"),

    # ══════════════════ WEEK 3 – Linux gebruikers & groepen ══════════════════
    ("Welk UID heeft het root-account onder Linux?",
     ["0", "1", "500", "1000"], 0, "Platformen – Week 3 Linux"),

    ("In welk bestand staan de versleutelde wachtwoorden onder Linux?",
     ["/etc/group", "/etc/passwd", "/etc/shadow", "/etc/users"], 2, "Platformen – Week 3 Linux"),

    ("Welk commando wisselt van gebruiker in de Linux-commandline?",
     ["switch", "su", "move", "change"], 1, "Platformen – Week 3 Linux"),

    ("Van welke groep moet je lid zijn om sudo te gebruiken?",
     ["wheel", "sudo", "root", "administrators"], 0, "Platformen – Week 3 Linux"),

    ("Welk commando voegt een gebruiker toe aan een secundaire groep?",
     ["adduser", "useradd", "usermod", "groupadd"], 2, "Platformen – Week 3 Linux"),

    ("Welk commando past het wachtwoord van gebruiker 'henk' aan?",
     ["passwd -u henk", "chpasswd henk", "usermod -p henk", "passwd henk"], 3, "Platformen – Week 3 Linux"),

    ("Welk bestand bevat de sudo-configuratie?",
     ["/etc/passwd", "/etc/sudoers", "/etc/group", "/etc/shadow"], 1, "Platformen – Week 3 Linux"),

    ("Welk commando maakt een nieuwe groep aan in Linux?",
     ["groupadd", "newgroup", "addgroup", "creategroup"], 0, "Platformen – Week 3 Linux"),

    ("Wat is GEEN geldig Linux-gebruikerstype?",
     ["Systeemgebruiker", "Gewone/eindgebruiker", "Root", "Sudo"], 3, "Platformen – Week 3 Linux"),

    ("Welk Linux-commando vraagt de eigenaar van een bestand op?",
     ["LsOwner", "show Owner", "cat owner", "ls -l"], 3, "Platformen – Week 3 Linux"),

    # ══════════════════ WEEK 3 – Netwerken (Ethernet / Switching) ══════════════════
    ("Welke laag van het OSI-model gebruikt MAC-adressen?",
     ["Laag 1", "Laag 2", "Laag 3", "Laag 4"], 1, "Netwerken – Week 3"),

    ("Wat is ARP?",
     ["Een protocol om IP-adressen toe te wijzen",
      "Een protocol om IPv4-adressen te vertalen naar MAC-adressen",
      "Een protocol voor domeinnaambeheer",
      "Een beveiligingsprotocol voor WiFi"], 1, "Netwerken – Week 3"),

    ("Wat is de maximale lengte van een UTP-kabel-segment?",
     ["50 m", "100 m", "150 m", "200 m"], 1, "Netwerken – Week 3"),

    ("Welk type UTP-kabel verbindt twee gelijkwaardige apparaten (bijv. switch–switch)?",
     ["Straight-through", "Crossover", "Rollover", "Coaxiaal"], 1, "Netwerken – Week 3"),

    ("Wat is full-duplex communicatie?",
     ["Slechts één kant kan tegelijk zenden",
      "Beide kanten kunnen gelijktijdig zenden en ontvangen",
      "Alleen ontvangen is mogelijk",
      "Communicatie via satelliet"], 1, "Netwerken – Week 3"),

    ("Hoe geeft een switch op welke poort een MAC-adres bereikbaar is?",
     ["Via een routing-table",
      "Via een MAC-adrestabel (CAM-table)",
      "Via ARP-cache",
      "Via de NVRAM"], 1, "Netwerken – Week 3"),

    ("Wat doet CSMA/CD?",
     ["Voorkomt botsingen door te wachten voor het zenden (WiFi)",
      "Detecteert botsingen op een gedeeld medium en herzendt daarna",
      "Versleutelt data op laag 2",
      "Wijst MAC-adressen toe"], 1, "Netwerken – Week 3"),

    # ══════════════════ WEEK 4 – NTFS-permissies ══════════════════
    ("Welke NTFS-permissie is de meest uitgebreide?",
     ["Modify", "Read & Execute", "Full Control", "Write"], 2, "Platformen – Week 4"),

    ("Welke NTFS-permissie geldt ALLEEN voor een map, NIET voor een bestand?",
     ["Full Control", "Modify", "Read & Execute", "List Folder Contents"], 3, "Platformen – Week 4"),

    ("Wat is geen kenmerk bij NTFS-permissies?",
     ["Inherit", "Explicit", "Cumulatief", "Reverse"], 3, "Platformen – Week 4"),

    ("Wat zijn NTFS geërfde (inherited) permissies?",
     ["Permissies die automatisch worden toegepast op alle gebruikers in een domein",
      "Permissies die worden overgenomen van de bovenliggende map",
      "Permissies die alleen gelden voor specifieke gebruikers",
      "Permissies die zijn ingesteld door de systeembeheerder en niet gewijzigd kunnen worden"], 1, "Platformen – Week 4"),

    ("Wint een Deny ALTIJD van een Allow bij NTFS-permissies?",
     ["Ja, altijd zonder uitzondering",
      "Nee, een explicit allow heeft voorrang op een inherited deny",
      "Ja, tenzij de gebruiker domeinadmin is",
      "Nee, het hangt af van de volgorde"], 1, "Platformen – Week 4"),

    ("Welke permissies zijn cumulatief (optelbaar) in Windows?",
     ["Alleen share-permissies",
      "Alleen NTFS-permissies",
      "Zowel share- als NTFS-permissies",
      "Alleen OS-permissies"], 2, "Platformen – Week 4"),

    ("Wat is de standaard share-permissie voor de groep 'Everyone'?",
     ["Full Control", "All", "Read", "Read & Write"], 2, "Platformen – Week 4"),

    ("Als share-permissie 'Read' is maar NTFS 'Full Control', wat mag de gebruiker?",
     ["Bestanden lezen, maar niet wijzigen of verwijderen",
      "Alles: lezen, wijzigen, verwijderen en aanmaken",
      "Niets, want share-permissie is beperkend",
      "Alleen bestandsnamen zien"], 0, "Platformen – Week 4"),

    ("Waarvoor staat UNC?",
     ["Unique Network Connection", "Unified Network Communication",
      "Uniform Network Control", "Universal Naming Convention"], 3, "Platformen – Week 4"),

    ("Wat is de juiste UNC-syntaxis?",
     ["\\server\\share\\file", "//server/share/file",
      "server.share.file", "\\\\server\\share"], 3, "Platformen – Week 4"),

    ("Wat is het nieuwste Windows-bestandssysteem?",
     ["NTFSv3", "Share64", "ReFS", "FAT64"], 2, "Platformen – Week 4"),

    ("Wat is een beperking van ReFS?",
     ["Je kunt geen share-permissies gebruiken",
      "Je kunt er niet van booten",
      "Je kunt er geen Linux VM's op zetten",
      "Je kunt de disk niet indelen in partities"], 1, "Platformen – Week 4"),

    ("Wat is een journaling filesystem?",
     ["Een bestandssysteem dat dagboekbestanden bijhoudt",
      "Een bestandssysteem dat logboeken genereert van uitgevoerde taken",
      "Een bestandssysteem dat een journaal gebruikt om onvoltooide wijzigingen bij te houden",
      "Een bestandssysteem voor journalisten"], 2, "Platformen – Week 4"),

    ("Welk bestandssysteem heeft GEEN journaling-mogelijkheid?",
     ["ext2", "xfs", "ext3", "ext4"], 0, "Platformen – Week 4"),

    # ══════════════════ WEEK 4 – Linux bestandssysteem & permissies ══════════════════
    ("Wat betekenen de klasieke rechten u, g, o onder Linux?",
     ["Ze geven aan voor welk bestand de permissies gelden",
      "Ze geven aan voor wie de rechten gelden: user, group, other",
      "UGO staat voor Users Get Ownership",
      "U=Read, G=Write, O=Ownership"], 1, "Platformen – Week 4 Linux"),

    ("Welke tool pas je het meest aan om Linux-permissies te wijzigen?",
     ["chmod", "chown", "grep", "ls"], 0, "Platformen – Week 4 Linux"),

    ("Wat vertegenwoordigt de permissie '640' in Linux?",
     ["Owner lees en schrijfrechten, groep leesrechten, others niets",
      "Owner alles, groep schrijfrechten, others leesrechten",
      "Owner lees en uitvoerrechten, groep schrijfrechten, others niets",
      "Owner alles, groep niets, others leesrechten"], 0, "Platformen – Week 4 Linux"),

    ("Hoeveel bits gebruikt Linux voor permissies (permission bits)?",
     ["Acht bits (000–777)", "Negen bits (000–777)",
      "Tien bits (0000–7777)", "Zeven bits (000–777)"], 1, "Platformen – Week 4 Linux"),

    ("Wat is het startpunt van het Linux-bestandssysteem?",
     ["/", "~", "/root", "/home"], 0, "Platformen – Week 4 Linux"),

    ("Wat is het verschil tussen een absoluut pad en een relatief pad?",
     ["Absoluut begint bij home (~); relatief bij root (/)",
      "Absoluut begint bij root (/); relatief begint bij de huidige directory",
      "Ze zijn hetzelfde",
      "Absoluut bevat geen slash (/)"], 1, "Platformen – Week 4 Linux"),

    ("Welk commando vraagt de huidige directory op in Linux?",
     ["ls", "dir", "cd", "pwd"], 3, "Platformen – Week 4 Linux"),

    ("Welk commando koppelt een disk of partitie aan het OS in Linux?",
     ["attach", "connect", "mount", "link"], 2, "Platformen – Week 4 Linux"),

    ("In welk bestand worden gekoppelde partities (mounts) opgeslagen?",
     ["/etc/mounts", "/etc/mounttable", "/etc/fstab", "/etc/partitions"], 2, "Platformen – Week 4 Linux"),

    ("Welke twee typen partitietabellen kom je tegen op een harde schijf?",
     ["FAT en NTFS", "Primary en Extended", "MBR en GPT", "Swap en Root"], 2, "Platformen – Week 4 Linux"),

    ("Wat is een voordeel van Logical Volume Management (LVM)?",
     ["Betere beveiliging tegen virussen",
      "Hogere rekenprestaties",
      "LV's groter of kleiner maken zonder dataverlies (on the fly)",
      "Verhoogde netwerkstabiliteit"], 2, "Platformen – Week 4 Linux"),

    ("Welk commando maakt een nieuw logical volume aan in LVM?",
     ["lvcreate", "pvcreate", "vgcreate", "lvextend"], 0, "Platformen – Week 4 Linux"),

    ("Welk commando toont de physical volumes in LVM?",
     ["pvview", "vgdisplay", "pvdisplay", "lvdisplay"], 2, "Platformen – Week 4 Linux"),

    ("Kun je na het partitioneren direct bestanden schrijven op een harde schijf?",
     ["Ja, zodra partities zijn aangemaakt",
      "Nee, je moet eerst een bestandssysteem aanmaken (mkfs)",
      "Ja, maar alleen na defragmentatie",
      "Ja, als de partitie NTFS of FAT32 is"], 1, "Platformen – Week 4 Linux"),

    ("Welk commando geeft een partitie een bestandssysteem onder Linux?",
     ["fscreate -t <fstype> <device>",
      "formatfs <fstype> <partition>",
      "mkfs -t <fstype> <device>",
      "fssetup <fstype> <partition>"], 2, "Platformen – Week 4 Linux"),

    ("Welk commando controleert en repareert een bestandssysteem in Linux?",
     ["chkdisk", "fsck", "diskutil", "scandisk"], 1, "Platformen – Week 4 Linux"),

    ("Welk veelgebruikt Linux-bestandssysteem is een moderne keuze?",
     ["NTFS", "FAT32", "ext4", "HFS+"], 2, "Platformen – Week 4 Linux"),

    ("Welk commando maakt een hard link in Linux?",
     ["ln", "link", "hardlink", "mklink"], 0, "Platformen – Week 4 Linux"),

    ("Wat voor soort referentie is een symbolische link in Linux?",
     ["Een directe referentie", "Een indirecte referentie",
      "Een absolute referentie", "Een dynamische referentie"], 1, "Platformen – Week 4 Linux"),

    ("Welk commando toont bestandsinformatie inclusief inode-details?",
     ["ls", "cd", "mkdir", "stat"], 3, "Platformen – Week 4 Linux"),

    ("Wat doet het chown-commando?",
     ["Wijzigt het bestandstype",
      "Wijzigt de bestandsnaam",
      "Wijzigt de bestandspermissies",
      "Wijzigt de eigenaar en/of groep van een bestand"], 3, "Platformen – Week 4 Linux"),

    ("Welk commando toont beschikbare schijven en partities?",
     ["lsblock", "df", "du", "fdisk -l of lsblk --fs"], 3, "Platformen – Week 4 Linux"),

    ("In welke directory vind je de device-bestanden van harde schijven?",
     ["/dev/", "/var", "/etc", "/home"], 0, "Platformen – Week 4 Linux"),

    ("Waarvoor wordt de swap-partitie gebruikt?",
     ["Voor logbestanden", "Als virtueel geheugen",
      "Voor tijdelijke bestanden", "Voor gebruikers-homedirectories"], 1, "Platformen – Week 4 Linux"),

    # ══════════════════ EXTRA – Netwerken Week 1 ══════════════════
    ("Hoeveel lagen heeft het OSI-model?",
     ["4", "5", "7", "9"], 2, "Netwerken – Week 1"),

    ("Welke OSI-laag is verantwoordelijk voor het segmenteren en hermonteren van data?",
     ["Laag 2 – Datalink", "Laag 3 – Netwerk", "Laag 4 – Transport", "Laag 5 – Sessie"], 2, "Netwerken – Week 1"),

    ("Welk TCP/IP-model laag komt overeen met OSI-lagen 5, 6 en 7?",
     ["Network Access", "Internet", "Transport", "Application"], 3, "Netwerken – Week 1"),

    ("Wat is de functie van de Presentatielaag (laag 6) in het OSI-model?",
     ["Zorgt voor fysieke verbindingen",
      "Biedt gemeenschappelijke datarepresentatie (codering, compressie, versleuteling)",
      "Beheert sessies tussen apparaten",
      "Routeert pakketten tussen netwerken"], 1, "Netwerken – Week 1"),

    ("Welk Cisco IOS-commando stel je in om een wachtwoord te vereisen bij het inloggen via de console?",
     ["enable secret cisco", "line vty 0 15 → password → login",
      "line console 0 → password → login", "service password-encryption"], 2, "Netwerken – Week 1"),

    ("Wat is het verschil tussen 'enable password' en 'enable secret' in Cisco IOS?",
     ["Ze zijn identiek",
      "Enable secret slaat het wachtwoord op in plaintext; enable password versleutelt het",
      "Enable secret versleutelt het wachtwoord met MD5; enable password slaat het op in plaintext",
      "Enable password werkt alleen op routers"], 2, "Netwerken – Week 1"),

    ("Welke toetsencombinatie breekt een lopende ping of traceroute af in Cisco IOS?",
     ["Ctrl-C", "Ctrl-Z", "Ctrl-Shift-6", "Esc"], 2, "Netwerken – Week 1"),

    ("Wat is de functie van de Tab-toets in de Cisco IOS CLI?",
     ["Gaat terug naar privileged EXEC mode",
      "Vult een gedeeltelijk ingevoerd commando aan",
      "Toont alle beschikbare commando's",
      "Slaat de configuratie op"], 1, "Netwerken – Week 1"),

    ("Hoe sla je de running-config op als startup-config in Cisco IOS?",
     ["save running-config", "copy startup-config running-config",
      "copy running-config startup-config", "write startup"], 2, "Netwerken – Week 1"),

    ("Wat is een unicast-bericht?",
     ["Een bericht naar alle hosts op het netwerk",
      "Een bericht naar een specifieke groep hosts",
      "Een bericht van één afzender naar één specifieke ontvanger",
      "Een bericht dat automatisch wordt doorgestuurd"], 2, "Netwerken – Week 1"),

    ("Wat is een broadcast-bericht?",
     ["Een bericht van één afzender naar één ontvanger",
      "Een bericht naar alle hosts in het netwerk",
      "Een bericht naar een geselecteerde groep",
      "Een versleuteld bericht"], 1, "Netwerken – Week 1"),

    ("Welke laag van het OSI-model beheert de fysieke verbinding (kabels, spanning)?",
     ["Laag 2 – Datalink", "Laag 1 – Fysiek", "Laag 3 – Netwerk", "Laag 4 – Transport"], 1, "Netwerken – Week 1"),

    ("Wat is de maximale grootte van een Ethernet-frame (payload)?",
     ["512 bytes", "1024 bytes", "1500 bytes", "9000 bytes"], 2, "Netwerken – Week 1"),

    ("Welk commando toon je de MAC-adrestabel van een Cisco-switch?",
     ["show ip arp", "show mac address-table", "show vlan brief", "show interfaces"], 1, "Netwerken – Week 1"),

    # ══════════════════ EXTRA – Netwerken Week 2 ══════════════════
    ("Wat is de decimale waarde van het binaire getal 11001000?",
     ["192", "200", "208", "224"], 1, "Netwerken – Week 2"),

    ("Wat is de binaire representatie van decimaal 192?",
     ["10110000", "11000000", "11000100", "11010000"], 1, "Netwerken – Week 2"),

    ("Hoeveel subnetten kun je maken met een /26-masker in een /24-netwerk?",
     ["2", "4", "8", "16"], 1, "Netwerken – Week 2"),

    ("Welk subnetmasker hoort bij een /28 prefix?",
     ["255.255.255.224", "255.255.255.240", "255.255.255.248", "255.255.255.252"], 1, "Netwerken – Week 2"),

    ("Hoeveel bruikbare hostadressen heeft een /30-subnet?",
     ["2", "4", "6", "8"], 0, "Netwerken – Week 2"),

    ("Wat is het doel van subnetting?",
     ["Het verhogen van de bandbreedte",
      "Het opdelen van een groot netwerk in kleinere, beheersbare subnetten",
      "Het versleutelen van IP-pakketten",
      "Het toewijzen van MAC-adressen"], 1, "Netwerken – Week 2"),

    ("Welk adres is een geldig privé-adres?",
     ["172.32.0.1", "192.169.1.1", "10.0.0.1", "8.8.8.8"], 2, "Netwerken – Week 2"),

    ("Wat is het netwerkadres van 172.16.5.10 /16?",
     ["172.16.5.0", "172.16.0.0", "172.0.0.0", "172.16.5.255"], 1, "Netwerken – Week 2"),

    ("Een router is nodig voor communicatie tussen twee hosts als …",
     ["ze hetzelfde MAC-adres hebben",
      "ze in verschillende subnetten zitten",
      "ze hetzelfde IP-adres hebben",
      "ze via WiFi verbonden zijn"], 1, "Netwerken – Week 2"),

    # ══════════════════ EXTRA – Netwerken Week 3 ══════════════════
    ("Wat staat er in een Ethernet-frame als bestemmingsadres?",
     ["Het IP-adres van de bestemming",
      "Het MAC-adres van de bestemmings-NIC",
      "Het poortnummer van de bestemming",
      "De TTL-waarde"], 1, "Netwerken – Week 3"),

    ("Wat is de minimale grootte van een geldig Ethernet-frame?",
     ["32 bytes", "48 bytes", "64 bytes", "128 bytes"], 2, "Netwerken – Week 3"),

    ("Wat is een 'runt frame' in Ethernet?",
     ["Een frame groter dan 1518 bytes",
      "Een frame kleiner dan 64 bytes",
      "Een frame met een CRC-fout",
      "Een frame zonder bestemmingsadres"], 1, "Netwerken – Week 3"),

    ("Waarvoor staat LLC in de Datalink-laag?",
     ["Link Layer Control", "Logical Link Control",
      "Local Link Connection", "Layered Link Communication"], 1, "Netwerken – Week 3"),

    ("Wat is de functie van de MAC-sublaag?",
     ["Communicatie met de bovenliggende lagen",
      "Data-inkapseling en mediatoegangsbeheer",
      "Versleuteling van frames",
      "Routebepaling tussen netwerken"], 1, "Netwerken – Week 3"),

    ("Wat doet een switch als hij een frame ontvangt met een onbekend bestemmings-MAC-adres?",
     ["Het frame verwijderen",
      "Het frame terugsturen naar de afzender",
      "Het frame flooden naar alle poorten behalve de inkomende poort",
      "Een ARP-verzoek sturen"], 2, "Netwerken – Week 3"),

    ("Wat is het multicast MAC-adresprefix voor IPv4?",
     ["FF-FF-FF-FF-FF-FF", "01-00-5E", "00-00-00", "AA-BB-CC"], 1, "Netwerken – Week 3"),

    ("Wat is het broadcast MAC-adres in Ethernet?",
     ["00-00-00-00-00-00", "FF-FF-FF-FF-FF-FF",
      "01-00-5E-00-00-00", "AA-AA-AA-AA-AA-AA"], 1, "Netwerken – Week 3"),

    ("Wat is de functie van Auto-MDIX op een switch?",
     ["Automatisch VLANs configureren",
      "Automatisch het kabeltype detecteren en de interface aanpassen",
      "Automatisch een IP-adres toewijzen",
      "Automatisch de duplex-instelling bepalen"], 1, "Netwerken – Week 3"),

    ("Wat is het verschil tussen bandbreedte en throughput?",
     ["Ze zijn hetzelfde",
      "Bandbreedte is de theoretische capaciteit; throughput is de werkelijk gemeten overdrachtssnelheid",
      "Throughput is altijd hoger dan bandbreedte",
      "Bandbreedte meet latency; throughput meet pakketgrootte"], 1, "Netwerken – Week 3"),

    # ══════════════════ EXTRA – Platformen Week 1 ══════════════════
    ("Wat is het verschil tussen een enterprise Linux-distributie en een hobbyistendistributie?",
     ["Enterprise distributies zijn altijd gratis; hobbyisten betalen",
      "Enterprise distributies prioriteren stabiliteit en langdurige ondersteuning; hobbyisten prioriteren nieuwe software",
      "Enterprise distributies hebben geen grafische interface",
      "Hobbyisten distributies zijn veiliger"], 1, "Platformen – Week 1"),

    ("Welke package manager wordt gebruikt door RHEL/Rocky Linux?",
     ["apt", "dnf/yum", "pacman", "zypper"], 1, "Platformen – Week 1"),

    ("Wat is een package in de context van Linux software-installatie?",
     ["Een map met bestanden",
      "Een verzameling bestanden en scripts met versieinformatie en afhankelijkheden",
      "Een ISO-image",
      "Een configuratiebestand"], 1, "Platformen – Week 1"),

    ("Wat is een repository in Linux?",
     ["Een lokale map met logbestanden",
      "Een online bibliotheek van softwarepakketten voor een distributie",
      "Een type partitie",
      "Een back-uplocatie"], 1, "Platformen – Week 1"),

    ("Wat is het doel van Logical Volume Management (LVM) bij een Linux-installatie?",
     ["Het versleutelen van de harde schijf",
      "Het flexibel beheren van opslagruimte zonder strikte partitiegrenzen",
      "Het installeren van de bootloader",
      "Het beheren van gebruikersaccounts"], 1, "Platformen – Week 1"),

    ("Welke partitie is VERPLICHT bij een Linux UEFI-systeem?",
     ["/home", "/var", "/boot/efi", "/tmp"], 2, "Platformen – Week 1"),

    ("Waarvoor dient de /boot-partitie?",
     ["Voor gebruikers-homedirectories",
      "Voor het opslaan van de kernel en bootbestanden",
      "Voor tijdelijke bestanden",
      "Voor applicatiedata"], 1, "Platformen – Week 1"),

    ("Wat is het aanbevolen swap-volume op een server met 4 GB RAM?",
     ["2 GB", "8 GB", "4 GB (vuistregel: 2x RAM, maar max 4 GB op servers)", "16 GB"], 2, "Platformen – Week 1"),

    ("Welke Windows Server-installatie heeft de kleinste aanvalsoppervlakte?",
     ["Desktop Experience", "Server Core", "Nano Server", "Hyper-V Server"], 2, "Platformen – Week 1"),

    ("Wat is een Linked Clone in VMware?",
     ["Een volledige kopie van een VM die onafhankelijk werkt",
      "Een VM die verwijzingen behoudt naar de originele base disk en zo schijfruimte bespaart",
      "Een VM-snapshot",
      "Een VM die draait in de cloud"], 1, "Platformen – Week 1"),

    # ══════════════════ EXTRA – Platformen Week 2 (Shell) ══════════════════
    ("Welk commando toont de inhoud van een directory in Linux?",
     ["pwd", "cd", "ls", "cat"], 2, "Platformen – Week 2"),

    ("Wat doet het commando 'cat /etc/passwd'?",
     ["Verwijdert het passwd-bestand",
      "Toont de inhoud van /etc/passwd op het scherm",
      "Zoekt naar gebruikers in het passwd-bestand",
      "Bewerkt het passwd-bestand"], 1, "Platformen – Week 2"),

    ("Wat doet de pipe-operator '|' in Linux?",
     ["Stuurt uitvoer naar een bestand",
      "Verbindt de uitvoer van één commando met de invoer van een volgend commando",
      "Verwijdert een bestand",
      "Maakt een nieuwe directory aan"], 1, "Platformen – Week 2"),

    ("Welk commando zoekt recursief naar alle .log-bestanden op het systeem?",
     ["grep '*.log' /", "ls -R *.log", "find / -name '*.log'", "search / *.log"], 2, "Platformen – Week 2"),

    ("Wat toont het commando 'echo $PATH'?",
     ["De inhoud van de home-directory",
      "Het zoekpad voor uitvoerbare bestanden",
      "De naam van de huidige gebruiker",
      "De hostnaam van het systeem"], 1, "Platformen – Week 2"),

    ("Wat is het verschil tussen 'more' en 'less' in Linux?",
     ["Ze zijn identiek",
      "'less' is een uitgebreidere versie van 'more' waarmee je ook terug kunt bladeren",
      "'more' is nieuwer dan 'less'",
      "'less' toont alleen de eerste pagina"], 1, "Platformen – Week 2"),

    ("Welk commando hernoemt een bestand in Linux?",
     ["rename", "rn", "mv", "cp"], 2, "Platformen – Week 2"),

    ("Wat doet 'cp -r /etc ~/etc.backup'?",
     ["Verplaatst /etc naar ~/etc.backup",
      "Kopieert de directory /etc inclusief alle subdirectories naar ~/etc.backup",
      "Maakt een link van /etc naar ~/etc.backup",
      "Synchroniseert /etc met ~/etc.backup"], 1, "Platformen – Week 2"),

    ("Wat doet '2>' bij output-redirection?",
     ["Stuurt standaardinvoer om",
      "Stuurt standaarduitvoer om",
      "Stuurt foutmeldingen (stderr) om naar een bestand",
      "Voegt toe aan een bestand"], 2, "Platformen – Week 2"),

    ("Welk commando geeft alle omgevingsvariabelen (environment variables) weer?",
     ["env of set", "vars", "echo $ALL", "printenv --all"], 0, "Platformen – Week 2"),

    ("Wat is de functie van het commando 'man' in Linux?",
     ["Het beheren van gebruikers",
      "Het tonen van de handleiding (manual page) van een commando",
      "Het aanmaken van mappen",
      "Het monitoren van processen"], 1, "Platformen – Week 2"),

    ("Welk commando zoek je om te weten welk commando bij 'copy' hoort?",
     ["man copy", "help copy", "man -k copy", "find copy"], 2, "Platformen – Week 2"),

    ("Wat is een login shell in Linux?",
     ["Een shell die gestart wordt door een ander programma",
      "Een shell die gestart wordt bij het inloggen en de volledige configuratie laadt",
      "Een shell die alleen root mag gebruiken",
      "Een shell zonder configuratiebestanden"], 1, "Platformen – Week 2"),

    ("Welk configuratiebestand geldt voor alle gebruikers bij een bash login shell?",
     ["~/.bashrc", "~/.bash_profile", "/etc/profile", "/etc/bashrc"], 2, "Platformen – Week 2"),

    # ══════════════════ EXTRA – Netwerken Week 1 (IOS/CLI aanvulling) ══════════════════
    ("Welke IOS-modus gebruik je voor het configureren van een interface?",
     ["User EXEC mode", "Privileged EXEC mode",
      "Global Configuration mode", "Interface Configuration mode"], 3, "Netwerken – Week 1"),

    ("Hoe kom je vanuit Global Configuration mode naar Privileged EXEC mode?",
     ["exit", "end of Ctrl-Z", "disable", "quit"], 1, "Netwerken – Week 1"),

    ("Wat is het commando om een hostname in te stellen op een Cisco-apparaat?",
     ["set hostname SW1", "hostname SW1", "name SW1", "device-name SW1"], 1, "Netwerken – Week 1"),

    ("Welk commando configureert een IP-adres op een Cisco router-interface?",
     ["set ip address 192.168.1.1 255.255.255.0",
      "ip address 192.168.1.1 255.255.255.0",
      "interface ip 192.168.1.1/24",
      "assign ip 192.168.1.1 mask 255.255.255.0"], 1, "Netwerken – Week 1"),

    ("Wat is SSH in vergelijking met Telnet?",
     ["SSH is langzamer maar eenvoudiger",
      "SSH is versleuteld en veiliger; Telnet verstuurt data in plaintext",
      "Telnet is veiliger dan SSH",
      "Ze zijn functioneel identiek"], 1, "Netwerken – Week 1"),

    # ══════════════════ GAPS – Netwerken Week 1 ══════════════════
    ("Wat is het verschil tussen een WAN en een LAN qua beheer?",
     ["Een LAN wordt beheerd door een provider; een WAN door één organisatie",
      "Een LAN wordt beheerd door één organisatie; een WAN door één of meer providers",
      "Beide worden altijd beheerd door een provider",
      "Er is geen verschil in beheer"], 1, "Netwerken – Week 1"),

    ("Wat is een loopback-interface op een router?",
     ["Een fysieke interface voor WAN-verbindingen",
      "Een virtuele interface die nooit down gaat en gebruikt wordt voor testen en protocollen zoals OSPF",
      "Een interface die alleen voor console-toegang dient",
      "Een back-upinterface die actief wordt als een andere interface uitvalt"], 1, "Netwerken – Week 1"),

    ("Welk IOS-commando configureert een 'banner of the day' (MOTD)?",
     ["banner login #tekst#", "banner motd #tekst#", "motd banner #tekst#", "set banner #tekst#"], 1, "Netwerken – Week 1"),

    ("Welke toegangsmethode gebruik je voor de EERSTE configuratie van een Cisco-apparaat zonder netwerk?",
     ["SSH", "Telnet", "Console", "HTTP"], 2, "Netwerken – Week 1"),

    ("Wat is goodput?",
     ["De theoretische maximale bandbreedte van een medium",
      "De gemeten overdrachtssnelheid inclusief overhead",
      "De hoeveelheid bruikbare data die per tijdseenheid wordt overgedragen (throughput minus overhead)",
      "De latency van een verbinding"], 2, "Netwerken – Week 1"),

    ("Wat is segmentering in netwerkcommunicatie?",
     ["Het opdelen van een netwerk in subnetten",
      "Het opsplitsen van een groot bericht in kleinere stukken voor verzending",
      "Het versleutelen van data voor transport",
      "Het samenvoegen van meerdere frames tot één pakket"], 1, "Netwerken – Week 1"),

    ("Wat is multicast?",
     ["Een bericht van één afzender naar alle hosts",
      "Een bericht van één afzender naar één specifieke ontvanger",
      "Een bericht van één afzender naar een specifieke groep ontvangers",
      "Een bericht dat automatisch wordt doorgestuurd door routers"], 2, "Netwerken – Week 1"),

    # ══════════════════ GAPS – Netwerken Week 2 ══════════════════
    ("Wat is de functie van het TTL-veld in een IPv4-pakketheader?",
     ["Het geeft de versie van het IP-protocol aan",
      "Het beperkt de levensduur van een pakket door het te verminderen bij elke router; bij 0 wordt het pakket verwijderd",
      "Het identificeert het bovenliggende protocol (TCP/UDP)",
      "Het geeft de prioriteit van het pakket aan"], 1, "Netwerken – Week 2"),

    ("Welk veld in de IPv4-header identificeert het bovenliggende protocol (bijv. TCP of UDP)?",
     ["Version", "TTL", "Protocol", "DS (Differentiated Services)"], 2, "Netwerken – Week 2"),

    ("Waarvoor dient het TEST-NET adresblok 192.0.2.0/24?",
     ["Voor privé-netwerken thuis",
      "Voor documentatie en leermateriaal, niet voor echt gebruik",
      "Voor multicast-toepassingen",
      "Voor ISP-backbone-verbindingen"], 1, "Netwerken – Week 2"),

    ("Tot welke klasse behoort het adres 172.20.0.1 in het classful adresseringssysteem?",
     ["Klasse A", "Klasse B", "Klasse C", "Klasse D"], 1, "Netwerken – Week 2"),

    ("Wat zijn de vier basisoperaties van de netwerklaag (OSI L3)?",
     ["Framing, adressering, foutdetectie, stroomregeling",
      "Adressering, inkapseling, routering, de-inkapseling",
      "Segmentering, sessie, presentatie, applicatie",
      "Codering, modulatie, transmissie, decodering"], 1, "Netwerken – Week 2"),

    # ══════════════════ GAPS – Netwerken Week 3 ══════════════════
    ("Wat is CSMA/CA en waar wordt het gebruikt?",
     ["Collision detection op bedrade netwerken (Ethernet)",
      "Collision avoidance op draadloze netwerken (WiFi/802.11)",
      "Een methode om MAC-adressen toe te wijzen",
      "Een encryptieprotocol voor WiFi"], 1, "Netwerken – Week 3"),

    ("Welk voordeel heeft glasvezel (fiber optic) ten opzichte van koper?",
     ["Goedkoper en eenvoudiger te installeren",
      "Grotere afstanden, minder demping en immuun voor elektromagnetische storing (EMI)",
      "Hogere weerstand tegen elektrische stroom",
      "Eenvoudiger te repareren"], 1, "Netwerken – Week 3"),

    ("Waarvoor wordt een rollover-kabel (consolekabel) gebruikt?",
     ["Het verbinden van twee switches met elkaar",
      "Het verbinden van een PC met de consolepoort van een router of switch",
      "Het verbinden van een router met een WAN-provider",
      "Het verbinden van twee routers back-to-back"], 1, "Netwerken – Week 3"),

    ("Welk WiFi-standaard (IEEE) wordt het meest gebruikt voor draadloze netwerken?",
     ["IEEE 802.15", "IEEE 802.11", "IEEE 802.16", "IEEE 802.3"], 1, "Netwerken – Week 3"),

    ("Welk IEEE-standaard hoort bij Bluetooth?",
     ["802.11", "802.15", "802.16", "802.3"], 1, "Netwerken – Week 3"),

    ("Welk commando toont de ARP-tabel op een Windows-pc?",
     ["show ip arp", "arp -a", "ipconfig /arp", "netstat -a"], 1, "Netwerken – Week 3"),

    ("Welk commando toont de ARP-tabel op een Cisco IOS-apparaat?",
     ["show arp table", "show ip arp", "display arp", "arp -a"], 1, "Netwerken – Week 3"),

    ("Wat stuurt een host wanneer hij het MAC-adres van een bestemmingshost niet kent?",
     ["Een ICMP-pakket naar de router",
      "Een ARP Request als broadcast naar alle hosts in het subnet",
      "Een DNS-verzoek naar de DNS-server",
      "Een TCP SYN-pakket naar de bestemming"], 1, "Netwerken – Week 3"),

    ("Welk veld in een Ethernet-frame wordt gebruikt voor foutdetectie?",
     ["Type-veld", "Start Frame Delimiter", "Frame Check Sequence (FCS) / CRC", "Preamble"], 2, "Netwerken – Week 3"),

    # ══════════════════ GAPS – Platformen Week 1 ══════════════════
    ("Wat is Nano Server in Windows?",
     ["Een nog minimalistischere installatie dan Core, alleen beschikbaar als container",
      "Een Windows Server voor kleine bedrijven",
      "De naam van Windows Server Core vóór 2016",
      "Een Linux-gebaseerde servervariant van Microsoft"], 0, "Platformen – Week 1"),

    ("Wat is Kickstart bij Linux-installaties?",
     ["Een tool om de bootloader te installeren",
      "Een methode voor volledig geautomatiseerde (unattended) Linux-installaties",
      "Een package manager voor Red Hat",
      "Een tool om VM-snapshots te maken"], 1, "Platformen – Week 1"),

    ("Wat lost een package manager op bij software-installatie?",
     ["Het compileren van broncode",
      "Onderlinge afhankelijkheden tussen pakketten (dependencies)",
      "Het aanmaken van gebruikersaccounts",
      "Het partitioneren van de harde schijf"], 1, "Platformen – Week 1"),

    ("Welke distributies zijn afgeleid van Debian?",
     ["Fedora en openSUSE",
      "Ubuntu en Ubuntu LTS",
      "Rocky Linux en Oracle Linux",
      "SLES en openSUSE"], 1, "Platformen – Week 1"),

    ("Wat is een OS release in de context van Linux-versiebeheer?",
     ["Een nieuwe versie van de Linux-kernel",
      "Een momentopname van alle beschikbare softwarepakketten waarvan de versies intern consistent zijn",
      "Een beveiligingsupdate voor het besturingssysteem",
      "Een nieuwe distributie gebaseerd op bestaande code"], 1, "Platformen – Week 1"),

    # ══════════════════ GAPS – Platformen Week 2 (shell) ══════════════════
    ("Wat doet het commando 'touch bestand.txt' in Linux?",
     ["Opent het bestand in een teksteditor",
      "Maakt een leeg bestand aan (of past de timestamp aan als het al bestaat)",
      "Geeft de rechten van het bestand weer",
      "Verwijdert het bestand"], 1, "Platformen – Week 2"),

    ("Wat is het verschil tussen '>' en '>>' bij output-redirection?",
     ["'>' voegt toe aan het einde; '>>' overschrijft het bestand",
      "'>' overschrijft het bestand; '>>' voegt toe aan het einde van het bestand",
      "Ze zijn identiek",
      "'>' werkt alleen voor stderr; '>>' voor stdout"], 1, "Platformen – Week 2"),

    ("Wat doet '>&' bij output-redirection in Linux?",
     ["Stuurt alleen stderr om",
      "Stuurt stdout én stderr tegelijk om naar dezelfde bestemming",
      "Stuurt stdin om",
      "Maakt een bidirectionele verbinding"], 1, "Platformen – Week 2"),

    ("Wat doet het 'export'-commando in Linux?",
     ["Exporteert bestanden naar een andere server",
      "Maakt een lokale shell-variabele beschikbaar als omgevingsvariabele voor kindprocessen",
      "Maakt een back-up van de omgevingsvariabelen",
      "Kopieert variabelen naar /etc/profile"], 1, "Platformen – Week 2"),

    ("Wat is PowerShell Remoting en welk commando gebruik je om verbinding te maken?",
     ["Een VPN-verbinding; commando: vpn-connect",
      "Remote beheer via WinRM; commando: Enter-PSSession -computername <naam>",
      "Remote desktop; commando: mstsc /v:<naam>",
      "SSH-toegang tot Windows; commando: ssh administrator@<naam>"], 1, "Platformen – Week 2"),

    ("Welk commando configureert een statisch IP-adres op een Windows Server Core via netsh?",
     ["netsh interface ipv4 set address name=<id> source=static address=<ip> mask=<mask> gateway=<gw>",
      "ipconfig /setip <id> <ip> <mask>",
      "set-netipaddress -ip <ip> -mask <mask>",
      "netsh ip set static <id> <ip> <mask>"], 0, "Platformen – Week 2"),

    ("Welk commando verwijdert een lege directory in Linux?",
     ["rm -r", "rmdir", "del", "remove"], 1, "Platformen – Week 2"),

    # ══════════════════ GAPS – Platformen Week 3 (AD) ══════════════════
    ("Waarom is DNS vereist voor Active Directory?",
     ["DNS versleutelt de AD-communicatie",
      "AD gebruikt DNS voor het lokaliseren van domeincontrollers en services; zonder DNS werkt AD niet",
      "DNS beheert de gebruikersaccounts in AD",
      "DNS is alleen nodig voor internetverbindingen, niet voor AD"], 1, "Platformen – Week 3"),

    ("Wat is een Domain Functional Level (DFL) in Active Directory?",
     ["Het aantal gebruikers dat een domein kan bevatten",
      "Een instelling die bepaalt welke AD-functies beschikbaar zijn op basis van de minimale DC-versie",
      "De maximale grootte van de AD-database",
      "Het beveiligingsniveau van wachtwoordversleuteling"], 1, "Platformen – Week 3"),

    ("Wat is SYSVOL in Active Directory?",
     ["Een beveiligingsprotocol voor DC-communicatie",
      "Een gedeelde map op DC's die scripts en Group Policy-bestanden bevat en gerepliceerd wordt",
      "De locatie van de AD-database (ntds.dit)",
      "Een tool voor het beheren van AD-objecten"], 1, "Platformen – Week 3"),

    ("Welk commando voegt een computer toe aan een domein via de command prompt (netdom)?",
     ["netdom join Server1 /d:domein.local /reboot",
      "netdom add Server1 /domain:domein.local",
      "domain join Server1 /d:domein.local",
      "netsh join Server1 /domain:domein.local"], 0, "Platformen – Week 3"),

    ("Wat is de Global Catalog in Active Directory?",
     ["Een lijst van alle Group Policy Objects",
      "Een gedeeltelijke, alleen-lezen kopie van alle objecten in het forest, gebruikt voor snelle zoekopdrachten",
      "De volledige database van één domein",
      "Een back-up van de AD-database"], 1, "Platformen – Week 3"),

    ("Wat doet DSMOD?",
     ["Zoekt objecten in Active Directory",
      "Verplaatst objecten binnen Active Directory",
      "Wijzigt eigenschappen van bestaande objecten in Active Directory",
      "Verwijdert objecten uit Active Directory"], 2, "Platformen – Week 3"),

    ("Aan hoeveel van de vier wachtwoordcomplexiteitseisen moet een AD-wachtwoord standaard voldoen?",
     ["Aan alle vier", "Aan minimaal drie van de vier", "Aan minimaal twee van de vier", "Aan minimaal één"], 1, "Platformen – Week 3"),

    ("Hoe ziet een UPN (User Principal Name) eruit in Active Directory?",
     ["DOMEIN\\gebruikersnaam", "gebruikersnaam@domein.com",
      "CN=gebruiker,DC=domein,DC=com", "gebruikersnaam.domein"], 1, "Platformen – Week 3"),

    ("Welk well-known SID hoort bij het Administrator-account?",
     ["S-1-3-0", "S-1-5-2", "S-1-5-11", "S-1-5-domein-500"], 3, "Platformen – Week 3"),

    # ══════════════════ GAPS – Platformen Week 3 Linux ══════════════════
    ("Welke drie bestanden zijn belangrijk voor gebruikers- en groepsbeheer onder Linux?",
     ["/etc/users, /etc/groups, /etc/passwords",
      "/etc/passwd, /etc/shadow, /etc/group",
      "/etc/accounts, /etc/shadow, /etc/sudoers",
      "/etc/passwd, /etc/shadow, /etc/sudoers"], 1, "Platformen – Week 3 Linux"),

    ("Wat bevat het bestand /etc/group onder Linux?",
     ["De versleutelde wachtwoorden van gebruikers",
      "De groepsnamen, groeps-ID's (GID) en groepsleden",
      "De sudo-configuratie",
      "De home-directories van gebruikers"], 1, "Platformen – Week 3 Linux"),

    ("Wat is een GID onder Linux?",
     ["Een Global Identifier voor AD-objecten",
      "Een uniek numeriek ID dat aan een groep wordt toegewezen",
      "Een encryptiesleutel voor wachtwoorden",
      "De naam van de primaire groep van een gebruiker"], 1, "Platformen – Week 3 Linux"),

    ("Wat is het GECOS-veld in /etc/passwd?",
     ["Het versleutelde wachtwoord",
      "Een veld voor aanvullende persoonlijke informatie over de gebruiker (naam, telefoon, etc.)",
      "De home-directory van de gebruiker",
      "De standaard shell van de gebruiker"], 1, "Platformen – Week 3 Linux"),

    ("Wat is het doel van /etc/skel?",
     ["Het bevat schaduwkopieën van systeembestanden",
      "Het is een sjabloon: bestanden hierin worden gekopieerd naar de home-directory van elke nieuwe gebruiker",
      "Het bevat tijdelijke bestanden",
      "Het bevat de sudo-configuratie"], 1, "Platformen – Week 3 Linux"),

    ("Wat is het verschil tussen 'useradd' en 'adduser'?",
     ["Ze zijn volledig identiek",
      "'useradd' is een laagniveau systeemcommando; 'adduser' is een gebruiksvriendelijker script dat meer stappen automatiseert",
      "'adduser' werkt alleen op Debian; 'useradd' alleen op Red Hat",
      "'useradd' maakt ook automatisch een home-directory aan; 'adduser' niet"], 1, "Platformen – Week 3 Linux"),

    ("Welk commando verwijdert een gebruikersaccount onder Linux?",
     ["usermod --delete", "userdel", "rmuser", "deluser --system"], 1, "Platformen – Week 3 Linux"),

    ("Welk commando stel je de maximale wachtwoordgeldigheid in voor een gebruiker onder Linux?",
     ["chmod", "passwdmod", "chage", "usermod --maxage"], 2, "Platformen – Week 3 Linux"),

    # ══════════════════ GAPS – Platformen Week 4 NTFS ══════════════════
    ("Wat is een ACE (Access Control Entry)?",
     ["Een foutmelding bij een geweigerde toegang",
      "Eén regel in een DACL die aangeeft welke rechten een specifieke gebruiker of groep heeft op een object",
      "Een versleutelingsmethode voor NTFS",
      "Een type gebruikersaccount in Windows"], 1, "Platformen – Week 4"),

    ("Wat gebeurt er met NTFS-permissies als je een bestand kopieert naar een andere NTFS-partitie?",
     ["De permissies blijven exact hetzelfde",
      "Het bestand erft de permissies van de doelmap",
      "Alle permissies worden verwijderd",
      "Alleen de eigenaar-permissie blijft behouden"], 1, "Platformen – Week 4"),

    ("Als share-permissie 'Change' is en NTFS-permissie 'Full Control', wat zijn de effectieve permissies?",
     ["Full Control, want NTFS wint altijd",
      "Change, want de meest beperkende van share en NTFS geldt",
      "Read Only, want veiligheid gaat voor",
      "Geen toegang, want de permissies conflicteren"], 1, "Platformen – Week 4"),

    # ══════════════════ GAPS – Platformen Week 4 Linux ══════════════════
    ("Wat is de sticky bit op een directory?",
     ["Geeft alle gebruikers volledige toegang",
      "Zorgt ervoor dat alleen de eigenaar (of root) zijn eigen bestanden in die directory kan verwijderen",
      "Maakt de directory verborgen",
      "Geeft de groep schrijfrechten op de directory"], 1, "Platformen – Week 4 Linux"),

    ("Wat doet de setuid-bit op een uitvoerbaar bestand?",
     ["Het bestand wordt uitgevoerd met de rechten van de eigenaar, ongeacht wie het uitvoert",
      "Het bestand kan niet worden verwijderd",
      "Het bestand wordt versleuteld bij uitvoering",
      "Het bestand krijgt automatisch uitvoerrechten"], 0, "Platformen – Week 4 Linux"),

    ("Welk commando toont het schijfgebruik per directory in Linux?",
     ["df", "du", "lsblk", "fdisk -l"], 1, "Platformen – Week 4 Linux"),

    ("Welk commando toont de beschikbare schijfruimte op gemounte bestandssystemen?",
     ["du", "df", "lsblk", "mount -l"], 1, "Platformen – Week 4 Linux"),

    ("Wat is een inode in een Linux-bestandssysteem?",
     ["Een type harde schijf",
      "Een datastructuur die metadata van een bestand opslaat (rechten, eigenaar, grootte, locatie op schijf)",
      "Een directory-entry",
      "Een type symbolische link"], 1, "Platformen – Week 4 Linux"),

    ("Wat is het verschil tussen ext2 en ext3?",
     ["ext3 is sneller dan ext2",
      "ext3 heeft journaling toegevoegd ten opzichte van ext2",
      "ext2 ondersteunt grotere bestanden dan ext3",
      "Er is geen praktisch verschil"], 1, "Platformen – Week 4 Linux"),

    ("Wat betekent de permissie '777' op een bestand of directory?",
     ["Alleen de eigenaar heeft alle rechten",
      "Eigenaar, groep én anderen hebben alle rechten (lezen, schrijven, uitvoeren)",
      "Niemand heeft rechten",
      "Alleen root heeft alle rechten"], 1, "Platformen – Week 4 Linux"),

    ("Welke van de zeven Linux-bestandstypes is een symbolische link?",
     ["regular file", "directory", "symbolic link", "block device file"], 2, "Platformen – Week 4 Linux"),
]


# ─────────────────────────────────────────────
# GUI APPLICATION
# ─────────────────────────────────────────────

class QuizApp:
    NUM_QUESTIONS = 20

    # ── Palette: clean light theme, fully consistent ──────────────────
    BG        = "#F4F6FB"   # page background – soft cool grey
    SIDEBAR   = "#1F2D4E"   # deep navy – header / sidebar strip
    CARD      = "#FFFFFF"   # card surface
    BORDER    = "#DDE3F0"   # subtle border
    ACCENT    = "#3B6FE8"   # primary blue
    ACCENT_HV = "#2A55C0"   # hover blue
    TEXT      = "#1A1D2E"   # near-black text
    SUBTEXT   = "#6B7280"   # muted grey text
    NAVY_TXT  = "#FFFFFF"   # text on dark sidebar
    CORRECT   = "#16A34A"   # green
    CORRECT_BG= "#ECFDF5"   # light green fill
    WRONG     = "#DC2626"   # red
    WRONG_BG  = "#FEF2F2"   # light red fill
    OPT_HOVER = "#EEF2FF"   # option hover fill

    def __init__(self, root):
        self.root = root
        self.root.title("BIPL Toets Oefening")
        self.root.geometry("940x720")
        self.root.minsize(820, 600)
        self.root.configure(bg=self.BG)

        self.questions      = []
        self.current        = 0
        self.score          = 0
        self.answered       = False
        self.option_buttons = []
        self.results        = []

        self._setup_styles()
        self._build_welcome()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Quiz.Horizontal.TProgressbar",
                        troughcolor=self.BORDER,
                        background=self.ACCENT,
                        bordercolor=self.BG,
                        lightcolor=self.ACCENT,
                        darkcolor=self.ACCENT,
                        thickness=6)
        style.configure("Thin.Vertical.TScrollbar",
                        troughcolor=self.BG,
                        background=self.BORDER,
                        bordercolor=self.BG,
                        arrowcolor=self.SUBTEXT)

    # ──────────────────────────────────────────────────────────────────
    # WELCOME SCREEN
    # ──────────────────────────────────────────────────────────────────
    def _build_welcome(self):
        self._clear()

        # Top navy banner
        banner = tk.Frame(self.root, bg=self.SIDEBAR, height=8)
        banner.pack(fill="x")

        # Centre content
        outer = tk.Frame(self.root, bg=self.BG)
        outer.pack(expand=True)

        # Card
        card = tk.Frame(outer, bg=self.CARD,
                        highlightthickness=1,
                        highlightbackground=self.BORDER)
        card.pack(padx=60, pady=40, ipadx=40, ipady=40)

        # Header strip inside card
        hdr = tk.Frame(card, bg=self.SIDEBAR)
        hdr.pack(fill="x")
        tk.Label(hdr, text="BIPL  Toets Oefening",
                 font=("Segoe UI", 20, "bold"),
                 bg=self.SIDEBAR, fg=self.NAVY_TXT,
                 padx=28, pady=18).pack(side="left")

        body = tk.Frame(card, bg=self.CARD)
        body.pack(padx=28, pady=24)

        tk.Label(body, text="Netwerken & Platformen – Weken 1 t/m 4",
                 font=("Segoe UI", 12), bg=self.CARD,
                 fg=self.SUBTEXT).pack(pady=(0, 22))

        # Info bullets
        for bullet in (
            f"  ✦   {self.NUM_QUESTIONS} willekeurige vragen per ronde",
            "  ✦   Antwoordopties worden elke keer geschud",
            "  ✦   Direct feedback + uitleg bij elk antwoord",
            "  ✦   Volledig scoreoverzicht aan het einde",
        ):
            tk.Label(body, text=bullet,
                     font=("Segoe UI", 11), bg=self.CARD,
                     fg=self.TEXT, anchor="w").pack(fill="x", pady=2)

        tk.Frame(body, bg=self.BORDER, height=1).pack(fill="x", pady=20)

        # Stats row
        stats = tk.Frame(body, bg=self.CARD)
        stats.pack(fill="x", pady=(0, 24))
        for val, lbl in ((str(len(ALL_QUESTIONS)), "vragen in bank"),
                         (str(self.NUM_QUESTIONS), "per quiz"),
                         ("55%", "slagingsgrens")):
            cell = tk.Frame(stats, bg=self.ACCENT, padx=18, pady=10)
            cell.pack(side="left", padx=6)
            tk.Label(cell, text=val, font=("Segoe UI", 16, "bold"),
                     bg=self.ACCENT, fg="white").pack()
            tk.Label(cell, text=lbl, font=("Segoe UI", 8),
                     bg=self.ACCENT, fg="#BDD0FF").pack()

        # Start button
        btn = tk.Button(body, text="Start Quiz  →",
                        font=("Segoe UI", 13, "bold"),
                        bg=self.ACCENT, fg="white",
                        activebackground=self.ACCENT_HV,
                        activeforeground="white",
                        relief="flat", padx=36, pady=13,
                        cursor="hand2", bd=0,
                        command=self._start_quiz)
        btn.pack()

    # ──────────────────────────────────────────────────────────────────
    # QUIZ SCREEN
    # ──────────────────────────────────────────────────────────────────
    def _start_quiz(self):
        pool = list(ALL_QUESTIONS)
        random.shuffle(pool)
        self.questions = pool[:self.NUM_QUESTIONS]
        self.current   = 0
        self.score     = 0
        self.answered  = False
        self.results   = []
        self._build_quiz_ui()
        self._load_question()

    def _build_quiz_ui(self):
        self._clear()

        # ── Top bar (navy) ──
        topbar = tk.Frame(self.root, bg=self.SIDEBAR)
        topbar.pack(fill="x")

        tk.Label(topbar, text="BIPL Toets Oefening",
                 font=("Segoe UI", 11, "bold"),
                 bg=self.SIDEBAR, fg=self.NAVY_TXT,
                 padx=20, pady=10).pack(side="left")

        self.lbl_score = tk.Label(topbar, text="",
                                  font=("Segoe UI", 11, "bold"),
                                  bg=self.SIDEBAR, fg="#93C5FD",
                                  padx=20)
        self.lbl_score.pack(side="right")

        self.lbl_progress = tk.Label(topbar, text="",
                                     font=("Segoe UI", 10),
                                     bg=self.SIDEBAR, fg="#93C5FD",
                                     padx=6)
        self.lbl_progress.pack(side="right")

        # ── Progress bar ──
        self.progress_bar = ttk.Progressbar(self.root,
                                            style="Quiz.Horizontal.TProgressbar",
                                            mode="determinate",
                                            maximum=self.NUM_QUESTIONS)
        self.progress_bar.pack(fill="x")

        # ── Scrollable main area ──
        canvas = tk.Canvas(self.root, bg=self.BG,
                           highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical",
                                  command=canvas.yview,
                                  style="Thin.Vertical.TScrollbar")
        self._quiz_inner = tk.Frame(canvas, bg=self.BG)
        self._quiz_inner.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self._quiz_inner, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        canvas.bind_all("<MouseWheel>",
                        lambda e: canvas.yview_scroll(
                            int(-1*(e.delta/120)), "units"))
        self._quiz_canvas = canvas

        pad = tk.Frame(self._quiz_inner, bg=self.BG)
        pad.pack(fill="x", padx=30, pady=20)

        # Topic badge
        self.lbl_topic = tk.Label(pad, text="",
                                  font=("Segoe UI", 9, "bold"),
                                  bg=self.ACCENT, fg="white",
                                  padx=10, pady=4)
        self.lbl_topic.pack(anchor="w", pady=(0, 10))

        # Question card
        qcard = tk.Frame(pad, bg=self.CARD,
                         highlightthickness=1,
                         highlightbackground=self.BORDER)
        qcard.pack(fill="x")

        # Coloured left stripe
        tk.Frame(qcard, bg=self.ACCENT, width=5).pack(side="left", fill="y")

        self.lbl_question = tk.Label(qcard, text="",
                                     wraplength=800,
                                     font=("Segoe UI", 13),
                                     bg=self.CARD, fg=self.TEXT,
                                     justify="left",
                                     padx=20, pady=20)
        self.lbl_question.pack(fill="x", expand=True)

        # Options
        self.opts_pad = tk.Frame(pad, bg=self.BG)
        self.opts_pad.pack(fill="x", pady=(12, 0))

        self.option_buttons = []
        for i in range(4):
            row = tk.Frame(self.opts_pad, bg=self.CARD,
                           highlightthickness=1,
                           highlightbackground=self.BORDER,
                           cursor="hand2")
            row.pack(fill="x", pady=5)

            # Letter badge
            badge = tk.Label(row, text=chr(65 + i),
                             font=("Segoe UI", 11, "bold"),
                             bg=self.BORDER, fg=self.SUBTEXT,
                             width=3, pady=14)
            badge.pack(side="left", fill="y")

            lbl = tk.Label(row, text="",
                           font=("Segoe UI", 11),
                           bg=self.CARD, fg=self.TEXT,
                           anchor="w", justify="left",
                           wraplength=750,
                           padx=14, pady=14)
            lbl.pack(side="left", fill="x", expand=True)

            # Bind clicks to both row, badge and label
            for widget in (row, badge, lbl):
                widget.bind("<Button-1>",
                            lambda e, idx=i: self._select_answer(idx))
                widget.bind("<Enter>",
                            lambda e, r=row, b=badge, l=lbl: self._opt_hover(r, b, l, True))
                widget.bind("<Leave>",
                            lambda e, r=row, b=badge, l=lbl: self._opt_hover(r, b, l, False))

            self.option_buttons.append((row, badge, lbl))

        # Feedback bar
        self.lbl_feedback = tk.Label(pad, text="",
                                     font=("Segoe UI", 11, "bold"),
                                     bg=self.BG, fg=self.TEXT,
                                     wraplength=860, justify="left",
                                     pady=6)
        self.lbl_feedback.pack(anchor="w", pady=(10, 0))

        # Next button
        self.btn_next = tk.Button(pad, text="Volgende vraag  →",
                                  font=("Segoe UI", 12, "bold"),
                                  bg=self.ACCENT, fg="white",
                                  activebackground=self.ACCENT_HV,
                                  activeforeground="white",
                                  relief="flat", padx=28, pady=12,
                                  cursor="hand2", bd=0,
                                  command=self._next_question,
                                  state="disabled")
        self.btn_next.pack(anchor="e", pady=(14, 30))

    def _opt_hover(self, row, badge, lbl, entering):
        if entering:
            row.config(highlightbackground=self.ACCENT,
                       bg=self.OPT_HOVER)
            badge.config(bg=self.ACCENT, fg="white")
            lbl.config(bg=self.OPT_HOVER)
        else:
            # Only reset if not already answered (coloured)
            if row.cget("bg") not in (self.CORRECT_BG, self.WRONG_BG):
                row.config(highlightbackground=self.BORDER, bg=self.CARD)
                badge.config(bg=self.BORDER, fg=self.SUBTEXT)
                lbl.config(bg=self.CARD)

    def _load_question(self):
        q_text, options, correct, topic = self.questions[self.current]
        self.answered = False

        n = self.current + 1
        self.lbl_progress.config(text=f"Vraag {n} / {self.NUM_QUESTIONS}")
        self.lbl_score.config(text=f"Score: {self.score}")
        self.progress_bar["value"] = self.current
        self.lbl_topic.config(text=f"  {topic}  ")
        self.lbl_question.config(text=f"{q_text}")
        self.lbl_feedback.config(text="", bg=self.BG)
        self.btn_next.config(state="disabled",
                             text="Volgende vraag  →" if n < self.NUM_QUESTIONS
                             else "Bekijk resultaten  →")

        indexed = list(enumerate(options))
        random.shuffle(indexed)
        self._shuffled_options = indexed

        for i, (orig_idx, text) in enumerate(indexed):
            row, badge, lbl = self.option_buttons[i]
            row.config(bg=self.CARD,
                       highlightbackground=self.BORDER,
                       cursor="hand2")
            badge.config(text=chr(65 + i),
                         bg=self.BORDER, fg=self.SUBTEXT)
            lbl.config(text=text, bg=self.CARD, fg=self.TEXT)
            for widget in (row, badge, lbl):
                widget.bind("<Button-1>",
                            lambda e, idx=i: self._select_answer(idx))

        # scroll back to top
        self._quiz_canvas.yview_moveto(0)

    def _select_answer(self, idx):
        if self.answered:
            return
        self.answered = True

        q_text, options, correct, topic = self.questions[self.current]
        correct_shuffled = next(
            i for i, (orig, _) in enumerate(self._shuffled_options)
            if orig == correct)

        is_correct = (idx == correct_shuffled)

        def colour_opt(i, bg, badge_bg, badge_fg, text_fg):
            row, badge, lbl = self.option_buttons[i]
            row.config(bg=bg, highlightbackground=badge_bg, cursor="")
            badge.config(bg=badge_bg, fg=badge_fg)
            lbl.config(bg=bg, fg=text_fg)
            for widget in (row, badge, lbl):
                widget.unbind("<Button-1>")
                widget.unbind("<Enter>")
                widget.unbind("<Leave>")

        if is_correct:
            self.score += 1
            colour_opt(idx, self.CORRECT_BG, self.CORRECT, "white", self.CORRECT)
            self.lbl_feedback.config(
                text="  ✓  Correct!",
                fg=self.CORRECT, bg=self.CORRECT_BG)
        else:
            colour_opt(idx, self.WRONG_BG, self.WRONG, "white", self.WRONG)
            colour_opt(correct_shuffled, self.CORRECT_BG, self.CORRECT, "white", self.CORRECT)
            self.lbl_feedback.config(
                text=f"  ✗  Fout.  Juist antwoord: {options[correct]}",
                fg=self.WRONG, bg=self.WRONG_BG)

        # Disable remaining options silently
        for i in range(4):
            if i != idx and i != correct_shuffled:
                colour_opt(i, self.CARD, self.BORDER, self.SUBTEXT, self.SUBTEXT)

        self.results.append({
            "question": q_text,
            "topic": topic,
            "correct": is_correct,
            "your_answer": self._shuffled_options[idx][1],
            "right_answer": options[correct],
        })
        self.btn_next.config(state="normal")

    def _next_question(self):
        self.current += 1
        if self.current >= self.NUM_QUESTIONS:
            self._show_results()
        else:
            self._load_question()

    # ──────────────────────────────────────────────────────────────────
    # RESULTS SCREEN
    # ──────────────────────────────────────────────────────────────────
    def _show_results(self):
        self._clear()

        pct    = round(self.score / self.NUM_QUESTIONS * 100)
        passed = pct >= 55

        result_color  = self.CORRECT if passed else self.WRONG
        result_bg     = self.CORRECT_BG if passed else self.WRONG_BG
        emoji         = "🏆" if pct >= 80 else ("👍" if passed else "📝")
        status_text   = "Geslaagd!" if passed else "Niet geslaagd – blijf oefenen!"

        # ── Header banner ──
        banner = tk.Frame(self.root, bg=self.SIDEBAR)
        banner.pack(fill="x")
        tk.Label(banner, text="Resultaten",
                 font=("Segoe UI", 13, "bold"),
                 bg=self.SIDEBAR, fg=self.NAVY_TXT,
                 padx=20, pady=10).pack(side="left")

        # ── Score card ──
        score_outer = tk.Frame(self.root, bg=result_bg,
                               highlightthickness=1,
                               highlightbackground=result_color)
        score_outer.pack(fill="x", padx=30, pady=(20, 0))

        inner_s = tk.Frame(score_outer, bg=result_bg)
        inner_s.pack(pady=18)

        tk.Label(inner_s, text=emoji,
                 font=("Segoe UI Emoji", 36),
                 bg=result_bg).pack(side="left", padx=(20, 14))

        right = tk.Frame(inner_s, bg=result_bg)
        right.pack(side="left")
        tk.Label(right,
                 text=f"{self.score} / {self.NUM_QUESTIONS}   ({pct}%)",
                 font=("Segoe UI", 22, "bold"),
                 bg=result_bg, fg=result_color).pack(anchor="w")
        tk.Label(right, text=status_text,
                 font=("Segoe UI", 12),
                 bg=result_bg, fg=result_color).pack(anchor="w")

        # ── Review header ──
        tk.Label(self.root,
                 text="Overzicht van jouw antwoorden",
                 font=("Segoe UI", 11, "bold"),
                 bg=self.BG, fg=self.TEXT).pack(
                     anchor="w", padx=30, pady=(16, 4))

        # ── Scrollable list ──
        wrap = tk.Frame(self.root, bg=self.BG)
        wrap.pack(fill="both", expand=True, padx=30, pady=(0, 4))

        cv = tk.Canvas(wrap, bg=self.BG, highlightthickness=0)
        sb = ttk.Scrollbar(wrap, orient="vertical",
                           command=cv.yview,
                           style="Thin.Vertical.TScrollbar")
        inner = tk.Frame(cv, bg=self.BG)
        inner.bind("<Configure>",
                   lambda e: cv.configure(scrollregion=cv.bbox("all")))
        cv.create_window((0, 0), window=inner, anchor="nw")
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        cv.bind_all("<MouseWheel>",
                    lambda e: cv.yview_scroll(
                        int(-1*(e.delta/120)), "units"))

        for i, r in enumerate(self.results):
            c   = self.CORRECT if r["correct"] else self.WRONG
            cbg = self.CORRECT_BG if r["correct"] else self.WRONG_BG
            ico = "✓" if r["correct"] else "✗"

            row = tk.Frame(inner, bg=cbg,
                           highlightthickness=1,
                           highlightbackground=c)
            row.pack(fill="x", pady=3)

            # Left icon strip
            tk.Label(row, text=ico,
                     font=("Segoe UI", 13, "bold"),
                     bg=c, fg="white",
                     width=3, pady=10).pack(side="left", fill="y")

            body = tk.Frame(row, bg=cbg)
            body.pack(side="left", fill="x", expand=True, padx=12, pady=8)

            tk.Label(body,
                     text=f"V{i+1}.  {r['question']}",
                     font=("Segoe UI", 10, "bold"),
                     bg=cbg, fg=c,
                     wraplength=760, justify="left").pack(anchor="w")

            if not r["correct"]:
                tk.Label(body,
                         text=f"Jouw antwoord:     {r['your_answer']}",
                         font=("Segoe UI", 9),
                         bg=cbg, fg=self.WRONG).pack(anchor="w", pady=(3, 0))
                tk.Label(body,
                         text=f"Juist antwoord:      {r['right_answer']}",
                         font=("Segoe UI", 9),
                         bg=cbg, fg=self.CORRECT).pack(anchor="w")

        # ── Action buttons ──
        btn_row = tk.Frame(self.root, bg=self.BG)
        btn_row.pack(pady=14)

        tk.Button(btn_row, text="Opnieuw spelen  →",
                  font=("Segoe UI", 12, "bold"),
                  bg=self.ACCENT, fg="white",
                  activebackground=self.ACCENT_HV,
                  activeforeground="white",
                  relief="flat", padx=24, pady=11,
                  cursor="hand2", bd=0,
                  command=self._start_quiz).pack(side="left", padx=8)

        tk.Button(btn_row, text="Hoofdmenu",
                  font=("Segoe UI", 12),
                  bg=self.CARD, fg=self.TEXT,
                  activebackground=self.BORDER,
                  relief="flat",
                  highlightthickness=1,
                  highlightbackground=self.BORDER,
                  padx=24, pady=11,
                  cursor="hand2", bd=0,
                  command=self._build_welcome).pack(side="left", padx=8)

    # ──────────────────────────────────────────────────────────────────
    def _clear(self):
        for w in self.root.winfo_children():
            w.destroy()


# ─────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
