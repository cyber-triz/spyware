# 🕵️‍♀️ Projeto: Spyware Educacional em Python

## 📌 Descrição

Este projeto demonstra de forma **educacional** como funcionam técnicas básicas de spyware, incluindo:

- Captura de teclas (keylogger)
- Captura de tela (screenshot)
- Armazenamento local das informações

> ⚠️ **Este projeto é destinado apenas para fins educativos e laboratoriais.**  
> **Não deve ser usado em ambientes reais ou para atividades maliciosas.** O uso indevido é de responsabilidade exclusiva de quem o utiliza.

---

## ⚙️ Funcionalidades

- 🖱️ Captura de teclas pressionadas (keylogger)
- 📸 Tira screenshots automáticas
- 🗃️ Salva logs e imagens localmente
- 🧵 Executa tudo em segundo plano usando `threading`

---

## 🧰 Tecnologias Utilizadas

- **Python 3.x**
- [`pynput`](https://pypi.org/project/pynput/) — para monitorar o teclado
- [`Pillow`](https://pypi.org/project/Pillow/) — para capturar screenshots
- `threading` e `datetime` (bibliotecas padrão do Python)

---

## 📁 Estrutura do Projeto
spyware/
├── spyware.py
├── logs/
│ └── keylog.txt
├── screenshots/
│ └── screenshot_YYYY-MM-DD_HH-MM-SS.png


---

## ▶️ Como Executar

1. Instale as dependências:
```bash
pip install pynput pillow
python spyware.py

🔒 Aviso Legal

Este projeto foi criado para fins educacionais e laboratoriais, visando entendimento de técnicas de segurança ofensiva para profissionais da área.
Nunca utilize este código sem consentimento explícito do usuário.
