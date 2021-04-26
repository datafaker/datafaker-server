# datafaker/rest-server

> The REST API server for datafaker tools

## Getting started

Create a virtual environment:

```shell
python3 -m venv .env
```

Activate the virtual environment:

```shell
source ./.env/bin/activate
```

Upgrade python tools:

```shell
python3 -m pip install --upgrade pip setuptools wheel
```

Install requirements:

```shell
python3 -m pip install -r requirements.txt
```

```shell
PYTHONPATH=./src python3 src/app.py
```