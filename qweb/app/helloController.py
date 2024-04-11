from autowired import component

from qweb.libs.authProvider import AuthProvider
from qweb.libs.controller import Controller
from qweb.libs.decorators import qroute, qauth


@component
class HelloController(Controller):
    @qroute("/api/hello")
    def hello(self):
        return ("Hello")

    @qroute("/api/hello/<name>")
    def helloName(self, name):
        return ("Hello " + name)

    @qroute("/api/auth/<name>")
    @qauth(AuthProvider)
    def helloAuth(self, name):
        return ("Hello " + name)

    @qroute("/api/auth/prova")
    @qauth(AuthProvider, ["prova"])
    def helloAuthProvaOk(self):
        return ("Hello Prova")

    @qroute("/api/auth/fault")
    @qauth(AuthProvider, ["fault"])
    def helloAuthProvaKo(self):
        return ("Hello Fault")
