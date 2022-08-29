import random
from PIL import Image, ImageDraw

offset_y = 5
offset_x = 5
tile_w = 8
tile_h = 8
win = 0
im = 0

map = [[0 for x in range(100)] for y in range(100)]



rooms = [(4,15),(4,25),(5,12),(5,25),(6,10),(6,16),(8,8),(8,12),(9,9),(9,10),(10,10)]



################################################################################
def display_map(h,w):
	for y in range(0,h):
		for x in range(0,w):
			if map[y][x] == 1:
				print("\u2588",end='')
			elif map[y][x] == 2:
				print("\u2592",end='')
			else:
				print(" ",end='')
		print("")


def draw_box_map(x1,y1,x2,y2,c):
	x1 = int(x1)
	x2 = int(x2)
	y1 = int(y1)
	y2 = int(y2)
	
	
	for y in range(y1,y2):
		for x in range(x1,x2):
			map[y][x] = c
################################################################################


def get_room_size(h,w):
	for i in range(len(rooms)-1,-1,-1):
		c = rooms[i]
		if c[0] <= h-2 and c[1] <= w-2:
			return c
	return (h-2,w-2)
	


#def gen_random_colors():
#	r = random.randint(10,255)
#	g = random.randint(10,255)
#	b = random.randint(10,255)
#	return color_rgb(r,g,b)


def draw_wbox(y,x,h,w):
	xx = (x*tile_w)+offset_x
	yy = (y*tile_h)+offset_y
	hh = h*tile_h
	ww = w*tile_w
	draw_box_map(x,y,x+w,y+h,1)



def draw_path(y1,x1,y2,x2,s):
	draw_box_map(x1,y1,x2+s,y2+s,2)






def draw_box_im(im,y,x,h,w):
	draw = ImageDraw.Draw(im)
	xx = (x*tile_w)+offset_x
	yy = (y*tile_h)+offset_y
	hh = h*tile_h
	ww = w*tile_w
	draw.rectangle([xx,yy,xx+ww,yy+hh],outline=0x0000ff,width=1)





def divide_box(y,x,h,w,c,count):
#	draw_box_im(im,y,x,h,w)
	
	if count == 0:
		rr = get_room_size(h,w)
		new_y = (h/2) - (rr[0]/2)
		new_x = (w/2) - (rr[1]/2)
		draw_wbox(y+new_y,x+new_x,rr[0],rr[1])
		return 0
	
	if c == 0:   # horizontal
		new_h = random.randint(int(h/5),int(h/2))
		
		if new_h < 6:
			rr = get_room_size(h,w)
			new_y = (h/2) - (rr[0]/2)
			new_x = (w/2) - (rr[1]/2)
			draw_wbox(y+new_y,x+new_x,rr[0],rr[1])
			return 0
		

		new_pos1 = [y,x]
		new_size1 = [new_h,w]
		
		new_pos2 = [y+(new_h),x]
		new_size2 = [(h-new_h),w]

		y1 = new_pos1[0] + (new_size1[0]/2)
		x1 = new_pos1[1] + (new_size1[1]/2)
		
		y2 = new_pos2[0] + (new_size2[0]/2)
		x2 = new_pos2[1] + (new_size2[1]/2)
		draw_path(y1,x1,y2,x2,1)
	
		divide_box(new_pos1[0],new_pos1[1],new_size1[0],new_size1[1],1,count-1)
		divide_box(new_pos2[0],new_pos2[1],new_size2[0],new_size2[1],1,count-1)
		
	else:        # vertical
		new_w = random.randint(int(w/5),int(w/2))
		
		if new_w < 10:
			rr = get_room_size(h,w)
			new_y = (h/2) - (rr[0]/2)
			new_x = (w/2) - (rr[1]/2)
			draw_wbox(y+new_y,x+new_x,rr[0],rr[1])
			return 0

		new_pos1 = [y,x]
		new_size1 = [h,new_w]
		
		new_pos2 = [y,x+new_w]
		new_size2 = [h,w-new_w]
		
		y1 = new_pos1[0] + (new_size1[0]/2)
		x1 = new_pos1[1] + (new_size1[1]/2)
		
		y2 = new_pos2[0] + (new_size2[0]/2)
		x2 = new_pos2[1] + (new_size2[1]/2)
		draw_path(y1,x1,y2,x2,1)
		
		divide_box(new_pos1[0],new_pos1[1],new_size1[0],new_size1[1],0,count-1)
		divide_box(new_pos2[0],new_pos2[1],new_size2[0],new_size2[1],0,count-1)		

	return 0
	

###################################################################################
def draw_tile(im,y,x,fill):
	draw = ImageDraw.Draw(im)
	draw.rectangle([x*tile_w+offset_x,y*tile_h+offset_y,((x+1)*tile_w)-1+offset_x,((y+1)*tile_h)-1+offset_y],fill,width=1)

def display_map_im(im,h,w):	
	for y in range(0,h):
		for x in range(0,w):
			if map[y][x] == 1:
				draw_tile(im,y,x,0xffffff)
			elif map[y][x] == 2:
				draw_tile(im,y,x,0xff0000)			
###################################################################################


im = Image.new('RGB', ((8*100)+10,(8*100)+10))


room_count = 0
divide_box(0,0,100,100,random.randint(0,1),50)
display_map(100,100)

display_map_im(im,100,100)
im.save("bsp.png", "PNG")

