import cv2
import matplotlib.pyplot as plt
from antapi import encrypt, decrypt
import numpy





# print("_________PiXntcode________")
# print("1.En \n2.Dec \nCh:",end="")
# ch = int(input())

# if ch == 1:


# fn = input("Open File by name: ")
# data =  input("Your Message: ")
# msg = data
# img = cv2.imread(fn)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# width, height, chennel = img.shape
# count = 0
# for w in range(width):
#     for h in range(height):
#           if count < len(msg):
#                 img[w,h]=(ord(msg[count]))
#                 count+=1

# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# nm = input("Filename(Save):")
# cv2.imwrite(nm, img)

# elif ch == 2:



fn = input("Open File by name: ")
img = cv2.imread(fn)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width, height, chennel = img.shape
count = 0
l = 20
for w in range(width):
    for h in range(height):
          if count < l:
                print(img[w,h])
                count+=1


# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# nm = input("Filename(Save):")
# cv2.imwrite(nm, img)
#     has = ("".join(collector))
#     res = decrypt(has)
#     print(f"Dec: {res}")
# else:
#     print("Nope!")

