from PIL import Image
blank = Image.open("blank.png")
live = Image.open("liveround.png")
blank = blank.rotate(90,expand=True)
live = live.rotate(90,expand=True)
blank.save("blank.png")
live.save("liveround.png")