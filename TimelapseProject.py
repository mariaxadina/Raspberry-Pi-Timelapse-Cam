from RPLCD.i2c import CharLCD
from time import sleep
from gpiozero import Button
from picamera2 import Picamera2
from datetime import datetime
import os
import time
import subprocess
import shutil

button_down = Button(17)
button_select = Button(27)
button_up = Button(22)

lcd = CharLCD('PCF8574', 0x3f)

lcd.write_string("Loading...")
sleep(2)
lcd.clear()

menu = ["Start Timelapse Cam", "      Help", "      Info"]
menuTime = ["5", "10", "15", "20", "25", "30", "45", "60", "120"]
key = 0
keyTime = 0



def show_info_on_lcd():
    lcd.clear()
    
    # Afișează data
    lcd.write_string(f"Date: 19.05.2025")
    sleep(2)

    # Afișează numele proiectului
    lcd.clear()
    lcd.write_string("Timelapse Cam")
    sleep(2)

    # Afișează persoanele implicate
    lcd.clear()
    lcd.cursor_pos = (0, 0)      
    lcd.write_string("Created by:")
    lcd.cursor_pos = (1, 0)        
    lcd.write_string("Maria & Stefan")
    sleep(3)

    lcd.clear()
    lcd.write_string("Have fun! :)")
    sleep(2)

    lcd.clear()




def createVideo(now):
    year = now.strftime("%Y")
    month_name = now.strftime("%B")
    day = now.strftime("%d")

    # Folderul cu poze
    photos_path = f"/home/raspberrypi/Timelapse_Cam/Photo/{year}/{month_name}/{day}"
    # Folderul unde salvezi video-ul
    video_path = f"/home/raspberrypi/Timelapse_Cam/Video/{year}/{month_name}/{day}"
    # Creează folderul pentru video dacă nu există
    os.makedirs(video_path, exist_ok=True)

    timestamp = datetime.now().strftime("%H-%M-%S")
    output_video = os.path.join(video_path, f"video {timestamp}.mp4")


    # Temporary directory to hold renamed images
    temp_dir = os.path.join(photos_path, "temp_ffmpeg")
    os.makedirs(temp_dir, exist_ok=True)

    # Get and sort all jpg files
    all_photos = sorted([
        f for f in os.listdir(photos_path)
        if f.lower().endswith(".jpg") and os.path.isfile(os.path.join(photos_path, f))
    ])

    print(f"Found {len(all_photos)} photos.")

    if not all_photos:
        print("❌ No photos found to process.")
        return

    # Copy and rename photos as image_00001.jpg, etc.
    for i, original_name in enumerate(all_photos):
        src = os.path.join(photos_path, original_name)
        dst = os.path.join(temp_dir, f"image_{i:05}.jpg")
        print(f"Copying {src} -> {dst}")
        shutil.copy2(src, dst)

    # FFmpeg command
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate", "10",
        "-i", "image_%05d.jpg",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_video
    ]

    print(f"Running FFmpeg in: {temp_dir}")
    subprocess.run(cmd, cwd=temp_dir)

    shutil.rmtree(temp_dir)
    print(f"✅ Video created: {output_video}")





picam2 = Picamera2()
picam2.start()
def TimelapseCam(interval):
    interval = float(interval)
    sleep(2)
    lcd.clear()
    lcd.write_string("Taking photos...")

    # Obține data curentă
    now = datetime.now()
    year = now.strftime("%Y")
    month_name = now.strftime("%B")
    day = now.strftime("%d")

    # Creează calea completă pentru salvare
    base_path = f"/home/raspberrypi/Timelapse_Cam/Photo/{year}/{month_name}/{day}"
    os.makedirs(base_path, exist_ok=True)
    ok = 0
    nr = 1
    while True:
        start_time = time.time()
	
        timestamp = datetime.now().strftime("%H-%M-%S")
        filename = os.path.join(base_path, f"image_{timestamp}.jpg")
        picam2.capture_file(filename)
        print(f"Captured {filename}")
	
	
        while time.time() - start_time < interval:
            if button_select.is_pressed:
                lcd.clear()
                lcd.write_string("Timelapse Cam stopped.")
                ok = 1
                break
	
        if ok == 1:
            break
        # Aici se poate modifica intervalul dintre poze
        # sleep(time)

    lcd.clear()
    lcd.clear()
    lcd.cursor_pos = (0, 0)          
    lcd.write_string("Save video?")

    lcd.cursor_pos = (1, 0)          
    lcd.write_string("no")

    lcd.cursor_pos = (1, 13)         
    lcd.write_string("yes")
    while True:
        if button_up.is_pressed:
            lcd.clear()
            createVideo(now)
            lcd.write_string("Video saved!")
            sleep(3)
            return
        if button_down.is_pressed:
            lcd.clear()
            lcd.write_string("Video not saved!")
            return
	    

def show_option(chosenMenu, chosenKey):
    lcd.clear()
    lcd.write_string(chosenMenu[chosenKey])
    lcd.cursor_pos = (1, 0)
    if chosenKey == 0:
        lcd.write_string("              ->")
    elif chosenKey == len(chosenMenu) - 1:
        lcd.write_string("<-              ")
    else:
        lcd.write_string("<-            ->")



def optionSelected():
    global key, keyTime
    
    if key == 0:
        lcd.clear()
        lcd.cursor_pos = (0, 0)  
        lcd.write_string("Choose time")
        lcd.cursor_pos = (1, 0)  
        lcd.write_string("between frames:")
        sleep(2)
        lcd.clear()
        show_option(menuTime, keyTime)
        while True:
            if button_down.is_pressed:
                print("Butonul <down> a fost apasat!")
                if keyTime > 0:
                    keyTime -= 1
                show_option(menuTime, keyTime)
                sleep(0.5)

            if button_select.is_pressed:
                TimelapseCam(menuTime[keyTime])
                return

            if button_up.is_pressed:
                print("Butonul <up> a fost apasat!")
                if keyTime < len(menuTime) - 1:
                    keyTime += 1
                show_option(menuTime, keyTime)
                sleep(0.5)
		
    if key == 1:
        lcd.clear()
        lcd.write_string("Navigate Menu")
        sleep(2)
        lcd.clear()
        lcd.write_string("Info Buttons:")
        lcd.cursor_pos = (1, 0)                  
        lcd.write_string("DOWN select UP")
        sleep(3)
        lcd.clear()
        lcd.write_string("When saving")
        lcd.cursor_pos = (1, 0)   
        lcd.write_string("video:")
        sleep(3)
        lcd.clear()
        lcd.write_string("DOWN for no")
        lcd.cursor_pos = (1, 0)   
        lcd.write_string("UP for yes")
        sleep(3)
        lcd.clear()
    if key == 2:
        show_info_on_lcd()
	


show_option(menu, key)	
try:
    while True:
        if button_down.is_pressed:
            print("Butonul <down> a fost apasat!")
            if key > 0:
                key -= 1
            show_option(menu, key)
            sleep(0.5)

        if button_select.is_pressed:
            print("Butonul <select> a fost apasat!")
            lcd.clear()
            optionSelected()
            lcd.clear()
            show_option(menu, key)
            sleep(1)

        if button_up.is_pressed:
            print("Butonul <up> a fost apasat!")
            if key < len(menu) - 1:
                key += 1
            show_option(menu, key)
            sleep(0.5)

except KeyboardInterrupt:
    print("Program Stopped by user")