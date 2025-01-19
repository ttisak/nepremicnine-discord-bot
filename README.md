# nepremicnine-discord-bot
A discord bot for notifying about new listings on the [nepremicnine.net](https://nepremicnine.net) website using [Playwright](https://playwright.dev/python/).

![Main workflow](https://github.com/mevljas/nepremicnine-discord-bot/actions/workflows/main.yml/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)


## Project setup

### Setup environment variables

```bash
cp .env.example .env
```

### Install requirements

```bash
poetry install
```

### Install Playwright browsers (chromium, firefox, webkit)

```bash
playwright install chromium
```

## Run the local browser

```bash
cd 'C:\Program Files\Google\Chrome\Application'
./chrome.exe -remote-debugging-port=9222

```

## Configure the bot
- Add Discord bot token to the **.env** file.
- Add database path to the **.env** file.
- Add discord channel ids and nepremicnine.net search url pairs to the **config.txt** file.

## Development

### Analyze the code

```bash
poetry run pylint $(git ls-files '*.py')
```

### Format the code

```bash
poetry run black .
```


## Run the bot

```bash
poetry run python main.py
```