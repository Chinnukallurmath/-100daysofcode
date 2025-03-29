alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# -1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

#2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
def encrypt( original_text = text,  shift_amount = shift):
    ciefer_text = " "

    for letter in original_text:
        if letter in alphabet:

            shifted_position = alphabet.index(letter) + shift_amount  
            shifted_position  %=  len(alphabet)
            
            ciefer_text += alphabet[shifted_position]
        else:
            ciefer_text += letter
            

    print(f"you encoded text is {ciefer_text}")


def decrypt(original_text = text, shift_amount = shift):
    ciefer_text = " "

    for letter in original_text:
        if letter in alphabet:

            shifted_position = alphabet.index(letter) - shift_amount 
            shifted_position %=  len(alphabet)
        
            ciefer_text = alphabet[shifted_position]
        else:
            ciefer_text += letter

    print(f"you encoded text is {ciefer_text}")

#-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# -3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Choose encrypt or decrypt")
     