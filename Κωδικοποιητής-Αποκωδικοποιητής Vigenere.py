'''
Κρυπτογραφος - Αποκρυπτογραφος
'''
import time
message = ""
keyword = ""
string = ""

charNum = [913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 931, 932, 933, 934, 935, 936, 937]
charTable = { "Α" : 0, "Β" : 1, "Γ" : 2, "Δ" : 3, "Ε" : 4, "Ζ" : 5, "Η" : 6, "Θ" : 7, "Ι" : 8, "Κ" : 9, "Λ" : 10, "Μ" : 11, "Ν" : 12, "Ξ" : 13, "Ο" : 14, "Π" : 15, "Ρ" : 16, "Σ" : 17, "Τ" : 18, "Υ" : 19, "Φ" : 20, "Χ" : 21, "Ψ" : 22, "Ω" : 23}



mode = input("Θες να κρυπτογραφησεις ενα μηνυμα ή να αποκρυπτογραφήσεις;\n----------------------------\n|1.Θέλω να κρυπτογραφήσω   |\n|2.Θέλω να αποκρυπτογραφήσω|\n----------------------------\nΕπιλογή:")
if mode == "1":
    keyword = input("Εισήγαγε το κλειδί που θα κωδικοποιήσει το μήνυμά σου σε μορφή ΧΩΡΙΣ ΣΗΜΕΙΑ ΣΤΙΞΗΣ:").upper()
    string = input("Εισήγαγε το κείμενο που θα κωδικοποιήσει το πρόγραμμα σε μορφή ΧΩΡΙΣ ΣΗΜΕΙΑ ΣΤΙΞΗΣ:\n").upper()

    keyword = keyword.replace(" ", "")
    string = string.replace(" ", "")
    
    i=0
    for char in string:
        character = charTable[char] + charTable[keyword[i]]
        if character > 23:
            character -= 24
        message += chr(charNum[character])
        i+=1
        if i == len(keyword):
            i=0
    print("Το κρυπτογραφημένο μήνυμα είναι:\n" + message +"\n(Μπορείς να το βρείς στον φάκελο που βρίσκεται το προγραμμα στο αρχείο Encrypted.txt)")	
    filee = open("Encrypted.txt", "a")
    filee.write(message)
    filee.write(" ")
    filee.write("ΚΛΕΙΔΙ:")
    filee.write(keyword)
    filee.write("\n")
    filee.close
    
elif mode == "2" :
    keyword = input("Εισήγαγε το κλειδί που θα αποκωδικοποιήσει το μήνυμά σου σε μορφή ΧΩΡΙΣ ΣΗΜΕΙΑ ΣΤΙΞΗΣ:").upper()
    string = input("Εισήγαγε το κείμενο που θα αποκωδικοποιήσει το πρόγραμμα σε μορφή ΧΩΡΙΣ ΣΗΜΕΙΑ ΣΤΙΞΗΣ:\n").upper()

    keyword = keyword.replace(" ", "")
    string = string.replace(" ", "")
    
    i=0
    for char in string:
        character = charTable[char] - charTable[keyword[i]]
        if character < 0:
            character += 24
        message += chr(charNum[character])
        i+=1
        if i == len(keyword):
            i=0
    print("Το αποκρυπτογραφημένο μήνυμα είναι:\n" + message +"\n(Μπορείς να το βρείς στον φάκελο που βρίσκεται το προγραμμα στο αρχείο Decrypted.txt)")
    filed = open("Decrypted.txt", "a")
    filed.write(message)
    filed.write(" ")
    filed.write("ΚΛΕΙΔΙ:")
    filed.write(keyword)
    filed.write("\n")
    filed.close		
	
time.sleep(8)
