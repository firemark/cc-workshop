import figures


def test_Trojkat_katy():
    assert figures.Trojkat.katy == 3


def test_trojkat_pole():
    assert figures.Trojkat(4, 10).pole() == 0.5 * 4 * 10


def test_trojkat_wymiary():
    assert figures.Trojkat(4, 15.7).a == 4.
    assert figures.Trojkat(4, 15.7).h == 15.7


def test_Czworokat_katy():
    assert figures.Czworokat.katy == 4


def test_Prostokat_katy():
    assert figures.Prostokat.katy == 4


def test_prostokat_pole():
    assert figures.Prostokat(3.1, 2.5).pole() == 3.1 * 2.5


def test_prostokat_obwod():
    assert figures.Prostokat(3.1, 2.5).obwod() == 2 * 3.1 + 2 * 2.5


def test_Kwadrat_katy():
    assert figures.Kwadrat.katy == 4


def test_prostokat_pole():
    assert figures.Kwadrat(3.1).pole() == 3.1**2


def test_prostokat_obwod():
    assert figures.Kwadrat(3.1).obwod() == 4 * 3.1


def test_Trapez_katy():
    assert figures.Trapez.katy == 4


def test_trapez_pole():
    assert figures.Trapez(3.1, 2.5, 7.8).pole() == 0.5 * (3.1 + 2.5) * 7.8
