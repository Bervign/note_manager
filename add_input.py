username = input('Введите имя пользователя:')
title = input('Введите заголовок заметки:')
content = input('Введите описание заметки:')
status = input('Введите статус заметки:')
created_date = input('Введите дату создания заметки в формате "день-месяц-год" пример 01-01-2001:')
issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год" пример 01-01-2001:')
print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print(f'Дата создания заметки, {created_date[:-5]}')
print(f'Дедлайн, {issue_date[:-5]}')
