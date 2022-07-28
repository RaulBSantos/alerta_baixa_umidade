#!/bin/bash

# O script deve estar ativado na Raspberry Pi como uma Crontab. Executar `crontab -e` e adicionar a configuração:
# @reboot python3 /home/pi/workspace/sensor_umidade/main.py
scp -pr ../sensor_umidade/alerta_baixa_umidade/ pi@192.168.15.200:/home/pi/workspace/

# Para acessar a Raspberry Pi:
# ssh pi@192.168.15.200
