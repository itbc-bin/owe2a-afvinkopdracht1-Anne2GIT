# Naam: Anne Manders
# Datum: 4/5/6 (tel kwijtgeraakt)
# Versie: 29-10-2017

def main(): 
    try:
        bestand = open("Alpacaklein.fa") # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand
    except IOError:
        print("File not found. Make sure the file is in the same location as your program.")
        return
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
        
    headers, seqs = lees_inhoud(bestand) 
   
    zoekwoord = input("Geef een zoekterm op: ")
    if zoekwoord != "":
        for element in headers:
            if zoekwoord in element:
                print(element)  
        for element in seqs:      
            if zoekwoord in element:
                print(element)
    print()

    try:         
        count = -1
        truecount = 0
        falselijst = []
    
        for element in seqs:
            count += 1
            
            DNA = is_dna(element)
            if DNA == True or DNA == "True":
                truecount += 1
            
            if DNA == "False" or DNA == False:
                falselijst.append(headers[count])
                
        if truecount == len(seqs):
            print("All sequences are DNA.")
        else:
            print("Not all sequences are DNA. These are not recognised as DNA: ")
            for element in falselijst:
                print(element)
    except IndexError:
        print("The lists don't have the samen length. Check lees_inhoud() for faults.")
        return
    knipt(seqs, headers)
    
"""
Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
Lever twee lijsten op:
- headers = [] met daarin alle headers
- seqs = [] met daarin alle sequenties behorend bij de headers
Hieronder vind je de return nodig om deze twee lijsten op te leveren ## SUBLIJSTEN??  --> nope!
"""
  
    
def lees_inhoud(bestands_naam):
    sequentie= ""
    headers= []
    seqs= []
    #if ">" not in bestands_naam:
        #print("The file in not in FASTA format. Make sure it is before starting the program again.")
        #return
    
    #try:
    #count = 0 
    for regel in bestands_naam:

        regel = regel.strip()
        waar = is_dna(regel)
        if waar =="False" or waar == False:
            headers.append(regel)
        for i in regel:
            
            if i == ">":# or not all([i==i.upper]):
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
    #print(count, len(seqs), len(headers)) # 1header minder is daardoor ook sequentie minder
    #if count != len(seqs):
        #print("File is not in fasta format. Make sure it is before you start the program again.")
        #return
    print(len(headers), len(seqs))
    return headers, seqs
    #except count != len(seqs):
        #print("File is not in fasta format. Make sure it is before you start the program again.")
'''if regel.startswith(">"):
            headers.append(regel)
        
        for i in regel:
            if i in range(0,9):
                if not regel.startswith(">"): 
                    headers.append(regel)
                    count += 1'''


"""
Deze functie bepaalt of de sequentie (een element uit seqs) DNA is.
Indien ja, return True
Zo niet, return False
"""
    
def is_dna(element):
    nuccount = 0
    DNA = "True"
    
    for ch in element:
        if ch in ["A", "T", "C", "G"]: 
            nuccount += 1
    if nuccount == len(element):  
        return True
    else:
        #print(nuccount, len(element))
        return False 

    
"""
Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

Deze functie bepaalt of een restrictie enzym in de sequentie (een element uit seqs) knipt.
Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
"""    
def knipt(seq, header):
    
    enzymen = open("enzymen.txt","r")
    try:
        elementcount = -1
        matchlijst = [] 
        frgmntlijst = []
        enzlijst = []
        for element in seq:     
            sublijstmatch = []  
            elementcount += 1   
            for regel in enzymen:                   
                regel = regel.replace("^", "")      
                enz, frgmnt = regel.split()
                test = is_dna(frgmnt)
                if test:
                    frgmntlijst.append(frgmnt)
                    enzlijst.append(enz)
                else:
                    print("The list of enzyms is faulty. Check it before starting the program again")
                    return

            for x in range(len(frgmntlijst)):
                if frgmntlijst[x] in element:       
                    sublijstmatch.append(enzlijst[x]) 
            matchlijst.append(sublijstmatch)
            print(elementcount, len(header))

            print(80*"-")
            print("Matches restrictieenzymen", header[elementcount], ":", matchlijst[elementcount])                                                              #print(enz, frgmnt) # komma = met spatie, plus = zonder spatie

    except IndexError:
        print()
main()
