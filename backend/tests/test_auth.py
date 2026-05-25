from app.core.security import create_access_token, decode_access_token, hash_password, verify_password


def test_auth_contract():
    password_hash = hash_password("science-pass")
    assert verify_password("science-pass", password_hash)
    token = create_access_token("kantkrishan0206@gmail.com", "secret", "admin")
    claims = decode_access_token(token, "secret")
    assert claims["role"] == "admin"
