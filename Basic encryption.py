import math, re
number_dictionary = {"0":"00000000", "1":"00011011", "2":"00011100", "3":"00011101", "4":"00011110", "5":"00011111", "6":"00100000", "7":"00111011", "8":"00111100", "9":"00111101"}
dictionary = {".":"111110", "0":"000000", "1":"011011", "2":"011100", "3":"011101", "4":"011110", "5":"011111", "6":"100000", "7":"111011", "8":"111100", "9":"111101", " ":"111111", "A":"000001", "B":"000010", "C":"000011", "D":"000100", "E":"000101", "F":"000110", "G":"000111", "H":"001000", "I":"001001", "J":"001010", "K":"001011", "L":"001100", "M":"001101", "N":"001110", "O":"001111", "P":"010000", "Q":"010001", "R":"010010", "S":"010011", "T":"010100", "U":"010101", "V":"010110", "W":"010111", "X":"011000", "Y":"011001", "Z":"011010", "a":"100001", "b":"100010", "c":"100011", "d":"100100", "e":"100101", "f":"100110", "g":"100111", "h":"101000", "i":"101001", "j":"101010", "k":"101011", "l":"101100", "m":"101101", "n":"101110", "o":"101111", "p":"110000", "q":"110001", "r":"110010", "s":"110011", "t":"110100", "u":"110101", "v":"110110", "w":"110111", "x":"111000", "y":"111001", "z":"111010"}
inverse_dictionary = {"111110":".", "000000":"0", "011011":"1", "011100":"2", "011101":"3", "011110":"4", "011111":"5", "100000":"6", "111011":"7", "111100":"8", "111101":"9", "111111":" ", "000001":"A", "000010":"B", "000011":"C", "000100":"D", "000101":"E", "000110":"F", "000111":"G", "001000":"H", "001001":"I", "001010":"J", "001011":"K", "001100":"L", "001101":"M", "001110":"N", "001111":"O", "010000":"P", "010001":"Q", "010010":"R", "010011":"S", "010100":"T", "010101":"U", "010110":"V", "010111":"W", "011000":"X", "011001":"Y", "011010":"Z", "100001":"a", "100010":"b", "100011":"c", "100100":"d", "100101":"e", "100110":"f", "100111":"g", "101000":"h", "101001":"i", "101010":"j", "101011":"k", "101100":"l", "101101":"m", "101110":"n", "101111":"o", "110000":"p", "110001":"q", "110010":"r", "110011":"s", "110100":"t", "110101":"u", "110110":"v", "110111":"w", "111000":"x", "111001":"y", "111010":"z"}
de_inverse_dictionary = {".":"111110", "0":"000000", "1":"011011", "2":"011100", "3":"011101", "4":"011110", "5":"011111", "6":"100000", "7":"111011", "8":"111100", "9":"111101", " ":"111111", "A":"000001", "B":"000010", "C":"000011", "D":"000100", "E":"000101", "F":"000110", "G":"000111", "H":"001000", "I":"001001", "J":"001010", "K":"001011", "L":"001100", "M":"001101", "N":"001110", "O":"001111", "P":"010000", "Q":"010001", "R":"010010", "S":"010011", "T":"010100", "U":"010101", "V":"010110", "W":"010111", "X":"011000", "Y":"011001", "Z":"011010", "a":"100001", "b":"100010", "c":"100011", "d":"100100", "e":"100101", "f":"100110", "g":"100111", "h":"101000", "i":"101001", "j":"101010", "k":"101011", "l":"101100", "m":"101101", "n":"101110", "o":"101111", "p":"110000", "q":"110001", "r":"110010", "s":"110011", "t":"110100", "u":"110101", "v":"110110", "w":"110111", "x":"111000", "y":"111001", "z":"111010"}
de_dictionary = {"111110":".", "000000":"0", "011011":"1", "011100":"2", "011101":"3", "011110":"4", "011111":"5", "100000":"6", "111011":"7", "111100":"8", "111101":"9", "111111":" ", "000001":"A", "000010":"B", "000011":"C", "000100":"D", "000101":"E", "000110":"F", "000111":"G", "001000":"H", "001001":"I", "001010":"J", "001011":"K", "001100":"L", "001101":"M", "001110":"N", "001111":"O", "010000":"P", "010001":"Q", "010010":"R", "010011":"S", "010100":"T", "010101":"U", "010110":"V", "010111":"W", "011000":"X", "011001":"Y", "011010":"Z", "100001":"a", "100010":"b", "100011":"c", "100100":"d", "100101":"e", "100110":"f", "100111":"g", "101000":"h", "101001":"i", "101010":"j", "101011":"k", "101100":"l", "101101":"m", "101110":"n", "101111":"o", "110000":"p", "110001":"q", "110010":"r", "110011":"s", "110100":"t", "110101":"u", "110110":"v", "110111":"w", "111000":"x", "111001":"y", "111010":"z"}
de_number_dictionary = {"00000000":"0", "00011011":"1", "00011100":"2", "00011101":"3", "00011110":"4", "00011111":"5", "00100000":"6", "00111011":"7", "00111100":"8", "00111101":"9"}
encrypt_message = []
de_encrypted = []
bin_de_encrypted = []
div_6 = False
div_8 = False
option_correct = False

