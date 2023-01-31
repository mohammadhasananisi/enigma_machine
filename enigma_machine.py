class Enigma:
    rotors = ("I","II","III")
    reflector = "UKW-B"
    ringSettings = "ABC"
    ringPositions = "DEF"
    plugboard = "AT BS DE FM IR KN LZ OW PV XY"
    def __init__(self, rotors, reflector, ringSettings, ringPositions, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.ringSettings = ringSettings
        self.ringPositions = ringPositions
        self.plugboard = plugboard



    def caesarShift(self, str, amount):
        output = ""

        for i in range(0,len(str)):
            c = str[i]
            code = ord(c)
            if ((code >= 65) and (code <= 90)):
                c = chr(((code - 65 + amount) % 26) + 65)
            output = output + c
        
        return output

    def encode(self, plaintext):
        rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
        rotor1Notch = "Q"
        rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
        rotor2Notch = "E"
        rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        rotor3Notch = "V"
        rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
        rotor4Notch = "J"
        rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
        rotor5Notch = "Z" 
        
        rotorDict = {"I":rotor1,"II":rotor2,"III":rotor3,"IV":rotor4,"V":rotor5}
        rotorNotchDict = {"I":rotor1Notch,"II":rotor2Notch,"III":rotor3Notch,"IV":rotor4Notch,"V":rotor5Notch}  
        
        reflectorB = {"A":"Y","Y":"A","B":"R","R":"B","C":"U","U":"C","D":"H","H":"D","E":"Q","Q":"E","F":"S","S":"F","G":"L","L":"G","I":"P","P":"I","J":"X","X":"J","K":"N","N":"K","M":"O","O":"M","T":"Z","Z":"T","V":"W","W":"V"}
        reflectorC = {"A":"F","F":"A","B":"V","V":"B","C":"P","P":"C","D":"J","J":"D","E":"I","I":"E","G":"O","O":"G","H":"Y","Y":"H","K":"R","R":"K","L":"Z","Z":"L","M":"X","X":"M","N":"W","W":"N","Q":"T","T":"Q","S":"U","U":"S"}
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rotorANotch = False
        rotorBNotch = False
        rotorCNotch = False
        
        if self.reflector=="UKW-B":
            reflectorDict = reflectorB
        else:
            reflectorDict = reflectorC
        
        #A = Left,  B = Mid,  C=Right 
        rotorA = rotorDict[self.rotors[0]]
        rotorB = rotorDict[self.rotors[1]]
        rotorC = rotorDict[self.rotors[2]]
        rotorANotch = rotorNotchDict[self.rotors[0]]
        rotorBNotch = rotorNotchDict[self.rotors[1]]
        rotorCNotch = rotorNotchDict[self.rotors[2]]
        
        rotorALetter = self.ringPositions[0]
        rotorBLetter = self.ringPositions[1]
        rotorCLetter = self.ringPositions[2]
        
        rotorASetting = self.ringSettings[0]
        offsetASetting = alphabet.index(rotorASetting)
        rotorBSetting = self.ringSettings[1]
        offsetBSetting = alphabet.index(rotorBSetting)
        rotorCSetting = self.ringSettings[2]
        offsetCSetting = alphabet.index(rotorCSetting)
        
        rotorA = self.caesarShift(rotorA,offsetASetting)
        rotorB = self.caesarShift(rotorB,offsetBSetting)
        rotorC = self.caesarShift(rotorC,offsetCSetting)
        
          
        if offsetASetting>0:
            rotorA = rotorA[26-offsetASetting:] + rotorA[0:26-offsetASetting]
        if offsetBSetting>0:
            rotorB = rotorB[26-offsetBSetting:] + rotorB[0:26-offsetBSetting]
        if offsetCSetting>0:
            rotorC = rotorC[26-offsetCSetting:] + rotorC[0:26-offsetCSetting]

        ciphertext = ""
        
        plugboardConnections = self.plugboard.upper().split(" ")
        plugboardDict = {}
        for pair in plugboardConnections:
            if len(pair)==2:
                plugboardDict[pair[0]] = pair[1]
                plugboardDict[pair[1]] = pair[0]
        
        plaintext = plaintext.upper()  
        for letter in plaintext:
            encryptedLetter = letter  
            
            if letter in alphabet:
            #Rotate Rotors - This happens as soon as a key is pressed, before encrypting the letter!
                rotorTrigger = False
                #Third rotor rotates by 1 for every key being pressed
                if rotorCLetter == rotorCNotch:
                    rotorTrigger = True 
                rotorCLetter = alphabet[(alphabet.index(rotorCLetter) + 1) % 26]
                #Check if rotorB needs to rotate
                if rotorTrigger:
                    rotorTrigger = False
                    if rotorBLetter == rotorBNotch:
                        rotorTrigger = True 
                    rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
            
                    #Check if rotorA needs to rotate
                    if (rotorTrigger):
                        rotorTrigger = False
                        rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]
                        
                else:
                    #Check for double step sequence!
                    if rotorBLetter == rotorBNotch:
                        rotorBLetter = alphabet[(alphabet.index(rotorBLetter) + 1) % 26]
                        rotorALetter = alphabet[(alphabet.index(rotorALetter) + 1) % 26]
                    
                #Implement plugboard encryption!
                if letter in plugboardDict.keys():
                    if plugboardDict[letter]!="":
                        encryptedLetter = plugboardDict[letter]
                
                #Rotors & Reflector Encryption
                offsetA = alphabet.index(rotorALetter)
                offsetB = alphabet.index(rotorBLetter)
                offsetC = alphabet.index(rotorCLetter)

                # Wheel 3 Encryption
                pos = alphabet.index(encryptedLetter)
                let = rotorC[(pos + offsetC)%26]
                pos = alphabet.index(let)
                encryptedLetter = alphabet[(pos - offsetC +26)%26]
                
                # Wheel 2 Encryption
                pos = alphabet.index(encryptedLetter)
                let = rotorB[(pos + offsetB)%26]
                pos = alphabet.index(let)
                encryptedLetter = alphabet[(pos - offsetB +26)%26]
                
                # Wheel 1 Encryption
                pos = alphabet.index(encryptedLetter)
                let = rotorA[(pos + offsetA)%26]
                pos = alphabet.index(let)
                encryptedLetter = alphabet[(pos - offsetA +26)%26]
                
                # Reflector encryption!
                if encryptedLetter in reflectorDict.keys():
                    if reflectorDict[encryptedLetter]!="":
                        encryptedLetter = reflectorDict[encryptedLetter]
                
                #Back through the rotors 
                # Wheel 1 Encryption
                pos = alphabet.index(encryptedLetter)
                let = alphabet[(pos + offsetA)%26]
                pos = rotorA.index(let)
                encryptedLetter = alphabet[(pos - offsetA +26)%26] 
                
                # Wheel 2 Encryption
                pos = alphabet.index(encryptedLetter)
                let = alphabet[(pos + offsetB)%26]
                pos = rotorB.index(let)
                encryptedLetter = alphabet[(pos - offsetB +26)%26]
                
                # Wheel 3 Encryption
                pos = alphabet.index(encryptedLetter)
                let = alphabet[(pos + offsetC)%26]
                pos = rotorC.index(let)
                encryptedLetter = alphabet[(pos - offsetC +26)%26]
                
                #Implement plugboard encryption!
                if encryptedLetter in plugboardDict.keys():
                    if plugboardDict[encryptedLetter]!="":
                        encryptedLetter = plugboardDict[encryptedLetter]

            ciphertext = ciphertext + encryptedLetter
        
        return ciphertext
