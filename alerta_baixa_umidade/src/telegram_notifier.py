from datetime import datetime
import logging

import telegram_send


class TelegramNotifier:
    last_notification = None
    air_humidity_min = None

    def __init__(self, air_humidity_min):
        self.air_humidity_min = air_humidity_min

    def _send_notification(self, humidity, temperature):
        logging.info('Sending Telegram message. Humidity: %s, Temperature: %s ', humidity, temperature)
        try:
            telegram_send.send(messages=[r"Atenção! Umidade baixa detectada! {}%".format(humidity),
                                         "Temperatura atual: {}°C".format(temperature)])
            self.last_notification = datetime.now()
        except Exception as e:
            logging.error('Error sending Telegram message. ', e)

    def _send_first_daily_notification(self, humidity, temperature):
        logging.info('_send_first_daily_notification: %s, Temperature: %s ', humidity, temperature)
        current_date = datetime.now()
        if not self.last_notification or current_date.day != self.last_notification.day:
            self._send_notification(humidity, temperature)

    def alert_low_humidity(self, humidity, temperature):
        logging.info('alert_low_humidity: %s, Temperature: %s ', humidity, temperature)
        if humidity <= self.air_humidity_min:
            self._send_first_daily_notification(humidity, temperature)