while option_correct == False:
    option = input("Do you want to encrypt or decrypt?\t")
    if option == "encrypt" or option == "decrypt":
        option_correct = True
    else:
        print("Invalid Input")
key = input("Please enter the encryption key\t")
text_input = input("Please enter the message to translate\t")

def code(inp):
    global out
    out = []
    Split = (' '.join(x for x in inp))
    SplitList = Split.split(" ")
    for i in range(int(SplitList.count("")/2)):
        SplitList.remove("")
        SplitList.insert(SplitList.index(""), " ")
        SplitList.remove("")
    for i in range(len(SplitList)):
        number = dictionary[SplitList[i]]
        out.append(number)
    out = "".join(out)

def number_code(inp):
    global out
    out = []
    Split = (' '.join(x for x in inp))
    SplitList = Split.split(" ")
    for i in range(int(SplitList.count("")/2)):
        SplitList.remove("")
        SplitList.insert(SplitList.index(""), " ")
        SplitList.remove("")
    for i in range(len(SplitList)):
        number = number_dictionary[SplitList[i]]
        out.append(number)
    out = "".join(out)

def de_code(inp):
    global out
    out = []
    Split = (' '.join(x for x in inp))
    SplitList = Split.split(" ")
    for i in range(int(SplitList.count("")/2)):
        SplitList.remove("")
        SplitList.insert(SplitList.index(""), " ")
        SplitList.remove("")
    for i in range(len(SplitList)):
        number = de_dictionary[SplitList[i]]
        out.append(number)
    out = "".join(out)

if option == "encrypt":
    text_input = "H"+text_input
    code(text_input)
    message = str(int(out, 2))
    code(key)
    bin_key = str(int(out, 2))
    bin_key = bin_key*(math.ceil(len(message)/len(bin_key)))
    bin_encrypted = str(int(bin_key)+int(message))
    number_code(bin_encrypted)
    while div_6 == False:
        len_div_6 = len(out)/6
        if len_div_6.is_integer():
            div_6 = True
        else:
            out = out+"0"
    encrypted_split = re.findall('......?', out)
    for i in range(len(encrypted_split)):
        encrypt_message.append(inverse_dictionary[encrypted_split[i]])
    encrypt_message = "".join(encrypt_message)
    print("["+encrypt_message+"]")

else:
    encrypted_split = re.findall('.?', text_input)
    for i in range(len(encrypted_split)-1):
        de_encrypted.append(de_inverse_dictionary[encrypted_split[i]])
    de_encrypted = "".join(de_encrypted)
    de_encrypted_split = re.findall('........?', de_encrypted)
    print(de_encrypted_split)
    for i in range(len(de_encrypted_split)):
        bin_de_encrypted.append(de_number_dictionary[de_encrypted_split[i]])
    bin_de_encrypted = "".join(bin_de_encrypted)
    code(key)
    bin_key = str(int(out, 2))
    bin_key = bin_key*(math.ceil(len(bin_de_encrypted)/len(bin_key)))
    binary_de_encrypted = str(int(bin_de_encrypted)-int(bin_key))
    print(bin(int(binary_de_encrypted)))
    binary_de_encrypted = (str("00"+bin(int(binary_de_encrypted))[2:]))
    binary_de_encrypted_split = re.findall('......?', binary_de_encrypted)
    out = []
    for i in range(len(binary_de_encrypted_split)):
        number = inverse_dictionary[binary_de_encrypted_split[i]]
        out.append(number)
    decrypted_message = "".join(out)
    decrypted_message = decrypted_message[1:]
    print(decrypted_message)
#

