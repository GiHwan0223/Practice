'''
Ideas of the Caesar cipher application
1. Type a string, then it returns an encrypted string using a Caesar cipher. 
2. If an input character is an alphabet, it shifts as 5. 
3. If an input character is not an alphabet, it returns input character.
'''

class cc:
    def caesar_cipher(text: str, shift: int = 5) -> str:
        """
        Encrypts the input text using a Caesar cipher.
        - Alphabet letters are shifted by `shift` positions.
        - Non-alphabetic characters remain unchanged.
        """
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted_char = chr((ord(char) - base + shift) % 26 + base)
                result.append(shifted_char)
            else:
                result.append(char)
        return ''.join(result)


if __name__ == "__main__":
    user_input = input("Type a string to encrypt: ")
    encrypted = cc.caesar_cipher(user_input)
    print(f"Encrypted string: {encrypted}")
