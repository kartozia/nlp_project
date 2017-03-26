# Проект по препроцессингу
## Токенизация электронных писем
### :zap:Команда:zap:
* Бибаева Мария — *разработка и тестирование*
* Картозия Инга — *аналитическая часть и general management*
* Анастасия Мельник — *разработка и тестирование*

## Checklist:

- [x] [Техническое задание](./TZ.md)
- [x] [Корпус текстов, на котором мы обучались и тестировали программу](./ling_emails.txt)
- [x] [Корпус текстов, на котором мы тестировали программу](./test.txt)
- [x] [Выдача прогона на тестовом корпусе](./output.txt)
- [x] [Резюме по статье](./article_review.md)
- [x] Отчет (данный файл)
- [x] [Презентация](./NLPproject.pdf)
- [x] Доп. задание по аббревиатурам: [def abbr_freq](./tokenizator_last.ipynb) и [результат](./abbreviations.txt)

## [Результаты тестирования](./output.txt) на 500 токенах нашего корпуса:

Точность: **0.99564**

Полнота: **0.99132**

## Для сегментации предложений (на том же материале):

Точность: **0.951**

Полнота: **0.866**

## Результаты тестирования [на нашем резюме по статье](./test_smth.txt):

Точность: **0.99071**

Полнота: **1**


## [Для сегментации предложений](./output_sents.txt) (на материале статьи выше):

Точность: **0.934**

Полнота: **0.866**

## Проблема с сегментацией предложений:

> 'С уважением, Команда Google Аккаунтов Не отвечайте на это сообщение.'

> С уважением, Учебный офис Здравствуйте, lingua!'

> Дорогие студенты, Завтра мы ждем вас ВСЕХ на собрании с руководителем школы лингвистики Е.В.'

В общем-то, мы пробовали добавить в код условие, что письмо обычно начинается с устойчивых сочетаний: Дорогие, Уважаемые, Доброй ночи, Добрый вечер/день, Доброе утро, Привет, Здравствуйте, Любимые. Конец письма также довольно формализован: Ваш, Ваша, С наилучшми пожеланиями, Всего доброго, С Уважением.

Ваш МА — одно предложение

Дорогие студенты — одно предложение

Остальной текст письма делится на предложения по стандартному принципу, т.е. если **слева** от точки(или другого знака конца предложения) есть незаглавная буква, а **справа** пробел + слово с заглавной буквы.


## Наши коды:
- [экстрактор писем из архива](./mail_corpus.ipynb)
- [убер-код, просто попробуйте](./tokenizator_last.ipynb)


