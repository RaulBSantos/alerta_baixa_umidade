# alerta_baixa_umidade
Verifica e envia alertas pelo Telegram quando a umidade do ar estiver baixa


# testes
Usando o PyTest e PyTest-Cov.

Rodar: 
- Testes: `pytest`
- Cobertura:
  - Logar apenas linhas não cobertas:`pytest -vv --cov=. --cov-report=term-missing:skip-covered`
  - Cria um relatório em htmlcov/index.html: `pytest -vv --cov=. --cov-report=html`