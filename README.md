# Demo

## Идея
Вообще для этой задачи идеально подходит streamlit если нужно показывать графики (быстро и просто). Для сбора информации сделал бы модуль который ходит к АПИ погоды или к АПИ валют. Закешировал бы функции, примерно на 10 секунд для валют, 30 для погоды, т.к. на таких сайтах есть лимиты по запросам.

## Что удалось
По погоде достал данные (https://open-meteo.com/en/docs#latitude=40.71&longitude=-74.01&hourly=temperature_2m), но не успел правильно график построить
По валютам нашел сайт для данных (https://exchangerate.host/#/docs)

## Запуск
```
cd src
streamlit run ⏺Main.py --server.port 5000
```