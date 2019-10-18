from PIL import Image
import colorsys
import PIL.Image as Image
import os


def cut(vx,vy):
    name1 =  "moon.jpg"
    im =Image.open(name1)

    dx = 100 #偏移量
    dy = 100
    n = 1

    x1 = 0  #從左上開始
    y1 = 0
    x2 = vx #切割大小
    y2 = vy

    #直的
    while x2 <= 3666:
        #橫的
        while y2 <= 3666:
            name3 =  str(n) + ".jpg"
            im2 = im.crop((y1, x1, y2, x2)) #切割
            im2.save(name3)
            y1 = y1 + dy
            y2 = y1 + vy
            n += 1
        x1 = x1 + dx
        x2 = x1 + vx
        y1 = 0
        y2 = vy

    print ("總共有:",end='')
    return n-1


if __name__=="__main__":

    res = cut(30,30)
    print (res)


def get_dominant_color(image):
    max_score = 0.0001
    dominant_color = None
    for count,(r,g,b) in image.getcolors(image.size[0]*image.size[1]): 
        #提高精確度
        saturation = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)[1]
        y = min(abs(r*2104+g*4130+b*802+4096+131072)>>13,235)
        y = (y-16.0)/(235-16)
 
        #忽略高亮色
        if y > 0.9:
            continue
        score = (saturation+0.1)*count
        if score > max_score:
            max_score = score
            dominant_color = (r,g,b)
    return dominant_color



a=0
tmp=0
if __name__ == '__main__':
    for i in range (1,res+1):
        image = Image.open(str(i) + '.jpg')
        image = image.convert('RGB')
        rgb = get_dominant_color(image)
        if rgb == None :
            os.remove(str(i) +".jpg")
        else:
            if(i//37!=tmp):
                a=0
            tmp = i//37
            a +=1
            f = open('RGB.txt','a')
            f.write(str(i//37+1)+"-"+str(a)+str(rgb)+"\n")
            f.close()



