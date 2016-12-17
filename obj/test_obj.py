import obj as o

def test_trojkat():
	assert o.Trojkat().angles == 3

def test_czworokat():
	assert o.Czworokat().angles == 4

def test_prostokat_pole():
	assert o.Prostokat(2,3).pole() == 6

def test_prostokat_obwod():
	assert o.Prostokat(2,3).obwod() == 10

def test_kwadrat_obwod():
	assert o.Kwadrat(2).obwod() == 8

def test_kwadrat_pole():
	assert o.Kwadrat(2).pole() == 4

def test_trapez_obwod():
	assert o.Trapez(6,6,2,2).obwod() == 16

def test_kwadrat_pole():
	assert o.Trapez(6,6,2,2).pole() == 12