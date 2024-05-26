class TranspositionCipher(object):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
        
    def __init__(self, key):
        self.key = key
           

    def encrypt_message(self, message):
        shift  = self.key % 26
        message = message.lower()
        new_msg = ""
        
        for char in message:
            if char in self.alphabet:
                new_index = self.alphabet.index(char) + shift
                if new_index > len(self.alphabet) - 1:
                    new_index = new_index - len(self.alphabet)
                new_msg += self.alphabet[new_index]
            else:
                new_msg += char
                
        return new_msg
    
    def decrypt_message(self, message):
        shift  = self.key % 26
        new_msg = ""
        
        for char in message:
            if char.lower() in self.alphabet:
                new_index = self.alphabet.index(char) - shift
                new_msg += self.alphabet[new_index]
            else:
                new_msg += char
                
        return new_msg
    
