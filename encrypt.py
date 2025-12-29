from PIL import Image

# image open karo
img = Image.open("image.jpg")
pixels = img.load()

width, height = img.size
key = 50   # secret key

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (r + key) % 256, (g + key) % 256, (b + key) % 256

img.save("encrypted.png")
print("Image encrypted successfully")
