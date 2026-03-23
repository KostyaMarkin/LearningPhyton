phrases_str = input("Введите фразы, разделенные ';': ")
phrases = phrases_str.split(';')
lengths = [len(phrase.split()) for phrase in phrases]
print("Исходный список фраз:", phrases)
print("Количество слов в каждой фразе:", lengths)