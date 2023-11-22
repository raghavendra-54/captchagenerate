import random
 
def checkCaptcha(captcha, user_captcha):
    if captcha == user_captcha:
        return True
    return False
 

def generateCaptcha(n):
     
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
     
    captcha = ""
    while (n):
        captcha += chrs[random.randint(1, 1000) % 62]
        n -= 1
    return captcha
 
captcha = generateCaptcha(9)
print(captcha)
 
print("Enter above CAPTCHA:")
usr_captcha = input()
 
if (checkCaptcha(captcha, usr_captcha)):
    print("CAPTCHA Matched")
else:
    print("CAPTCHA Not Matched")