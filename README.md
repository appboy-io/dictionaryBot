# DictionaryBot
DictionaryBot is a Discord bot that allows users to lookup the definition of words in the chat. The bot is written in Python and uses the Meriam Webster Dictionary API to retrieve the definitions.

## Usage
To use DictionaryBot, simply type /define <word> in the chat, where <word> is the word you want to lookup. For example, to lookup the definition of the word "computer", type:

```bash
/define computer
```
The bot will then reply with the definition of the word. If the bot is unable to find a definition for the word, it will reply with an error message.

Install on your s

## Run Locally
To install and run DictionaryBot, follow these steps:

### Prerequisites
* Docker
* Docker Compose
* VENV
* Python 3.9.6+

1. Clone this repository to your local machine.

2. Create a virtual environment for the project using virtualenv or conda.

3. Activate the virtual environment.

4. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

5. Create a new Discord bot and obtain the bot token.

6. Sign up at Meriam Webster for a dictionary API key.

7. Add the bot to your Discord server.

8. Add the following variables to your environment variables:

```bash
export dictionary_bot_token=<your bot token>
export dictionary_api_token=<your api token>
```
Run the bot using the following command:

```bash
docker-compose up --build
```
Contributing
If you want to contribute to DictionaryBot, feel free to submit a pull request. 

License
DictionaryBot is released under the MIT License.