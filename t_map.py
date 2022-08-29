from perlin_noise import PerlinNoise
import random
from PIL import Image, ImageDraw

offset_y = 5
offset_x = 5
tile_w = 8
tile_h = 8

map = [[0 for x in range(100)] for y in range(100)]



###################################################################################

def draw_tile(im,y,x,fill):
	draw = ImageDraw.Draw(im)
	draw.rectangle([x*tile_w+offset_x,y*tile_h+offset_y,((x+1)*tile_w)-1+offset_x,((y+1)*tile_h)-1+offset_y],fill,width=1)


def display_map_im(im,h,w):	
	for y in range(0,h):
		for x in range(0,w):
			if map[y][x] == 1:
				draw_tile(im,y,x,0xff0000)
			elif map[y][x] == 2:
				draw_tile(im,y,x,0x00ff00)	
###################################################################################

def gen_map(h,w):
	noise = PerlinNoise(octaves=3,seed=1)
	for y in range(h):
		for x in range(w):
			n = noise([x/w, y/h])
			print("[%d %d]: %f" % (y,x,n))
			if n < 0:
				map[y][x] = 1
			else:
				map[y][x] = 2



###################################################################################



im = Image.new('RGB', ((8*100)+10,(8*100)+10))
gen_map(100,100)
display_map_im(im,100,100)
im.save("map.png", "PNG")
im.show()




print("Hello this is a test")
