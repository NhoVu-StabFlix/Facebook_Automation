from FBHelper import FBHelper

class FbAuto():
    Chrome = FBHelper()
    Chrome.login()
    isLogin=Chrome.check_login()




if __name__ == '__main__':
    FbAuto()
