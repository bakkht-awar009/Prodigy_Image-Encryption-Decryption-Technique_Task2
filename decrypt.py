from PIL import Image

img = Image.open("encrypted.png")
pixels = img.load()

width, height = img.size
key = 50

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (r - key) % 256, (g - key) % 256, (b - key) % 256

img.save("decrypted.png")
print("Image decrypted successfully")
