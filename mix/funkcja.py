from cgi import print_arguments


def pierz():
    print('wyprane')

def zrob_kanapke(chlebek, smarowdilo, wedlina):
    print('robie kanapke')
    print(f'{chlebek}')
    print(f'{smarowdilo}')
    print(f'{wedlina}')
    return 'tekst'

zmienna = zrob_kanapke('pszenny', 'maselko', 'szynka')
print(zmienna)