from warnings import catch_warnings
import cv2
import matplotlib.pyplot as plt
from antapi import encrypt, decrypt



print("____Only Png Supported____")
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
    for wt in range(w):
        for ht in range(h):
            if len(msg)> count:
                img[wt,ht] = [int(ord(msg[count])),0,0]
                count += 1
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    nm = input("Filename(Save):")
    print(f"Password_hash:{encrypt(str(count))}")
    cv2.imwrite(f"{nm}.png", img)

elif ch == 2:
    try:
        fn = input("Open File by name:")
        img = cv2.imread(fn)
        n = input("PasswordHash: ")
        n = decrypt(n)
        n = int(n)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        w, h, c = img.shape
        collector = []
        countx = 0
        for wt in range(w):
            for ht in range(h):
                if n > countx:    
                    collector.append(chr(int(img[wt,ht].tolist()[0])))
                    countx +=1
        has = ("".join(collector))
        res = decrypt(has)
        print(f"Msg: {res}")
    except:
        print("Some error Happend")
else:
    print("Nope!")


