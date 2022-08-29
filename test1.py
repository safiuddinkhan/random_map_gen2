from PIL import Image, ImageDraw



im = Image.new('RGB', (100, 100))

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=0xffffff)
draw.rectangle([0, 0, 5, 5],outline=0xffffff,width=1)


im.save("test1.png", "PNG")
im.show()
