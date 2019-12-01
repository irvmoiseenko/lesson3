with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(len(content))  # количество символов в тексте = длине получившейся строки'
    print(len(content.replace('\n', ' ').split(' ')))  # количество слов
    
    # заменены точки на восклицательные знаки
    print(content.replace('.', '!'))
