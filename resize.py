from PIL import Image
from data import LETTERS
for l in LETTERS:
    image = Image.open(f"./{l}.png")
    resized= image.resize((50,50))
    resized.save(f"{l}.png")