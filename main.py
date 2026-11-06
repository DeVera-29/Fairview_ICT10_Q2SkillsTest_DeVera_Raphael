from pyscript import document
#Dictionarly containing non-metal information

non_metals= {"HYDROGEN": ("H", "Hydrogen", 1, 1.008),
             "HELIUM": ("He", "Helium", 2, 4.0026),
             "CARBON": ("C", "Carbon", 6, 12.011),
             "NITROGEN": ("N", "Nitrogen", 7, 14.007),
             "OXYGEN": ("O", "Oxygen", 8, 15.999),
             "PHOSPHORUS": ("P", "Phosphorus", 15, 30.974),
             "SULFUR": ("S", "Sulfur", 16, 32.06),
             "SELENIUM": ("Se", "Selenium", 34, 78.971),
             "FLUORINE": ("F", "Fluorine", 9, 18.998),
             "CHLORINE": ("Cl", "Chlorine", 17, 35.45),
             "BROMINE": ("Br", "Bromine", 35, 79.904),
             "IODINE": ("I", "Iodine", 53, 126.90),
             "ASTATINE": ("At", "Astatine", 85, 210),
             "TELLURIUM": ("Te", "Tellurium", 52, 127.60),
             "TENESSINE": ("Ts", "Tennessine", 117, 294),
             "HELIUM": ("He", "Helium", 2, 4.0026),
             "NEON": ("Ne", "Neon", 10, 20.180),
             "ARGON": ("Ar", "Argon", 18, 39.948),
             "KRYPTON": ("Kr", "Krypton", 36, 83.798),
             "XENON": ("Xe", "Xenon", 54, 131.29),
             "RADON": ("Rn", "Radon", 86, 222),
             "OGANESSON": ("Og", "Oganesson", 118, 294)


              }
             #  ELEMENT NAME, SYMBOL, ATOMIC NUMBER, ATOMIC MASS

def search_element(e):
    #get input from html
    Element1 = document.getElementById("element1").value.upper()
    #get info from dictionary
    result = non_metals.get(Element1, ("element not found", "-", "-"))
    #display result in html
    # element name, symbol, atomic number, atomic mass
    document.getElementById("name").innerText = result[1]
    document.getElementById("symbol").innerText = result[0]
    document.getElementById("number").innerText = result[2]
    document.getElementById("mass").innerText = result[3]