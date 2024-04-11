from autowired import component

from qweb.libs.authProvider import AuthProvider
from qweb.libs.controller import Controller
from qweb.libs.decorators import qroute, qauth


@component
class HelloController(Controller):
    # def __init__(self, authProvider:AuthProvider):
    #     self.auth_provider = authProvider
    #
    # def mapRoutes(self, controllerMapper):
    #     controllerMapper.get("/api/auth/fault", self.hello).withAuth(self.auth_provider).withPermissions(["fault"]).build()
    #     controllerMapper.get("/api/hello", self.hello).build()
    #     controllerMapper.get("/api/hello/<name>", self.helloName).build()
    #     controllerMapper.get("/api/auth/<name>", self.helloName).withAuth(self.auth_provider).build()
    #     controllerMapper.get("/api/auth/prova", self.hello).withAuth(self.auth_provider).withPermissions(["prova"]).build()

    @qroute("/api/hello")
    def hello(self):
        return ("Hello")

    @qroute("/api/hello/<name>")
    def helloName(self,name):
        return ("Hello "+name)

    @qroute("/api/auth/<name>")
    @qauth(AuthProvider)
    def helloAuth(self,name):
        return ("Hello "+name)

    @qroute("/api/auth/prova")
    @qauth(AuthProvider,["prova"])
    def helloAuthProvaOk(self):
        return ("Hello Prova")

    @qroute("/api/auth/fault")
    @qauth(AuthProvider,["fault"])
    def helloAuthProvaKo(self):
        return ("Hello Fault")
