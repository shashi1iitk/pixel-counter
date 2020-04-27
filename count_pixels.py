import cv2
import numpy as np
import os
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'File Name')
sheet1.write(0, 1, 'White %')
sheet1.write(0, 2, 'Orange %')
r = 1
directory = "Fedex"
for path, subdirnames, filenames in os.walk(directory):
    for filename in filenames:

        img_path = os.path.join(path, filename)
        print("img_name:", filename)
        test_img = cv2.imread(img_path)

        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rows,cols = img.shape

        pixels = []

        for i in range(rows):
          for j in range(cols):
             pixels.append(img[i,j])

        pixels = list(dict.fromkeys(pixels))

        pixels.sort()
        size = len(pixels)
        i = 0
        j = 0

        sum = 0
        for i in range(0, size-1):
            sum += pixels[i]

        threshold = int((int(pixels[0]) +int(pixels[size-1]))*0.5)
        threshold  = int(sum/size)

        orange = 0
        white = 0

        for i in range(rows):
          for j in range(cols):
              if(img[i,j] > threshold):
                  white+=1;
              else:
                  orange+=1;

        white_p = int((white*100)/(white+orange))
        # white_p = int(str(round(white_p, 2)))
        orange_p = 100 - white_p
        print(white_p)

        sheet1.write(r, 0, filename)
        sheet1.write(r, 1, white_p)
        sheet1.write(r, 2, orange_p)
        r+=1
        print(orange_p)

wb.save('Fedex.xls')