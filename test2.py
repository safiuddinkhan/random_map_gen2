import random
from PIL import Image, ImageDraw

offset_y = 5
offset_x = 5
tile_w = 8
tile_h = 8
win = 0
im = 0





###################################################################################
def draw_tile(im,y,x,fill):
	draw = ImageDraw.Draw(im)
	draw.rectangle([x*tile_w+offset_x,y*tile_h+offset_y,((x+1)*tile_w)-1+offset_x,((y+1)*tile_h)-1+offset_y],fill,width=1)

def display_map_im(map,im,h,w):	
	for y in range(0,h):
		for x in range(0,w):
			if map[y][x] == 1:
				draw_tile(im,y,x,0xffffff)
###################################################################################

def gen_noise(map,d,h,w):
	
	for y in range(0,h):
		for x in range(0,w):
			r = int(random.random() * 100)
			if r > d:
				map[y][x] = 1


def ca_func(map,y,x,h,w):
	c = 0
	#print("-----------------")
	for yy in range(y-1,y+2):
		for xx in range(x-1,x+2):
			if(yy < 0):
#				print("- [%d %d]" % (yy,xx))
				c = c + 1

			elif(xx < 0):
#				print("- [%d %d]" % (yy,xx))
				c = c + 1

			elif(yy > h-1):
#				print("- [%d %d]" % (yy,xx))
				c = c + 1

			elif(xx > w-1):
#				print("- [%d %d]" % (yy,xx))
				c = c + 1

			elif(yy == y and xx == x):
#				print("-- [%d %d]" % (yy,xx))
				pass
			else:
				#print("[%d %d]" % (yy,xx))
				if(map[yy][xx] == 0):
					c = c + 1
		
	return c


def gen_ca(map,map1,h,w):
	for y in range(0,h):
		for x in range(0,w):
			c = ca_func(map,y,x,h,w)
			#print("[%d %d] n = %d" % (y,x,c))
			if(c > 4):
				map1[y][x] = 0
			else:
				map1[y][x] = 1

def clone(inp,out,h,w):
	for y in range(0,h):
		for x in range(0,w):
			inp[y][x] = out[y][x]
			
def gen_ca_i(inp,h,w,itr):
	out = [[0 for x in range(w)] for y in range(h)]

	for i in range(0,itr):
		gen_ca(inp,out,h,w)
		clone(inp,out,h,w)
		

	
		
	

###################################################################################

map = [[0 for x in range(100)] for y in range(100)]



im = Image.new('RGB', ((8*100)+10,(8*100)+10))



gen_noise(map,60,100,100)
gen_ca_i(map,100,100,10)





display_map_im(map,im,100,100)



im.show()
im.save("test2.png", "PNG")
