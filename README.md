# Тестовое задание greenatom

## Задание 1
*Какие шаги ты бы предпринял, если бы пользователь сказал, что API возвращает ему ошибку 500?*

Для начала необходимо понять, в каком именно месте возникает ошибка. Для этого можно прочитать логи. Когда причина ошибки выявлена, необходимо устранить причину ее возникновения, а также написать unit-тесты, чтобы в будущем автоматически запускать тестирование и убеждаться, что проблема не возникла снова.

## Задание 2
*Какие ты видишь проблемы в следующем фрагменте кода? Как его следует исправить? Исправь ошибку и перепиши код ниже с использованием типизации*
```python
def create_handlers(callback):
    handlers = []
    for step in range(5):
        # Добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda: callback(step))
    return handlers


def execute_handlers(handlers):
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
```
Необходимо передать аргумент в функцию callback через lambda

[Исправления](./task2.py)

## Задание 3
*Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы выше*

На сайте 774 тега и 478 из них содержат атрибуты

[Решение](./task3.py)

## Задание 4
*Напиши функцию на Python, которая возвращает текущий публичный IP-адрес компьютера (например, с использованием сервиса ifconfig.me)*

[Решение](./task4.py)

## Задание 5
*Напиши функцию на Python, выполняющую сравнение версий. Условия:* 
 - Return -1 if version A is older than version B
 - Return 0 if version A and B are equivalent
 - Return 1 if version A is newer than version B
 - Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1. 

[Решение](./task5.py)