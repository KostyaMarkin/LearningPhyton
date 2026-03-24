import re


def find_datetime(text):

    pattern = r'\b(20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\s+([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\b'

    matches = re.findall(pattern, text)

    # Форматируем результат
    results = []
    for match in matches:
        formatted = f"{match[0]}-{match[1]}-{match[2]} {match[3]}:{match[4]}:{match[5]}"
        results.append(formatted)

    return results


# Основная программа
if __name__ == "__main__":
    print("Введите текст для поиска дат и времени (для завершения введите пустую строку):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)

    # Поиск дат и времени
    dates = find_datetime(text)

    # Вывод результатов
    print("\nНайденные даты и время:")
    if dates:
        for date in dates:
            print(date)
    else:
        print("Даты и время не найдены.")