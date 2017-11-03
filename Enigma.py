'''
Κρυπτογραφος - Αποκρυπτογραφος
'''
import time

message = ""
string = ""

charNum = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]
plugAlpha = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]
charTable = { "Α" : 0, "Β" : 1, "Γ" : 2, "Δ" : 3, "Ε" : 4, "Ζ" : 5, "Η" : 6, "Θ" : 7, "Ι" : 8, "Κ" : 9, "Λ" : 10, "Μ" : 11, "Ν" : 12, "Ξ" : 13, "Ο" : 14, "Π" : 15, "Ρ" : 16, "Σ" : 17, "Τ" : 18, "Υ" : 19, "Φ" : 20, "Χ" : 21, "Ψ" : 22, "Ω" : 23}
plugBoard = dict()
reflector = ["Ε", "Κ", "Μ", "Ζ", "Λ", "Γ", "Δ", "Ζ", "Ι", "Β", "Λ", "Ε", "Κ", "Α" , "Η", "Μ", "Θ", "Δ", "Α", "Ι", "Β", "Η", "Γ",  "Θ"]
plugs=0

aAlpha = ["Ε", "Κ", "Μ", "Ζ", "Λ", "Ξ", "Δ", "Ψ", "Φ", "Ω", "Ν", "Τ", "Ο", "Υ" , "Η", "Χ", "Σ", "Π", "Α", "Ι", "Β", "Ρ", "Γ",  "Θ"]





class gear:
    def __init__(self, letter, changer, alphabet):
        self.letter = letter
        self.changer = changer
        self.alphabet = alphabet
        self.realalpha = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]
        self.set()
    def shift(self, other = None , other2 = None):
        if self.realalpha[0] == self.changer and other != None:
            other.shift(other2)
        self.alphabet = self.alphabet[-23:] + self.alphabet[:-23]
        self.realalpha = self.realalpha[-23:] + self.realalpha[:-23]
        
		    
    def __str__(self):
        return str(self.alphabet) + " " + str(self.realalpha)


    def set(self):
        while self.letter != self.realalpha[0]:
            self.shift()

    def passLeft(self,character):
        if isinstance(character, str):    
            character = charTable[character]
        character = self.alphabet[character]
        for index, i in enumerate(self.realalpha):
            if i == character:
                return index

    def passRight(self, num):
        character = self.realalpha[num]
        for index, i in enumerate(self.alphabet):
            if i == character:
                return index
	


def passLeftAll(a, b, c, char):
    return c.passLeft(b.passLeft(a.passLeft(char)))

def reflect(num):
    char = reflector[num]
    for index, i in enumerate(reflector):
        if i == char and num!=index:
            return index

def passRightAll(a, b, c, char):
    return a.passRight(b.passRight(c.passRight(char)))

def encode(a, b, c, char):
    a.shift(b,c)
    return charNum[passRightAll(a, b, c, reflect(passLeftAll(a, b, c, char)))]
				
    
A=gear("Π","Τ", aAlpha)

B=gear("Υ", "Ρ", aAlpha)

C=gear("Ρ", "Φ", aAlpha)

gears ={ "1" : A, "2": B, "3": C}
firstGear = None
secondGear = None
thirdGear = None
#Test Body

print("Καλωσόρισες στον προσομοιωτη της μηχανης Enigma\n")
print("Θα σου ζητηθει να εισαγεις την σειρα με την οποια θα παραταξουμε τα γραναζια στην μηχανη\n")
print("Τα υπάρχοντα γραναζια ειναι τα εξής:\n1.A\n2.B\n3.C\n")
firstGear=gears[input("Πρωτο γραναζι:")]
secondGear=gears[input("Δεύτερο γρανάζι:")]
thirdGear=gears[input("Τρίτο γρανάζι:")]
threeLW = list(input("Εισηγαγε μια λεξη τριων γραμματων στην σειρα(Π.χ. ΗΙΡ):").upper())

firstGear.letter = threeLW[2]
secondGear.letter = threeLW[1]
thirdGear.letter = threeLW[0]
firstGear.set()
secondGear.set()
thirdGear.set()

while True:
    mode=input("Θές να προσθέσεις μια σύνδεση μεταξύ γραμμάτων στο PlugBoard?\n1.Ναί  |  2.Όχι\nΕπιλογή:")
    if mode=="2":
        break
    elif mode=="1":
        for index, i in enumerate(plugAlpha):
            print(index+1, ".", i, sep ="")
        plugCharA = int(input("Εισηγαγε τον πρώτο χαρακτηρα:")) - 1
        firstc=plugAlpha[plugCharA]
        plugAlpha.remove(plugAlpha[plugCharA])
        for index, i in enumerate(plugAlpha):
            print(index+1, ".", i, sep ="")
        plugCharB = int(input("Εισηγαγε τον δεύτερο χαρακτηρα:")) - 1
        secondc=plugAlpha[plugCharB]
        plugAlpha.remove(plugAlpha[plugCharB])
        plugBoard[firstc] = secondc
        plugBoard[secondc] = firstc
        plugs+=1
    if plugs==6:
        print("You have the max amount of plugs on the PlugBoard!!")
        break
for i in plugAlpha:
    plugBoard[i]=i


string = input("Εισήγαγε το κείμενο που θα κωδικοποιήσει το πρόγραμμα σε μορφή ΧΩΡΙΣ ΣΗΜΕΙΑ ΣΤΙΞΗΣ:\n").upper()

for i in string:
    if i!=" ":
        message += plugBoard[encode(firstGear,secondGear,thirdGear, plugBoard[i])]
    else:
        message += " "

print(message)



time.sleep(10)

