import logging
from unittest.mock import MagicMock

import pytest
import telegram_send

from ..src.telegram_notifier import TelegramNotifier


class TestTelegramNotifier:
    AIR_HUMIDITY_MIN_PARAMETER = 60

    @pytest.mark.parametrize("humidity_value", [60, 59])
    def test_alert_low_humidity_sends_message(self, humidity_value):
        telegram = TelegramNotifier(air_humidity_min=self.AIR_HUMIDITY_MIN_PARAMETER)
        telegram._send_first_daily_notification = MagicMock()
        telegram.alert_low_humidity(humidity=humidity_value, temperature=None)

        telegram._send_first_daily_notification.assert_called_once_with(humidity_value, None)

    @pytest.mark.parametrize("humidity_value", [61, 62])
    def test_alert_low_humidity_not_sends_message(self, humidity_value):
        telegram = TelegramNotifier(air_humidity_min=self.AIR_HUMIDITY_MIN_PARAMETER)
        telegram._send_first_daily_notification = MagicMock()
        telegram.alert_low_humidity(humidity=humidity_value, temperature=None)

        telegram._send_first_daily_notification.assert_not_called()

    @pytest.mark.parametrize("humidity_first,humidity_second", [(59, 59), (59, 60), (60, 60)])
    def test_alert_low_humidity_multiple_calls_sends_only_first_daily_message(self, mocker, humidity_first,
                                                                              humidity_second):
        # given a TelegramNotifier instance with min humidity
        mocker.patch('telegram_send.send')
        telegram = TelegramNotifier(air_humidity_min=self.AIR_HUMIDITY_MIN_PARAMETER)
        # when alert_low_humidity is called more than one time with low humidity
        telegram.alert_low_humidity(humidity=humidity_first, temperature=None)
        telegram.alert_low_humidity(humidity=humidity_second, temperature=None)
        # then telegram_send will be called once
        telegram_send.send.assert_called_once()

    def test_alert_low_humidity_absorb_thrown_exceptions(self, mocker):
        # given a exception sending telegram message
        mocker.patch('telegram_send.send', MagicMock(side_effect=Exception('Connection error, or something!')))
        mocker.patch('logging.error')
        # and a TelegramNotifier instance with min humidity
        telegram = TelegramNotifier(air_humidity_min=self.AIR_HUMIDITY_MIN_PARAMETER)
        # when alert_low_humidity is called
        telegram.alert_low_humidity(humidity=59, temperature=20)
        # then the exception should be absorbed (test will fail if it don't absorb)
        # and should print a logging line
        logging.error.assert_called_once()
