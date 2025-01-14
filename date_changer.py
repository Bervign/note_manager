def process_string(input_string):
    if not input_string:  # Сначала проверяется, не является ли входная строка пустой. Если пустая, функция возвращает пустую строку
        return ""

    length = len(input_string) # Вычисляется длина строки
    if length > 8:
        return input_string[:-5]
    else:
        return input_string[:-3]

created_date = input('Введите дату создания заметки: ')
result1 = process_string(created_date)
print(f"дата создания:  {result1}")
issue_date = input('Введите дедлайн заметки: ')
result1 = process_string(issue_date)
print(f"дедлайн:  {result1}")