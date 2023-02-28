def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    print(" ".join(str(ord(i)-ord("a")+1)
          for i in text.lower() if i.isalpha()))


alphabet_position("The sunset sets at twelve o' clock.")
