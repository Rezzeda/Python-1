Задача:

Система собирает информацию с датчиков, в ней есть модуль
логирования, который заносит в журнал все обращения к датчикам.
в системе есть модуль, выполняющий обращения для получения данных с
датчиков и модуль генерации html-представления.
запуск системы осуществляется из головного модуля.

выделим 5 модулей:
1. сбор информации с датчиков
2. логирование
3. UI (user interface)
4. HTML-генератор
5. главный модуль

1. data_provider
    get_temperature, get_pressure, get_wind_speed
2. logger
    temperature_logger, pressure_logger, wind_speed_logger
3. user_interface
    temperature_view, pressure_view, wind_speed_view
4. html_creator
    create
5. main