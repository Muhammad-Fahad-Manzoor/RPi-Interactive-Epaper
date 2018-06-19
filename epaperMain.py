##
 #  @filename   :   epaperMain.py
 #  @brief      :   Interface for 2.9inch E-paper display with 2 x buttons
 #  @author     :   Fahad Manzoor
 ##

import epd2in9                                                                                    
import time
import Image
import ImageDraw
import ImageFont
import ImageOps
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#Button1 to GPIO16
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#Button2 to GPIO26	
	
def main():
	epd = epd2in9.EPD()                                                                           
	epd.init(epd.lut_partial_update)
	
	# For simplicity, the arguments are explicit numerical coordinates
	image = Image.new('1', (epd2in9.EPD_WIDTH, epd2in9.EPD_HEIGHT), 255)  # 255: clear the frame
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)                                                                                                      
	epd.clear_frame_memory(0xFF)
	epd.set_frame_memory(image, 0, 0)
	epd.display_frame()
	
	# epd.delay_ms(1000)

	# Add following lines:                                                                      
	##
	# there are 2 memory areas embedded in the e-paper display
	# and once the display is refreshed, the memory area will be auto-toggled,
	# i.e. the next action of SetFrameMemory will set the other memory area
	# therefore you have to set the frame memory twice.
	##     
	epd.clear_frame_memory(0xFF)
	epd.display_frame()
	epd.clear_frame_memory(0xFF)
	epd.display_frame()

	# for partial update                               
	epd.init(epd.lut_partial_update)
	# epd.delay_ms(10000)
	image = Image.open('image1.bmp')
	imageNumber = 1
	delay = 10000
	image = image.rotate(90)
	epd.delay_ms(delay)
	epd.set_frame_memory(image, 0, 0)
	epd.display_frame()
	epd.set_frame_memory(image, 0, 0)
	epd.display_frame()
	print(imageNumber) 
	# rotateAndClear()


  	
	image = Image.open('image2.bmp')
	image = image.rotate(90)
	imageNumber = 2
	epd.set_frame_memory(image, 0, 0)
	epd.display_frame()
	epd.set_frame_memory(image, 0, 0)
	epd.display_frame()
	print(imageNumber) 
	# rotateAndClear()

	while True:
		
		btn1_state = False
		btn2_state = False	
        	btn1_state = GPIO.input(16)
		btn2_state = GPIO.input(26)

	
		if btn1_state == True: #False means Button NOT pressed
			print('BTN1 is pressed')
			if imageNumber == 2:
				image = Image.open('image3.bmp')
				imageNumber = 3 
				delay = 10000
				image = image.rotate(90)
				epd.delay_ms(delay)
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				print(imageNumber)
				# rotateAndClear()

				image = Image.open('image4.bmp')
				imageNumber = 4
				delay = 10000
				image = image.rotate(90)
				epd.delay_ms(delay)
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				print(imageNumber)
				# rotateAndClear()
			
			elif imageNumber==4:
				image = Image.open('image5.bmp')
				imageNumber = 5 
				delay = 10000
				image = image.rotate(90)
				epd.delay_ms(delay)
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				print(imageNumber) 
				# rotateAndClear()

				image = Image.open('image6.bmp')
				imageNumber = 6  
				delay = 10000
				image = image.rotate(90)
				epd.delay_ms(delay)
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				print(imageNumber)
				# rotateAndClear()
	
				image = Image.open('image2.bmp')
				imageNumber = 2
				image = image.rotate(90)
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				print(imageNumber) 
				# rotateAndClear()
									

			

	

		     	
		if btn2_state == True and imageNumber == 2: #False means Button NOT pressed
			print('BTN2 is pressed')
			image = Image.open('image7.bmp')
			btn2_state = False
			imageNumber = 7
			delay = 10000
			image = image.rotate(90)
			epd.delay_ms(delay)
			epd.set_frame_memory(image, 0, 0)
			epd.display_frame()
			epd.set_frame_memory(image, 0, 0)
			epd.display_frame()
			print(imageNumber) 
			# rotateAndClear()
			

			if imageNumber==7 and btn1_state == True:
				print('BTN1 is pressed again')
				image = Image.open('image3.bmp')
				imageNumber = 3
				delay = 10000
				image = image.rotate(90)
				epd.delay_ms(delay)
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				print(imageNumber) 
				# rotateAndClear()
	
				image = Image.open('image4.bmp')
				imageNumber = 4
				image = image.rotate(90)
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				print(imageNumber) 
				# rotateAndClear()
				btn1_state = False
				
			elif imageNumber==7:
				image = Image.open('image8.bmp')
				imageNumber = 8
				# delay = 10000
				image = image.rotate(90)
				# epd.delay_ms(delay)
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				epd.set_frame_memory(image, 0, 0)
				epd.display_frame()
				print(imageNumber) 
				# rotateAndClear()
					
				if imageNumber == 8 and btn2_state == True:
					image = Image.open('image7.bmp')
					imageNumber = 7
					delay = 10000
					image = image.rotate(90)
					epd.delay_ms(delay)
					epd.set_frame_memory(image, 0, 0)
					epd.display_frame()
					epd.set_frame_memory(image, 0, 0)
					epd.display_frame()
					print(imageNumber) 
					# rotateAndClear()
	
				elif imageNumber == 8 and btn2_state == False:
					image = Image.open('image9.bmp')
					imageNumber = 9
					delay = 10000
					image = image.rotate(90)
					epd.delay_ms(delay)
					epd.set_frame_memory(image, 0, 0)
					epd.display_frame()
					epd.set_frame_memory(image, 0, 0)
					epd.display_frame()
					print(imageNumber) 
					# rotateAndClear()
		
					image = Image.open('image2.bmp')
					imageNumber = 2 
					delay = 10000
					image = image.rotate(90)
					epd.delay_ms(delay)
					epd.set_frame_memory(image, 0, 0)
					epd.display_frame()
					epd.set_frame_memory(image, 0, 0)
					epd.display_frame()
					print(imageNumber)
					# rotateAndClear()
					
	



			
	
			

	##
 	# there are 2 memory areas embedded in the e-paper display
	# and once the display is refreshed, the memory area will be auto-toggled,
 	# i.e. the next action of SetFrameMemory will set the other memory area
 	# therefore you have to set the frame memory twice.
 	##     
	epd.set_frame_memory(image, 0, 0)
	epd.display_frame()
	epd.set_frame_memory(image, 0, 0)
	epd.display_frame()

	time_image = Image.new('1', (96, 32), 255)  # 255: clear the frame
	draw = ImageDraw.Draw(time_image)
	font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 32)
	image_width, image_height  = time_image.size


if __name__ == '__main__':
	main()
