from FBHelper import FBHelper


class FbAuto:
    Chrome = FBHelper()
    Chrome.login()
    isLoginFB=Chrome.check_login()
    if isLoginFB:
        Chrome.surf_newsfeed()



if __name__ == '__main__':
    FbAuto()
