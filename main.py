words = {
    'лол' : 'Что то очень смешное',
    'кринж' : 'Стыд',
    'агриться' : 'злиться'
}
while True:
    run = True
    word = input('Введите слово:').lower
    if word in words:
        print(words[word])
    else:
        print('такого слова нет')
