import speech_recognition as sr
from gtts import gTTS

class sound_encryption_decryption_program:
    def __init__(self):
        self.codes = {'a': 'z', 'b': 'x', 'c': 'y', 'd': 's', 'e': 'u', 'f': 'a', 'g': 'e', 'h': 'c', 'i': 'k',
                      'j': 'r', 'k': 'n', 'l': 'g', 'm': 'd', 'n': 'l', 'o': 'm', 'p': 't', 'q': 'f', 'r': 'i',
                      's': 'h', 't': 'o', 'u': 'j', 'v': 'p', 'w': 'v', 'x': 'b', 'y': 'w', 'z': 'q'}
        self.list_1 = []
        self.list_2 = []
        self.r = sr.Recognizer()
        self.dec1 =[]
        self.dec2 = []
        self.List = []

    def encryption(self):
        with sr.Microphone() as source:
            print("speak......")
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            try:
                Text = self.r.recognize_google(audio)
                print("after converting:", Text.lower())

                #encryption code

                x = Text.split(" ")
                inverse_text = x[::-1]
                z = ""
                for i in range(0, len(inverse_text)):
                    string = "".join(reversed(inverse_text[i]))
                    z += string
                    z += " "
                for i in z:
                    self.list_1.append(i)
                for i in range(0, len(self.list_1)):
                    for j in self.list_1[i]:
                        if j != ' ':

                            for key in self.codes.keys():
                                if key in j:
                                    self.list_2.append(self.codes.get(key))
                        else:
                            self.list_2.append("/s")
                encrypt = " "
                for i in range(0, len(self.list_2)):
                    if self.list_2[i] == "/s":
                        encrypt += " "
                    else:
                        encrypt += self.list_2[i]
                print("your encrypted text:", encrypt) #file me jaye gi
                file = open("encrypt.txt", 'w')
                file.write(encrypt)

                try:
                    tts = gTTS(text=encrypt, lang='en')
                    f_name = 'voice.mp3'
                    tts.save(f_name)
                    print("working")
                except:
                    print("not saving")
            except:
                print("could not recognize your voice")


    def decryption_of_soundfile(self):
        z=[]
        f = open("encrypt.txt", "r")
        for i in f:
           for x in i:
               z.append(x)
        print(z)

        for i in range(0, len(z)):
            for j in z[i]:
                if j != " ":
                    if j in self.codes.values():
                        self.dec1.append(list(self.codes.keys())[list(self.codes.values()).index(z[i])])


                else:
                    self.dec1.append("/s")
        z = ""
        for i in range(0, len(self.dec1)):
            if self.dec1[i] == "/s":
                z += " "
            else:
                z += self.dec1[i]
        y = z.split(" ")
        for i in y:
            self.dec2.append(i)
        rev = self.dec2[::-1]
        rever = ""
        for i in range(0, len(rev)):
            string = "".join(reversed(rev[i]))
            rever += string
            rever += " "
        print("decrypted text:", rever)
        try:
            tts = gTTS(text=rever, lang='en')
            f_name = 'decryptedfile.mp3'
            tts.save(f_name)
            print("working")
        except:
            print("file has not been created")



    

        


ob = sound_encryption_decryption_program()
ob.encryption()
ob.decryption_of_soundfile()





