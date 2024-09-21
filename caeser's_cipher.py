import functions as func

choice=True
while choice:
  direction=input("Type encode to encrypt and decode to decrypt: \n").lower()
  text=input("Enter your message: \n")
  shift = int(input("Type the shift number: "))
  if direction=="encode":
    func.encrypt(text,shift)
  elif direction=="decode":
    func.decrypt(text, shift)
  forward=input("Do you want to do it again?").lower()
  if forward=="yes":
    choice=True
  else:
    choice=False


