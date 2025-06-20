# Raspberry Pi Timelapse Cam
## Table of Contents
1. [Introduction](#introduction)
2. [General Description](#General-Description)
3. [Hardware Design](#Hardware-Design)
4. [Software Design](#Software-Design)
5. [Results](#Results)
6. [Bibliography/Resources](#Bibliography/Resources)
   
## Introduction
This project is a Timelapse Camera system built with a Raspberry Pi, designed to automatically capture images at user-defined intervals and organize them into date-based folders. The system features a user-friendly interface through an I2C LCD display and three physical buttons for navigation and selection.

## General Description

### Detailed Description of Hardware Functionality
**1. Microcomputer Raspberry Pi 4B**: It runs the Python scripts, handles GPIO input from buttons, manages the camera module, and controls the LCD display. It also stores the captured images and can generate a timelapse video from them.

**2. LCD 16x2 Display with I2C Module**: Displays menu options and system messages to the user. The I2C module simplifies wiring and communication, using only two pins (SDA and SCL) on the Raspberry Pi.

**3. Microsoft LifeCam  HD-3000 Web Camera**: Used as the image capture device. It interfaces with the Raspberry Pi through USB and is controlled via the Picamera2 library to take snapshots for the timelapse.

## Description
To get started, I installed the Raspberry Pi OS onto a 128GB microSD card using the Raspberry Pi Imager. After booting up the Raspberry Pi 4 Model B, I connected it to Wi-Fi,activated ssh, set up a static IP address and enabled VNC via raspi-config, allowing me to remotely access the desktop environment from my laptop.

Next, I connected a 16x2 I2C LCD display and three physical buttons to the GPIO pins. Using Python, I built a menu interface on the LCD, navigable with the buttons (UP, DOWN, SELECT). This interface allows the user to browse through options like starting the timelapse, saving the video, viewing instructions for easy use.

## Hardware Design 
### Bill of Materials (BOM)
| Component                        | Quantity| Description                           | Datasheet                                                                                       |
|----------------------------------|---------|---------------------------------------|-------------------------------------------------------------------------------------------------|
| Raspberry Pi Model 4B            |1        | Main Microcomputer                    | https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf                            |
| 128GB microSD card               | 1       | Primary storage for OS                | https://www.kingston.com/datasheets/SDC10G2_us.pdf                                              |
| LCD 16x2 display with I2C Module | 1       | Menu Display                          | https://components101.com/sites/default/files/component_datasheet/16x2%20LCD%20Datasheet.pdf    |
| Mini Breadboard                  | 1       | Small board for easy connection       | https://media.digikey.com/pdf/Data%20Sheets/Sparkfun%20PDFs/PRT-12047_Web.pdf                   |
| Push Buttons                     | 3       | Used for navigating the menu          | https://components101.com/sites/default/files/component_datasheet/Push-Button.pdf               |
| Microsoft LifeCam Web Camera     | 1       | Captures images                       | https://download.microsoft.com/download/d/6/1/d61506a5-ac78-4e03-b35f-e4de7388251f/lchd3000_for%20business_sellsheet_us_lores.pdfm|
| Jumper Wires (Cables)            | -       | Male-to-female/Female-to-female wires | https://www.mouser.com/c/ds/tools-supplies/prototyping-products/jumper-wires/?srsltid=AfmBOopanPWOk8Ukw1_juN3MPRRptIMeLviuPscUZNwjSLqPMhHw0F-X|

### 3D Printed Cases with Prusa i3 MK3
To protect and organize the hardware components of the Timelapse Camera system, I 3D printed custom cases using the Prusa i3 MK3 printer.
#### Print Settings:
- Printer: Original Prusa i3 MK3

- Material: PETG (from Prusa), chosen for its durability and temperature resistance

- Infill: 15%

- Supports: Enabled everywhere

### Circuit Schematic  
<a>
  <img src="https://github.com/mariaxadina/Raspberry-Pi-Timelapse-Cam/blob/main/images/CircuitSchema.png" width="800"/>
</a>

### Connected Components
<p>
  <img src="https://github.com/mariaxadina/Raspberry-Pi-Timelapse-Cam/blob/main/images/1.jpeg" width="49%" />
  <img src="https://github.com/mariaxadina/Raspberry-Pi-Timelapse-Cam/blob/main/images/2.jpeg" width="49%" />
</p>
<p>
  <img src="https://github.com/mariaxadina/Raspberry-Pi-Timelapse-Cam/blob/main/images/3.jpeg" width="49%" />
  <img src="https://github.com/mariaxadina/Raspberry-Pi-Timelapse-Cam/blob/main/images/4.jpeg" width="49%" />
</p>


## Software Design

### Development Environment 
The project is developed directly on a Raspberry Pi 4 Model B, running Raspberry Pi OS. Development and interaction are done using: Python 3 as programming language, VNC Viewer to remotely access the Raspberry Pi, Terminal for writing and running Python scripts.

### Libraries
In this project, I used three libraries to manage various components effectively:
- **Picamera2**: Capture images with the connected camera.
- **RPLCD**: Designed to control LCD output.
- **GPIO Zero**: Used to control buttons.

### Image Capture Using Microsoft LifeCam HD-3000
To capture high-quality images for the timelapse sequence, I used the Microsoft LifeCam HD-3000, a USB webcam known for its reliability and 720p resolution. The camera was interfaced with the Raspberry Pi using the Picamera2 library, which offers support for USB cameras and seamless integration into Python scripts.

## Results
The final outcome of the project successfully met all the initial objectives. The Raspberry Pi 4B, paired with the Microsoft LifeCam HD-3000 and LCD interface, functioned reliably to capture timelapse sequences based on user-selected intervals.

### Collaboration
This project was developed in collaboration with [Bichel Stefan-Adrian](https://github.com/StefanAdrian2003).

## Bibliography/Resources
1. https://www.youngwonks.com/blog/Raspberry-Pi-4-Pinout
2. https://www.raspberrypi.com/software/
3. https://www.instructables.com/Simple-timelapse-camera-using-Raspberry-Pi-and-a-c/
4. https://www.thingiverse.com/
