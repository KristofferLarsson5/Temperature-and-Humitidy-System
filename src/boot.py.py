import network
import time

# Fill in your WiFi network name (ssid) and password here:
wifi_ssid = ""
wifi_password = ""

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while not wlan.isconnected():
    print('Waiting for connection...')
    time.sleep(1)
print("Connected to WiFi"
