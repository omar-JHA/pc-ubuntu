import plantcv as pcv

#lee imagen

img,path,img_filename=pcv.readimage("plan.jpg")

#contador dl paso de procesamiento de imagen
device=0

# Create binary image from a gray image based on threshold values. Targeting light objects in the image.
#device, threshold_light = pcv.binary_threshold(img, 36, 255, 'dark', device, debug="print")
device, h_channel=pcv.rgb2gray_hsv(img, 'h', device, debug="print")
device, threshold_binary = pcv.binary_threshold(h_channel,25, 255, 'light', device, debug='print')

#device, color_header, color_data, analysis_images= pcv.analyze_color(img, "im",threshold_binary, 256, device, debug="print", None, 'v', 'img', 300,analyze_color.png)
device, color_header, color_data, color_img = pcv.analyze_color(img,img_filename,threshold_binary, 256, device, debug="print", 'all', 'v', 'img', 300,analyze_color.png)
pcv.print_image(h_channel, "image-gray.jpg")
#pcv.print_image(threshold_light, "test-image.jpg")
"""notas"""
#si uso plot :imprime datos de la imagen no aguarda
#si uso print :imprime imagen y la aguarda con un nombre de la funcion


#si uso el light es un entorno diferente
#si uso  dark es otro entorno de la imagen
