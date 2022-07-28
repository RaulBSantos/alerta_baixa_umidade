# import unittest
# from unittest.mock import MagicMock
#
# from alerta_baixa_umidade.src.globals import AIR_HUMIDITY_MIN
# from alerta_baixa_umidade.src.telegram_notifier import TelegramNotifier
#
#
# class TestSum(unittest.TestCase):
#
#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
#
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
#
# if __name__ == '__main__':
#     unittest.main()








# from unittest.mock import MagicMock
#
# from ..src.globals import AIR_HUMIDITY_MIN
# from alerta_baixa_umidade.src.telegram_notifier import TelegramNotifier
#
#
# class TestTelegramNotifier:
#     def test_alert_low_humidity_sends_message(self):
#         # given a low humitity value
#         humidity = AIR_HUMIDITY_MIN
#         telegram = TelegramNotifier()
#         telegram._send_first_daily_notification = MagicMock()
#         telegram.alert_low_humidity(humidity=humidity, temperature=None)
#
#         telegram._send_first_daily_notification.assert_called_once_with(humidity, None)