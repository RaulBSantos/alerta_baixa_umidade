from unittest.mock import MagicMock

import pytest

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
        telegram = TelegramNotifier(air_humidity_min=60)
        telegram._send_first_daily_notification = MagicMock()
        telegram.alert_low_humidity(humidity=humidity_value, temperature=None)

        telegram._send_first_daily_notification.assert_not_called()
