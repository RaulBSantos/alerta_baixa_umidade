from datetime import datetime
import logging

import telegram_send
from alerta_baixa_umidade.src.globals import AIR_HUMIDITY_MIN


class TelegramNotifier:
    last_notification = None

    def _send_notification(self, humidity, temperature):
        logging.info('Sending Telegram message. Humidity: %s, Temperature: %s ', humidity, temperature)
        telegram_send.send(messages=[r"Atenção! Umidade baixa detectada! {}%".format(humidity),
                                     "Temperatura atual: {}°C".format(temperature)])
        self.last_notification = datetime.now()

    def _send_first_daily_notification(self, humidity, temperature):
        logging.info('_send_first_daily_notification: %s, Temperature: %s ', humidity, temperature)
        current_date = datetime.now()
        if not self.last_notification or current_date.day != self.last_notification.day:
            self._send_notification(humidity, temperature)

    def alert_low_humidity(self, humidity, temperature):
        logging.info('alert_low_humidity: %s, Temperature: %s ', humidity, temperature)
        if humidity <= AIR_HUMIDITY_MIN:
            self._send_first_daily_notification(humidity, temperature)


if __name__ == '__main__':
    telegram = TelegramNotifier()
    telegram.alert_low_humidity(100, 100)
