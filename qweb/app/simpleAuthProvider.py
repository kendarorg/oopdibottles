from autowired import component

from qweb.libs.authProvider import AuthProvider


@component
class SimpleAuthProvider(AuthProvider):
    def checkAuth(self, login, password):
        return (login == "admin" and password == "admin") or (login == "guest" and password == "guest")

    def checkPermission(self, login, permissions: [str]):
        if login == "admin" and "prova" in permissions:
            return True
        return False
