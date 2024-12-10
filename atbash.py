


def uncode():
    message = []
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    flag = 0 
    for i in range(0, len(text)):
        if text[i] == "z" or text[i] == "Z":
            message.append("a")
            
        elif text[i] == "y" or text[i] == "Y":
            message.append("b")
            
        elif text[i] == "x" or text[i] == "X":
            message.append("c")
            
        elif text[i] == "w" or text[i] == "W":
            message.append("d")
            
        elif text[i] == "v" or text[i] == "V":
            message.append("e")
            
        elif text[i] == "u" or text[i] == "U":
            message.append("f")
            
        elif text[i] == "t" or text[i] == "T":
            message.append("g")
            
        elif text[i] == "s" or text[i] == "S":
            message.append("h")
            
        elif text[i] == "r" or text[i] == "R":
            message.append("i")
            
        elif text[i] == "q" or text[i] == "Q":
            message.append("j")
            
        elif text[i] == "p" or text[i] == "P":
            message.append("k")
            
        elif text[i] == "o" or text[i] == "O":
            message.append("l")
            
        elif text[i] == "n" or text[i] == "N":
            message.append("m")
            
        elif text[i] == "m" or text[i] == "M":
            message.append("n")
            
        elif text[i] == "l" or text[i] == "L":
            message.append("o")
            
        elif text[i] == "k" or text[i] == "K":
            message.append("p")
            
        elif text[i] == "j" or text[i] == "J":
            message.append("q")
            
        elif text[i] == "i" or text[i] == "I":
            message.append("r")
            
        elif text[i] == "h" or text[i] == "H":
            message.append("s")
            
        elif text[i] == "g" or text[i] == "G":
            message.append("t")
            
        elif text[i] == "f" or text[i] == "F":
            message.append("u")
            
        elif text[i] == "e" or text[i] == "E":
            message.append("v")
            
        elif text[i] == "d" or text[i] == "D":
            message.append("w")
            
        elif text[i] == "c" or text[i] == "C":
            message.append("x")
            
        elif text[i] == "b" or text[i] == "B":
            message.append("y")
            
        elif text[i] == "a" or text[i] == "A":
            message.append("z")
            
        elif text[i] == " ":
            message.append(" ")
        elif text[i] == ".":
            message.append(".")
            message.append("\n")
        
        elif text[i] == ",":
            message.append(",")                                    
        
        
        if text[i] == " ":
            flag =flag + 1 
            
        
        if flag  % 4 == 0:
            #message.append("\n")
            flag = 0                           
        
    return ''.join(message)

def encode():
    encoded_message = []
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    flag = 0
    for i in range(0, len(text)):
        if text[i] == "a" or text[i] == "A":
            encoded_message.append("z")
            
        elif text[i] == "b" or text[i] == "B":
            encoded_message.append("y")
            
        elif text[i] == "c" or text[i] == "C":
            encoded_message.append("x")
            
        elif text[i] == "d" or text[i] == "D":
            encoded_message.append("w")
            
        elif text[i] == "e" or text[i] == "E":
            encoded_message.append("v")
            
        elif text[i] == "f" or text[i] == "F":
            encoded_message.append("u")
            
        elif text[i] == "g" or text[i] == "G":
            encoded_message.append("t")
            
        elif text[i] == "h" or text[i] == "H":
            encoded_message.append("s")
            
        elif text[i] == "i" or text[i] == "I":
            encoded_message.append("r")
            
        elif text[i] == "j" or text[i] == "J":
            encoded_message.append("q")
            
        elif text[i] == "k" or text[i] == "K":
            encoded_message.append("p")
            
        elif text[i] == "l" or text[i] == "L":
            encoded_message.append("o")
            
        elif text[i] == "m" or text[i] == "M":
            encoded_message.append("n")
            
        elif text[i] == "n" or text[i] == "N":
            encoded_message.append("m")
            
        elif text[i] == "o" or text[i] == "O":
            encoded_message.append("l")
            
        elif text[i] == "p" or text[i] == "P":
            encoded_message.append("k")
            
        elif text[i] == "q" or text[i] == "Q":
            encoded_message.append("j")
            
        elif text[i] == "r" or text[i] == "R":
            encoded_message.append("i")
            
        elif text[i] == "s" or text[i] == "S":
            encoded_message.append("h")
            
        elif text[i] == "t" or text[i] == "T":
            encoded_message.append("g")
            
        elif text[i] == "u" or text[i] == "U":
            encoded_message.append("f")
            
        elif text[i] == "v" or text[i] == "V":
            encoded_message.append("e")
            
        elif text[i] == "w" or text[i] == "W":
            encoded_message.append("d")
            
        elif text[i] == "x" or text[i] == "X":
            encoded_message.append("c")
            
        elif text[i] == "y" or text[i] == "Y":
            encoded_message.append("b")
            
        elif text[i] == "z" or text[i] == "Z":
            encoded_message.append("a")
            
        elif text[i] == " ":
            encoded_message.append(" ")
            
        elif text[i] == ".":
            encoded_message.append(".")
            encoded_message.append("\n")
            
        elif text[i] == ",":
            encoded_message.append(",")                                        
        
        if text[i] == " ":
            flag += 1
            
        if flag % 4 == 0:
            # encoded_message.append("\n")  # Uncomment this line if line breaks are needed
            flag = 0                           
        
    return ''.join(encoded_message)
    
def write(text):
    try:
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Error: {e}")
  
        
    
 
def main():
    uncoded = uncode()
    write(uncoded)
    
    True
    
          
if __name__ == "__main__":
    main()