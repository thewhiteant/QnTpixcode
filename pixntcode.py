import cv2
import matplotlib.pyplot as plt
<<<<<<< HEAD
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


=======
from antcrypt import encrypt, decrypt
import numpy
import keyboard






print("_________PiXntcode________")
print("1.En \n2.Dec \nCh:",end="")
ch = int(input())

if ch == 1:
    try :

        fn = input("Open File by name:")
        img = cv2.imread(fn)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        width, height, chennel = img.shape
        txt = input("Your Message: ")
        count = 0
        for w in range(width):
            for h in range(height):
                if len(txt) > count:
                    img[w, h] = ord(txt[count])
                    count += 1
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        nm = input("Save File: ")
        cv2.imwrite(nm, img)
        print(f"Your Password_Hash: {encrypt(str(count))}")
    except:
        print("Something Wrong!")


elif ch == 2:
    try:
        fn = input("Open File by name:")
        img = cv2.imread(fn)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        width, height, chennel = img.shape
        
        lo = input("PassHash: ")
        lo = decrypt(lo)
        lo = int(lo)
        countx = 0
        out = []
        for w in range(width):
            for h in range(height):
                if lo > countx:

                    out.append(chr(int(img[w, h].tolist()[0])))
                    countx += 1


        msg = "".join(out)
        print(f"Message : {msg}")
    except:
        print("Something Wrong!")

else:
    print("Nope!")
>>>>>>> parent of 341610d (.)
