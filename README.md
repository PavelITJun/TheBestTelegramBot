# Telegram Бот с Поддержкой Оплаты, Геолокации, Регистрации и Уведомлений

Этот бот создан исключительно в учебных целях и демонстрирует различные возможности взаимодействия с пользователями через Telegram. В нем реализованы следующие функции:

### 1. Оплата и выбор товара
Пользователь может выбрать товар или услугу, оформить покупку и произвести оплату через встроенные платежные системы Telegram. Процесс оплаты сопровождается интуитивно понятными сообщениями и подтверждением успешного платежа.

### 2. Передача локации и номера телефона
Бот может запрашивать у пользователя доступ к его геолокации и номеру телефона через встроенные кнопки. Это может быть полезно для сервисов доставки или других интерактивных сценариев.

### 3. Голосования
Пользователь может инициировать голосование по нажатию кнопки. Это подходит для получения обратной связи или проведения опросов.

### 4. Регистрация через машину состояний
Система регистрации реализована с использованием машины состояний, что позволяет последовательно собирать необходимые данные от пользователя (например, имя, номер телефона, адрес) и сохранять их в системе.

### 5. Уведомления по расписанию с оплатой
Бот поддерживает отправку уведомлений по заданному расписанию, в том числе с возможностью оплаты за предоставленные услуги. Пользователи могут подписаться на определенные уведомления и получать их в назначенное время с возможностью оплаты.

### 6. Встроенная клавиатура
Бот использует встроенные кнопки для удобного взаимодействия. Пользователь может быстро выбрать нужную функцию, например, отправить свои данные, начать оплату или инициировать голосование.

## Установка и Настройка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/username/telegram-bot.git
    ```

2. Создайте и активируйте виртуальное окружение (требуется Python 3.9 или выше):

    Для активации на Windows:
    ```bash
    .\venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Получите токен для работы с Telegram API:
    - Создайте бота через [BotFather](https://t.me/BotFather) и получите API токен.
    - Добавьте токен в файл конфигурации `input`:
      ```bash
      TOKEN=<Ваш_Токен>
      ADMIN_ID=<Ваш ID в телеграм>
      ```
      
5. Запустите бота:

    ```bash
    python main.py
    ```

Теперь бот готов к использованию, и его функциональность включает разнообразные возможности взаимодействия с пользователями.
