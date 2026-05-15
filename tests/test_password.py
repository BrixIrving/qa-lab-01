from src.password import password_segura

def test_password_segura():
    assert password_segura("python123") == True

def test_password_insegura():
    assert password_segura("abc") == False