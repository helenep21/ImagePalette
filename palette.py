from PIL import Image
import glob
import colorific

def get_img(address):
    origin = Image.open(address)
    return origin

def get_img2(path,filename):
    address=str(path+"/"+filename)
    origin = Image.open(address)
    return origin

def resize(origin):
    o_size = origin.size
    if o_size[0] > o_size[1]:
        ratio = o_size[0] / 320
    else:
        ratio = o_size[1] / 320
    new_w = int(o_size[0] / ratio)
    new_h = int(o_size[1] / ratio)
    img = origin.resize((new_w,new_h))
    return img

def empty_palette(origin):
    size=origin.size
    w=int(size[0])
    h=int(size[1]/10)
    empty = Image.new("RGB",(w,h),"#0000FF")
    return empty

def get_colors(img):
    palette=colorific.extract_colors(img,min_prominence=0.001,min_saturation=0)
    color1=palette.colors[0].value
    color2=palette.colors[1].value
    color3=palette.colors[2].value
    color4=palette.colors[3].value
    color5=palette.colors[4].value
    colors=[color1,color2,color3,color4,color5]
    return colors

def save_palette(empty,color1,color2,color3,color4,color5):
    pal_w=empty.size[0]
    pal_h=empty.size[1]
    pixels=empty.load()
    for i in range(0,pal_w):
        if i < (int(pal_w/5)):
            for j in range(0,pal_h):
                pixels[i,j]=color1
        elif i < (int(2*(pal_w/5))):
            for j in range(0,pal_h):
                pixels[i,j]=color2
        elif i < (int(3*(pal_w/5))):
            for j in range(0,pal_h):
                pixels[i,j]=color3
        elif i < (int(4*(pal_w/5))):
            for j in range(0,pal_h):
                pixels[i,j]=color4
        elif i < (int(5*(pal_w/5))):
            for j in range(0,pal_h):
                pixels[i,j]=color5
    return empty

def img_final(origin,empty):
    size1=origin.size
    size2=empty.size
    w=int(size1[0])
    h=int(size1[1]+size2[1])
    final = Image.new("RGB",(w,h),"#0000FF")
    final.paste(origin,(0,0))
    final.paste(empty,(0,h-size2[1]))
    return final

def save_final(final,destination):
    final.save(destination)
    final.show()