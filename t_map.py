from perlin_noise import PerlinNoise
import random
import math
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
			elif map[y][x] == 3:
				draw_tile(im,y,x,0x00ffff)	
			elif map[y][x] == 4:
				draw_tile(im,y,x,0xffffff)	
			elif map[y][x] == 0:
				draw_tile(im,y,x,0)	


###################################################################################

def gen_map(h,w):
	r = random.random() * 65536
	noise = PerlinNoise(octaves=4,seed=r)
	for y in range(h):
		for x in range(w):

			n = math.floor(noise([x/w, y/h]) * 5)
#			print("[%d %d]: %f" % (y,x,n))
			if n <= -2:
				map[y][x] = 1
			elif n == -1:
				map[y][x] = 2
			elif n == 0:
				map[y][x] = 3
			elif n >= 1:
				map[y][x] = 4


###################################################################################

def draw_box_im(im,y,x,h,w):
	draw = ImageDraw.Draw(im)
	xx = (x*tile_w)+offset_x
	yy = (y*tile_h)+offset_y
	hh = h*tile_h
	ww = w*tile_w
	draw.rectangle([xx,yy,xx+ww,yy+hh],outline=0x0000ff,width=1)
	
	
def check_pos_tile(y,x):
		if map[y][x] != 1 and map[y+1][x] != 1 and map[y-1][x] != 1 and map[y][x+1] != 1 and map[y][x-1] != 1 and map[y-1][x-1] != 1 and map[y+1][x+1] != 1 and map[y-1][x+1] != 1 and map[y+1][x-1] != 1:
			return 1
		else:
			return 0





def divide_box(im,y,x,h,w,c,count):
#	draw_box_im(im,y,x,h,w)
	
	if count == 0:
		new_y = int(y + (random.random()*(h-4))) + 2
		new_x = int(x + (random.random()*(w-4))) + 2
		#print("map: [%d %d] %d" % (new_y,new_x,map[new_y][new_x]))
		

		if check_pos_tile(new_y,new_x):
			map[new_y][new_x] = 0
			#draw_tile(im,new_y,new_x,0)
		return 0
	
	if c == 0:   # horizontal
		new_h = random.randint(int(h/5),int(h/2))

		new_pos1 = [y,x]
		new_size1 = [new_h,w]
		
		new_pos2 = [y+(new_h),x]
		new_size2 = [(h-new_h),w]

		y1 = new_pos1[0] + (new_size1[0]/2)
		x1 = new_pos1[1] + (new_size1[1]/2)
		
		y2 = new_pos2[0] + (new_size2[0]/2)
		x2 = new_pos2[1] + (new_size2[1]/2)
	
		divide_box(im,new_pos1[0],new_pos1[1],new_size1[0],new_size1[1],1,count-1)
		divide_box(im,new_pos2[0],new_pos2[1],new_size2[0],new_size2[1],1,count-1)
		
	else:        # vertical
		new_w = random.randint(int(w/5),int(w/2))



		new_pos1 = [y,x]
		new_size1 = [h,new_w]
		
		new_pos2 = [y,x+new_w]
		new_size2 = [h,w-new_w]
		
		y1 = new_pos1[0] + (new_size1[0]/2)
		x1 = new_pos1[1] + (new_size1[1]/2)
		
		y2 = new_pos2[0] + (new_size2[0]/2)
		x2 = new_pos2[1] + (new_size2[1]/2)

		divide_box(im,new_pos1[0],new_pos1[1],new_size1[0],new_size1[1],0,count-1)
		divide_box(im,new_pos2[0],new_pos2[1],new_size2[0],new_size2[1],0,count-1)		

	return 0
	
	

###################################################################################

im = Image.new('RGB', ((8*100)+10,(8*100)+10))
gen_map(100,100)
divide_box(im,0,0,100,100,random.randint(0,1),5)
display_map_im(im,100,100)

im.save("map.png", "PNG")
im.show()


