from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from pydantic import SecretStr

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)

SECTRET = "SECRET"

def get_jwt_statagy() -> JWTStrategy:
    return JWTStrategy(secret=SECTRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name= "jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_statagy,
)