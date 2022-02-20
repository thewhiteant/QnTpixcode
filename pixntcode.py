import cv2
import matplotlib.pyplot as plt
from antapi import encrypt, decrypt
# print("_________PiXntcode________")
# print("1.En \n2.Dec \nCh:",end="")
# ch = int(input())


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
#                 img[w,h]=([ord(msg[count]),0,0])
#                 count+=1
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# nm = input("Filename(Save):")
# cv2.imwrite(nm, img)


fn = input("Open File by name: ")
img = cv2.imread(fn)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width, height, chennel = img.shape
count = 0
l = 20
out = []
for w in range(width):
    for h in range(height):
          if count < l:
                out.append(((chr(int(img[w,h].tolist()[0])))))
                count+=1

has = ("".join(out))
print(f"Dec: {has}")


