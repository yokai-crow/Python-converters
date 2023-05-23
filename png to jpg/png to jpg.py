
#importing the required package
from PIL import Image
  
#open image in png format
img_png = Image.open('yok.webp')
  
#The image object is used to save the image in jpg format
img_png.save('changed.jpg')