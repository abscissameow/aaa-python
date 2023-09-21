def step3_umbrella_meow():
    print('Утка крикнула "мяу!" и все в баре обернулись. Она немного смущена.')

def step3_umbrella_purr():
    print('Утка замурлыкала "мурр..." и бармен подмигнул ей. Видимо, ей удалось произвести впечатление!')


def step2_umbrella():
    print('Утка взяла зонтик. Что она теперь скажет - "мяу" или "мур"?')
    option = ''
    options = {'мяу': "мяу", 'мур': "мур"}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option] == "мяу":
        return step3_umbrella_meow()
    return step3_umbrella_purr()

def step2_no_umbrella():
    print(
        'Бум! Вы превратили утку в свынюшку 🐷'
    )

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар.'
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

if __name__ == '__main__':
    step1()