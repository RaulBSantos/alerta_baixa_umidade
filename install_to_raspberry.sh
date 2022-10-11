#!/bin/bash

# Preencher com os dados abaixo
USER=<usuario-do-raspberry-pi>
IP=<ip-rede-local-do-raspberry-pi>
# O script deve estar ativado na Raspberry Pi como uma Crontab. Executar `crontab -e` e adicionar a configuração:
# @reboot python3 /home/pi/workspace/sensor_umidade/main.py
scp -pr ../sensor_umidade/alerta_baixa_umidade/ USER@IP:/home/pi/workspace/


