# Naam: Anne Manders
# Datum: 4/5/6 (tel kwijtgeraakt)
# Versie: 29-10-2017

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

#inhoud = bestand.readlines()
    #print(inhoud) #inhoud klopt! 
    #lees_inhoud(bestand)


'Het programma begon met draaien om 13:24 en onderbrak ik om 13:33.'

def main(): ### bestand = open("Alpacaklein.fa", "r")
    bestand = open("Alpacaklein.fa") # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    headers, seqs = lees_inhoud(bestand) 
    #print(seqs)       
    #print(headers)
  
    zoekwoord = input("Geef een zoekterm op: ")
    for element in headers:
        if zoekwoord in element:
            if zoekwoord != "":
                print(element)  # <-- of de regel weergeven
    for element in seqs:      
        if zoekwoord in element:
            if zoekwoord != "":
                print(element)
    print()
            
    count = -1
    for element in seqs:
        count += 1
        #print(count)
        print(headers[count])
        print(is_dna(element))  # of in 1 keer

    knipt(seqs, headers)
    
"""
Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
Lever twee lijsten op:
- headers = [] met daarin alle headers
- seqs = [] met daarin alle sequenties behorend bij de headers
Hieronder vind je de return nodig om deze twee lijsten op te leveren ## SUBLIJSTEN??  --> nope!
"""
  
    
def lees_inhoud(bestands_naam):
    #bestand = open(bestands_naam, "r")
    
    import os
    import re

    #in_file=bestands_naam.readlines()      Snap niks van de commando's, maar welvwat het
    #dir,file=os.path.split(str(in_file))   zou moeten doen, maar was uiteindelijk niet
    #temp = os.path.join(dir,output)        nodig voor dit stukje code! De code beneden
    #out_file=open(temp,'w')                is die van Biopython, of iets vergelijkbaars

    sequentie= ""
    headers= []
    seqs= []

    for regel in bestands_naam:

        regel = regel.strip()
        for i in regel:
            if i == '>':               # regel.startswith(">") kan ook
                headers.append(regel)
                if sequentie:
                    seqs.append("".join(sequentie)) ## blijkbaar sneller dan .append,
                    sequentie = ""                  ## handiger bij grote bestanden
                break
            else:
                regel = regel.upper()
        
        if all([k==k.upper() for k in regel]):
            sequentie = sequentie + regel
    if sequentie:
        seqs.append("".join(sequentie))

    return headers, seqs


"""
Deze functie bepaalt of de sequentie (een element uit seqs) DNA is.
Indien ja, return True
Zo niet, return False
"""
    
def is_dna(seq):
    nuccount = 0
    for element in seq:
        for ch in element:
            if ch in ["A", "T", "C", "G"]: ## wil dat het true print boven/onder sequentie 
                nuccount += 1
        if nuccount == len(element):  #betekent alle nucleotiden a, t, c of g zijn
            return True #print("True. Het is DNA.")
        else:
            print(nuccount, len(element))
            return False #print("False. Het is geen DNA.")

    
"""
Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

Deze functie bepaalt of een restrictie enzym in de sequentie (een element uit seqs) knipt.
Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
"""    
def knipt(seq, header):
    
    enzymen = open("enzymen.txt","r")
    elementcount = -1
    matchlijst = [] #(boven) geeft nu voor alle3 dezelfde 3
    frgmntlijst = []
    enzlijst = []
    for element in seq:     # met seq[0: ] blijft enzymen van de 1e voor allemaal
        sublijstmatch = []  ##hier geeft de matchlijst ook geen inhoud,  of gaat programma niet eens verder
        elementcount += 1   ## IN element: eiwitten testen  met forloop!
        for regel in enzymen:                   #vanaf hier uit forloop element--> alleen laatste doornemen
            regel = regel.replace("^", "")      #vanaf hier in de forloop element-->alleen eerste doornemen
            enz, frgmnt = regel.split()
            frgmntlijst.append(frgmnt)
            enzlijst.append(enz)
        #print(len(frgmntlijst), frgmntlijst)   #zijn even lang
        #print(len(enzlijst), enzlijst)
        for x in range(len(frgmntlijst)):
            if frgmntlijst[x] in element:       ## geeft voor de sequenties dezelfde enzymen aan, die van 1e!
                sublijstmatch.append(enzlijst[x]) 
        matchlijst.append(sublijstmatch)

        print(80*"-")
        print("Matches restrictieenzymen", header[elementcount], ":", matchlijst[elementcount])                                                              #print(enz, frgmnt) # komma = met spatie, plus = zonder spatie


main()
