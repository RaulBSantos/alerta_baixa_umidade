import RPi.GPIO as GPIO
import Adafruit_DHT as dht
from datetime import datetime
import time
import logging

from globals import AIR_HUMIDITY_MIN, WORKING_TIME_RANGE
from telegram_notifier import TelegramNotifier

SENSOR_PIN = 17
RED_LED_PIN = 27
TIME_CICLE_SECONDS = 60 * 5

logging.basicConfig(filename='alerta_baixa_umidade.log',
                    format='%(asctime)s %(message)s',
                    level=logging.INFO)


def set_led_on_when_low_humidity(humidity):
    output_value = GPIO.HIGH if humidity <= AIR_HUMIDITY_MIN else GPIO.LOW
    logging.info('Setting Red light: %s', output_value)
    GPIO.output(RED_LED_PIN, output_value)


def read_humidity_and_temperature_sensor():
    humi, temp = dht.read_retry(dht.DHT11, SENSOR_PIN)
    logging.info('Humidity: %s Temperature: %s', humi, temp) #FIXME: Implementar log rotate
    return humi, temp


if __name__ == '__main__':
    logging.info('***Starting***')
    # setup GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RED_LED_PIN, GPIO.OUT)
    logging.info('GPIO configured!')
    telegram = TelegramNotifier(air_humidity_min=AIR_HUMIDITY_MIN)
    while True:
        if datetime.now().hour in WORKING_TIME_RANGE:
            humidity, temperature = read_humidity_and_temperature_sensor()
            set_led_on_when_low_humidity(humidity)
            telegram.alert_low_humidity(humidity, temperature)
            time.sleep(TIME_CICLE_SECONDS)
