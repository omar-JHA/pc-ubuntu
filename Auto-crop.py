# -*- coding: utf-8 -*-
import plantcv as pcv
import cv2

def trac(z):
    pass
cv2.namedWindow('threshold_binary')
cv2.createTrackbar('valor','threshold_binary',150,255,trac)

while(True):
    #lee imagen
    img,path,img_filename=pcv.readimage("/home/kubeet/pruebas/begin/lo.jpg")
    #contador dl paso de procesamiento de imagen
    device=0
    #while(True):
    val=cv2.getTrackbarPos('valor','threshold_binary')
    #se crea una imagen a escala de grises 8 bit
    device, s = pcv.rgb2gray_hsv(img, 's', device, debug=None)
    cv2.imshow("rgb2gray",s)

    # crea una imagen binaria a partir de una imagen a escala de grises
    device, threshold_binary = pcv.binary_threshold(s,val, 255, 'light', device, debug=None)
    cv2.imshow("threshold_binary",threshold_binary)

    # Create binary image from a gray image based on threshold values. Targeting light objects in the image.
    #device, masked_image = pcv.apply_mask(img,threshold_binary, 'black', device, debug=None)
    #cv2.imshow("masked-image",masked_image)
    
    #encuentro contornos de objeto Find Objects
    device, id_objects, obj_hierarchy = pcv.find_objects(img,threshold_binary, device, debug=None)
    #cv2.imshow("id_objects",id_objects)
    #print(id_objects)
    device, crop_img=pcv.auto_crop(device, img, id_objects[0],20,20,'white',debug=None)
    cv2.imshow("crop_img",crop_img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
cv2.destroyAllWindows()
"""notas"""







