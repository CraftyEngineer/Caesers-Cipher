from alphabet import alphabets
def encrypt(original_text, shift_amount):
  cipher=""
  for i in original_text:
    if i not in alphabets:
      cipher+=i
      continue
    shifted_pos=alphabets.index(i)+shift_amount
    if shifted_pos>(len(alphabets)-1):
      shifted_pos-=26
    cipher+=alphabets[shifted_pos]
  print(cipher)

def decrypt(cipher_text, shift_amount):
  decipher=""
  for i in cipher_text:
    if i not in alphabets:
      cipher+=i
      continue
    shifted_pos=alphabets.index(i)-shift_amount
    if shifted_pos<0:
      shifted_pos+=26
    decipher+=alphabets[shifted_pos]
  print(decipher)