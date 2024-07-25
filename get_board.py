from time import sleep
from PIL import Image
from PIL import ImageGrab


filename = r'board.png'

board = Image.open(filename)

size = board.size

square_size = int(size[0] / 9) + 1

n = 0
for y in range(0, size[0], square_size):
    for x in range(0, size[0], square_size):
        square_bbox =  x, y, square_size + x , square_size + y #im.crop((left - x0, top - y0, right - x0, bottom - y0))
        square = board.crop(square_bbox)
        square.save(f'squares/square{n}.png')
        n+=1

        

print(0, size[0], square_size)