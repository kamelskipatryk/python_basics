
'''
Przygotuj fukncję, która na podstawie wysokości oraz długości podstawy wyświetli (print) pole trójkąta.
capsys -> czy funkcja dobrze liczy
(a*h)/2
'''

def get_triangle_field(base:int, height:int) -> float:
    print(base * height / 2)

def test_get_triangle_field(capsys):
    # given
    base = 10
    height = 8

    # when
    get_triangle_field(base, height)
    out, err = capsys.readouterr()

    #then
    assert out == '40.0\n'




