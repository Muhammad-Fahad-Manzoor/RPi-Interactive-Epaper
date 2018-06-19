# RPi-Button-Interface
This program provides Epaper interactive interface with two user buttons and 10 images/messages for raspberry pi
  
# Development Environment
  * OS: Raspbian for Raspberry Pi
  * Libraries required: 
        SPI library of Python
        PIL (Python Imaging Library) library
	BCM2835 library
        WiringPi library
        Spidev library
        RPi.GPIO library

# Hardware connection
  * EPD    ->    Raspberry Pi
  * VCC    ->    3.3
  * GND    ->    GND
  * DIN    ->    MOSI
  * CLK    ->    SCLK
  * CS     ->    24 (Physical, BCM: CE0, 8)
  * D/C    ->    22 (Physical, BCM: 25)
  * RES    ->    11 (Physical, BCM: 17)
  * BUSY   ->    18 (Physical, BCM: 24)

# How to use
  1. install the Python libraries.
  2. hardware setup with rpi, epaper, buttons
  3. add 10 images in the Epaper_Interactive_UI folder which you like to display on epaper in bmp format with names: image1, image2, ...image10
  3. run the with: 
     sudo python epaperMain.py


