import cv2
import matplotlib.pyplot as plt
from antcrypt import encrypt, decrypt
import numpy






print("_________PiXntcode________")
print("1.En \n2.Dec \nCh:",end="")
ch = int(input())

if ch == 1:


    fn = input("Open File by name: ")
    data =  input("Your Message: ")
    msg = encrypt(data)
    img = cv2.imread(fn)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    w, h, c = img.shape
    count = 0
    for ht in range(w-3):
        if ht % 10 == 0:
            img[ht, int(h/2)] = numpy.array([ord(msg[count]), 255, 255])
            count += 1
        elif count == len(msg):
            img[ht+10, int(h/2)] = numpy.array([126, 255, 255])
            break


    plt.imshow(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    nm = input("Filename(Save):")
    cv2.imwrite(nm, img)

elif ch == 2:

    fn = input("Open File by name:")
    img = cv2.imread(fn)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    w, h, c = img.shape
    collector = []
    for ht in range(w-3):
        if ht % 10 == 0:
            if chr(int((img[ht+1, int(h/2)]).tolist()[0])) != "~":
                data = int((img[ht, int(h/2)]).tolist()[0])
                collector.append(chr(data))
            else:
                break

    has = ("".join(collector))
    res = decrypt(has)
    print(f"Dec: {res}")

else:
    print("Nope!")