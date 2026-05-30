from art import text2art as t2a

input_text = input("Enter text to convert to ASCII art: ")
ascii_art = t2a(input_text)
print("\nHere is your ASCII art:\n")
print(ascii_art)
#Needs pip installed to work 