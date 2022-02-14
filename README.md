## Aiogram3.0 with Dialog on webhooks template
### Install
```sh
pip install -U --pre -r requirements.txt
```

### Set envs
```sh
cp .env.sapmle .env
```
```sh
BOT_TOKEN # from botfather
WH_HOST # domain where your web app hosted
APP_PORT # on which port your web app started
```

### Start
```sh
python main.py
```

### Localization
```sh
pybabel extract dialogs -o locales/dd.pot # i18n init
pybabel init -i locales/dd.pot -d locales -D dd -l ru # add new lang
pybabel update -i locales/dd.pot -d locales -D dd # update translate files
pybabel compile -d locales -D dd # compile
```

### Diagrams generating
```sh
python diagram.py
```
