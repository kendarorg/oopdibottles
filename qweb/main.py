import qweb

from qweb.applicationcontext import ApplicationContext
from qweb.libs.bottleService import BottleService


def main():
    ctx = ApplicationContext(qweb)
    bottleService: BottleService = ctx.resolve(BottleService)
    bottleService.run(host='', port=8080, debug=True)


if __name__ == '__main__':
    main()
