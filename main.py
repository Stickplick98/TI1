from tkinter import Tk     #pip install tk
from tkinter.filedialog import askopenfilename
import cv2 as cv

Tk().withdraw() 
filename = askopenfilename(initialdir = "C:\\TraitementImages3eme\\Images")

img = cv.imread(filename,cv.IMREAD_COLOR)  # BGR
cv.imshow("Plages sans traitement",img)

if img is None:
    print("error opening image")
else:
    b,g,r = cv.split(img)
    if b is None and g is None and r is None:
        print("error opening image")
    else:
        img_blurB = cv.blur(b, (5, 5))
        img_blurG = cv.blur(g, (5, 5))
        img_blurR = cv.blur(r, (5, 5))
        imgfinale = cv.merge((img_blurB, img_blurG, img_blurR))

        cv.imwrite("ImageFinale.png", imgfinale)

        cv.imshow("Plages avec traitement", imgfinale)
        cv.waitKey(0)
        cv.destroyAllWindows()
