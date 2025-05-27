# Raspberry Pi Timelapse Cam

## Introduction
This project is a Timelapse Camera system built with a Raspberry Pi, designed to automatically capture images at user-defined intervals and organize them into date-based folders. The system features a user-friendly interface through an I2C LCD display and three physical buttons for navigation and selection.

### Detailed Description of Hardware Functionality
**1. Microcontroller - ATmega328P**


## Description
To get started, I installed the Raspberry Pi OS onto a 128GB microSD card using the Raspberry Pi Imager. After booting up the Raspberry Pi 4 Model B, I connected it to Wi-Fi,activated ssh, set up a static IP address and enabled VNC via raspi-config, allowing me to remotely access the desktop environment from my laptop.

Next, I connected a 16x2 I2C LCD display and three physical buttons to the GPIO pins. Using Python, I built a menu interface on the LCD, navigable with the buttons (UP, DOWN, SELECT). This interface allows the user to browse through options like starting the timelapse, saving the video, viewing instructions for easy use.

## Hardware Design 
### Bill of Materials (BOM)
| Component                        | Quantity| Description                           | Datasheet                                                                                       |
|----------------------------------|---------|---------------------------------------|-------------------------------------------------------------------------------------------------|
| Raspberry Pi Model 4B            |1        | Main Microcomputer                    | chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf|
| 128GB microSD card               | 1       | Primary storage for OS                | chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.kingston.com/datasheets/SDC10G2_us.pdf|
| LCD 16x2 display with I2C Module | 1       | Menu Display                          | https://components101.com/sites/default/files/component_datasheet/16x2%20LCD%20Datasheet.pdf|
| Mini Breadboard                  | 1       | Small board for easy connection       | chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://media.digikey.com/pdf/Data%20Sheets/Sparkfun%20PDFs/PRT-12047_Web.pdf|
| Push Buttons                     | 3       | Used for navigating the menu          | https://components101.com/sites/default/files/component_datasheet/Push-Button.pdf|
| Microsoft LifeCam Web Camera     | 1       | Captures images                       | https://download.microsoft.com/download/d/6/1/d61506a5-ac78-4e03-b35f-e4de7388251f/lchd3000_for%20business_sellsheet_us_lores.pdfm|
| Jumper Wires (Cables)            | -       | Male-to-female/Female-to-female wires | https://www.mouser.com/c/ds/tools-supplies/prototyping-products/jumper-wires/?srsltid=AfmBOopanPWOk8Ukw1_juN3MPRRptIMeLviuPscUZNwjSLqPMhHw0F-X|

### Circuit Schematic  
<a>
  <img src="https://github.com/mariaxadina/" width="800"/>
</a>

### Connected Components

### Development Environment 
The project is developed directly on a Raspberry Pi 4 Model B, running Raspberry Pi OS. Development and interaction are done using: Python 3 as programming language, VNC Viewer to remotely access the Raspberry Pi, Terminal for writing and running Python scripts.

### Libraries
In this project, I used three libraries to manage various components effectively:
- **Picamera2**: Capture images with the connected camera.
- **RPLCD**: Designed to control LCD output.
- **GPIO Zero**: Used to control buttons.


## Conclusions
