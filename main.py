
# def incrypt(message,shift):
#   z=""
#   message = message.lower().replace(" ", "")
#   for i in message:
#     z+=(chr(ord(i) + shift))
#   print(f"the encoded message is {z}")

# def decrypt(encrypt_message,back_shift):
#   m=""
#   encrypt_message = encrypt_message.lower().replace(" ", "")
#   for i in encrypt_message:
#     m+=(chr(ord(i) - back_shift))
#   print(f"the decoded message is {m}")   

# from replit import clear
# import c_logo
# print(c_logo.logo)
# print("use '_' instead of spaces")
# u_continue= True
# while u_continue:
#  sol=input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
#  if sol=="encode":
#    message=input("enter message to encrypt: ")
#    shift=int(input("enter shifting digit: "))
#    clear()
#    shift=shift % 26
#    incrypt(message,shift)
#  elif sol=="decode":
#    encrypt_message=input("enter message to decrypt: ")
#    back_shift=int(input("enter shifting digit: "))
#    clear()
#    back_shift=back_shift % 26
#    decrypt(encrypt_message,back_shift)
#  ok=input("type 'yes' to restart and 'no' to exit:\n")
#  if ok=="yes":
#    u_continue=True
#    clear()
#  elif ok=='no':
#    u_continue=False
#    clear()
#    print("Thank you for using!")
