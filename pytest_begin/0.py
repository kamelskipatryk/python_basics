# Przygotuj funkcję sprawdzającą czy osoba o przekazanym wieku jest osobą pełnoletnią.



def is_adult(age:int) -> bool:
    return age >= 18

print(is_adult(12))
print(is_adult(18))
print(is_adult(19))

def test_is_adult():
    # given - wszystko to co będzie służyło do przeprowadzenia testu
    age = 18

    # when - metody, które dają nam wynik
    result = is_adult(age)

    # then - sprawdzamy otrzymany wynik
    assert result

def test_is_not_adult():
    assert not is_adult(17)
    assert not is_adult(3)


