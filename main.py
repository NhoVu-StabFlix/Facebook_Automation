import time

from FBHelper import FBHelper


class FbAuto:
    Chrome = FBHelper()
    Chrome.login()
    islogin=Chrome.check_login()
    if islogin:
        Chrome.add_friend()


if __name__ == '__main__':
    FbAuto()
