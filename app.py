from PIL import Image


# it can be more automated
# like sending the rgbs with selenium to a website get its color name and print it

im = Image.open('Hormoz-Island-3.jpg')  # Can be many different formats.
pix = im.load()
frame = im.size
Colors = dict()

for x in range(frame[0]):
    for y in range(frame[1]):
        if (pix[x, y] in Colors.keys()):
            Colors[pix[x, y]] += 1
        else:
            Colors[pix[x, y]] = 1

Colors_Sorted = [(key, Colors[key])
                 for key in sorted(Colors, key=Colors.get, reverse=True)]

for i in range(100):
    item = Colors_Sorted[i]
    print("RGBs: " + str(item[0]) + "\t" + "Repetition: " + str(item[1]))
