import os
from pathlib import Path

from autowired import component
from bottle import static_file

from qweb.libs.controller import Controller


def staticControllerCallbackFactory(m):
    return lambda: staticControllerRender(m)


def staticControllerRender(path):
    return static_file(path, "")


@component
class StaticController(Controller):

    def mapRoutes(self, controllerMapper):
        staticPathString = str(Path(__file__).resolve().parent.parent) + "/static"

        for currentpath, folders, files in os.walk(staticPathString):
            for file in files:
                content = Path(os.path.join(currentpath, file))
                subPath = str(content).replace(staticPathString, "")
                controllerMapper.get(subPath, staticControllerCallbackFactory("/static" + subPath)).build()
                if subPath.endswith("index.html") or subPath.endswith("index.htm"):
                    emtpy = str(content.parent).replace(staticPathString, "") + "/"
                    controllerMapper.get(emtpy, staticControllerCallbackFactory("/static" + subPath)).build()
