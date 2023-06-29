Created by: Kristoffer Larsson

Student credentials: kl223kk

Date: 2023 july
# Temperature-and-Humitidy-System
This tutorial will show you how to use the raspberry pi pico WH to send information about the humitidy and temperature in your room. For this to be done you will be using the raspberry pi pico WH, a DHT11 sensor, code in MicroPython and adafruit. 

Time estimation for project: 5 hours

# 1. Objectives

**1.1 The why**

Early on I knew that I wanted to use the DHT11 sensor to monitor my room, this to be able to get a clear understanding of how the climate in my apartment changes over the day. The fact that the DHT11 sensor also meausures humitidy made it clear to me that this sensor also were more superiour than a standard thermostate.

**1.2 Purpose**

The purpose of this project is to give the user an introductiction to how you can work with microcontrollers and basic sensors.

**1.3 Insights that the project might bring**

After this tutorial you will get a basic understanding of how you can work with the raspberry pi pico WH, the DHT11 sensor, adafruit and microPython.

# 2. Material
| Material name | Functionality | Where to buy |
|----------|----------|----------|
| Raspberry pi pico wh   | Microcontroller that runs programs and have multiple pins for connections to sensors. Also has the capability of running on WiFi.   | https://www.electrokit.com/produkt/raspberry-pi-pico-w/   |
| USB to micro-USB cable    | Transfers electricity to the microcontroller, which both gives it electricity to run, but also makes it possible to program it when plugged into a computer.   | https://www.electrokit.com/produkt/usb-kabel-a-hane-mini-b-hane-5p-1-8m/|
| Sensor DHT11   | A sensor that measures the temperature and humidity.   | https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/|
| Breadboard| A breadboard with connections that makes it easier to connect the microcontroller with the sensors.   | https://www.electrokit.com/en/product/solderless-breadboard-400-tie-points/   |
| Cables – male to male   | Connects electricity between the microcontroller, sensors and the power supply.   | https://www.electrokit.com/produkt/labsladd-1-pin-hane-hane-150mm-10-pack/|



# 3. Environment Setup
**3.1 Why I choose Thonny**

The reason that I chose Thonny as my IDE was because I had never worked with it nor heard about it. I quickly started to favor the basic setup and UI that Thonny offered.

Although that Thonny were my choice I actually also tried to use VScode and it also worked quite well, though in this tutorial I will only cover Thonny, but remember that VScode absolutly also is an option.

**3.2 Setting up the raspberry**

Step 1: Remove the black sponge from the Pico

Step 2: Download the micropython firmware, you will get a uf2 file, be sure to chose the latest from **releases** category: https://micropython.org/download/rp2-pico-w/

Step 3: Connect your raspberry pi to your computer by using the micro-usb cable

Step 4: While holding the BOOTSEL key on the raspberry, connect to your computer. Release the button after you see a new drive with the name RPI-RP2

Step 5: Paste the uf2 file into the raspberry and wait till it disconnects and reconnects to your computer

You have now updated the firmware on your raspberry and are ready to use it

**3.3 Setting up Thonny**

Step 1: Download Thonny from: https://github.com/thonny/thonny/releases/download/v4.0.2/thonny-4.0.2.exe

Step 2: Open Thonny and press View >> Files to open the file manager panel.

![image](https://github.com/KristofferLarsson5/Temperature-and-Humitidy-System/assets/117590527/4fae9d41-4c5f-4fef-846b-01139a83111d)

Step 3: Open interpreter from Run >> Configure interpreter
![image](https://github.com/KristofferLarsson5/Temperature-and-Humitidy-System/assets/117590527/60ee4bb9-97ea-4e4e-85ca-264da4cdcbc6)

Step 4: Choose MicroPython as your interpreter and after that choose your USB-port that is connected to your raspberry
![image](https://github.com/KristofferLarsson5/Temperature-and-Humitidy-System/assets/117590527/0ce9545f-c483-4f29-b0e4-763fa4cd066e)

You now have succeded with connecting your raspberry to Thonny, and your chosen programming language is micropython

# 4. Putting everything togheter
![Alt Text](2023-06-13.png)

# 5. Platforms and infrastructure
**5.1 Why I choose MQTT as my messaging protocol and Adafruit as my platform**

After just a couple of tries with MQTT I quickly realized that this would be more than enough for this project. I navigated to the Adafruit website and quickly got started with sending data from my device to the internet. The technical aspect was in my opinion not very hard to understand, and the code that you needed to provide were straightforward (more on this in the next part)

**5.2 How to get acess to MQTT with Thonny**

# 6. The code

# 7. The physical network layer

# 8. Visualization and user interface

# 9. Finalizing the design
