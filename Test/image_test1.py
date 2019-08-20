from PIL import Image
import os
from PIL import ImageChops

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    snapshot_base = path + '/snapshot/1.png'
    snapshot_run = path + '/snapshot/3.png'
    img1= Image.open(snapshot_base)
    img2= Image.open(snapshot_run)
    diff = ImageChops.difference(img1,img2).getbbox()
    print(diff)
    #返回None，则为完全一样1
    img3 = Image.open(path + '/snapshot/8.png')
    img4 = Image.open(path + '/snapshot/9.png')
    diff1 = ImageChops.difference(img3, img4).getbbox()
    print(diff1)
