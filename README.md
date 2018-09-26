# Lapsang 正山

Lapsang is a game developed to learn a foreign language.

It will be best appreciated by 2 players of different native languages.

While playing, you can contribute to the [Tatoeba project](https://tatoeba.org).

## Install

This will install Falcon (API framework) and gunicorn (server).

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
gunicorn play:api
```
