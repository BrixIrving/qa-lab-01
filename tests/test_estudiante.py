from src.estudiante import evaluar_aprobacion

def test_estudiante_aprobado():
    assert evaluar_aprobacion(15) == "Aprobado"

def test_estudiante_desaprobado():
    assert evaluar_aprobacion(5) == "Desaprobado"