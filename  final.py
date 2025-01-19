username = input('Введите имя пользователя:')
title = []
result=title.append(input('Введите заголовок заметки:'))
result2=title.append(input('Введите заголовок заметки:'))
result3=title.append(input('Введите заголовок заметки:'))
content = input('Введите описание заметки:')
status = input('Введите статус заметки:')
created_date = input('Введите дату создания заметки в формате "день-месяц-год" пример 01-01-2001:')
issue_date = input('Введите дату истечения заметки (дедлайн) в формате "день-месяц-год" пример 01-01-2001:')
note = [
    username,
    content,
    status,
    created_date,
    issue_date,
    title
]
print('Имя пользователя:', note[0],
      '\nОписание заметки:', note[1],
      '\nСтатус заметки:', note[2],
      '\nДата создания заметки:', note[3],
      '\nДедлайн:', note[4],
      '\nЗаголовоки:', note[5]
)