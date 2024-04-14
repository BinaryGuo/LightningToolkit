from os import getcwd
from PIL import Image
imagels = ["/home/gqx/Python/Buckshot_Roulette/assets/E.png","/home/gqx/Python/Buckshot_Roulette/assets/N.png","/home/gqx/Python/Buckshot_Roulette/assets/T.png","/home/gqx/Python/Buckshot_Roulette/assets/E.png","/home/gqx/Python/Buckshot_Roulette/assets/R.png"]
def splicing(k,n,imagelist):
    target_shape=(n*k,n)
    bg = Image.new("RGBA",target_shape,(0,0,0,0))
    for ind,i in enumerate(imagelist):
        image = Image.open(i)
        if image.mode != "RGBA":
            image.convert("RGBA")
        loc = (ind*n,0) # 放置位置
        bg.paste(image,loc)
    return bg
splicing(5,50,imagels).save("./ENTER.png")