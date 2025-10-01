## What is it?

A Telegram bot for group chats that can parse topics for messages containing links to PDF articles and download those PDFs into a local directory.

## How to run?

1. Run `poetry env activate` in the root directory.

2. Run `poetry install` in the root directory.

3. Run `poetry run python src/bot_server.py` and the bot will start polling.

## Setup in Telegram

1. Add the bot to your group.

2. Add the bot to the list of administrators (so that it receives all messages, not just commands).