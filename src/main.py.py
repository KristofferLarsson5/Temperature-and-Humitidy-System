import time
from umqtt.simple import MQTTClient
import dht
import machine

# Fill in your Adafruit IO Authentication and Feed MQTT Topic details
mqtt_host = "io.adafruit.com"
mqtt_username = "KristofferLarsson5"  # Your Adafruit IO username
mqtt_password = "aio_wgti93DTRfas1jUIdC30LhiOGEHs"  # Adafruit IO Key
mqtt_temperature_topic = "KristofferLarsson5/feeds/temperature-graph"  # Temperature MQTT topic
mqtt_humidity_topic = "KristofferLarsson5/feeds/humidity-graph"  # Humidity MQTT topic

# Enter a random ID for this MQTT Client
# It needs to be globally unique across all of Adafruit IO.
mqtt_client_id = "Kristoffer_DHT11_LNU2023"

# Initialize our MQTTClient and connect to the MQTT server
mqtt_client = MQTTClient(
    client_id=mqtt_client_id,
    server=mqtt_host,
    user=mqtt_username,
    password=mqtt_password)

mqtt_client.connect()

# Initialize the DHT sensor
tempSensor = dht.DHT11(machine.Pin(27))     # DHT11 Constructor

try:
    while True:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))

        # Publish temperature data
        mqtt_client.publish(mqtt_temperature_topic, str(temperature))
        print("Temperature data published")

        # Publish humidity data
        mqtt_client.publish(mqtt_humidity_topic, str(humidity))
        print("Humidity data published")

        time.sleep(10)

except Exception as error:
    print("Exception occurred:", error)

finally:
    mqtt_client.disconnect()