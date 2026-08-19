from app.main import suma

def test_suma():
    # ERROR INTENCIONAL PARA PARTE 4: 2 + 3 debería ser 5, pero pusimos 99
    assert suma(2, 3) == 99
