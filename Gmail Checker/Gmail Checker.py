import requests , re , threading as th
Url_Get_Cookies = "https://accounts.google.com/SignUp?continue=https%3A%2F%2Fwww.google.com%2F&hl=en&dsh=S-553617478%3A1614242741811960&gmb=exp&biz=false"
cookies = ""
email_list  = open("list.txt", "r").read().splitlines()
def check(email):
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (Linux; Android 7.1.2; G011A Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36",
                'Cookie': f"1P_JAR=2021-02-23-19; NID=210={cookies}; __Host-GAPS=1:GV8kzgewC2diEGhLxP46yc0RnUbE3w:b2UyjKc8vOsTSKWu",
                'ContentType': "application/x-www-form-urlencoded;charset=UTF-8",
                'Host': "accounts.google.com",
                'Accept': "*/*",
                "Google-Accounts-XSRF": "1"
            }
            data = {'continue': 'https://www.google.com/?gws_rd=ssl&dsh=S486615459:1614110174398934', "hl": "ar",
                    "flowName": "GlifWebSignIn", "flowEntry": "SignUp",
                    "f.req": "[" + cookies + ",""by404.erroz"",""its""," + email + ",false]",
                    "azt": "AFoagUV7a5sfFTSy_fbzkMiYW9ZXRGkAcA:1614155570432", "cookiesDisabled": "false",
                    "deviceinfo": "[null,null,null,[],null,SA,null,null,[],GlifWebSignIn,null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,0,null,false]",
                    "gmscoreversion": "undefined"}
            response = requests.post(
                "https://accounts.google.com/_/signup/webusernameavailability?hl=ar&_reqid=208973&rt=j", data=data,
                headers=headers).text
            if '[[["gf.wuar",1,[]' in response:
               return True
            elif '[[["er",null,null,null,null,400,null,null,null,3]' in response:
                get_cookie()
                check(email)
            else:
                return False
        except Exception:
             get_cookie()
             check(email)
def get_cookie():
    global cookies
    ress = requests.get(Url_Get_Cookies, headers={"Cookie": "1P_JAR=2021-02-23-19; NID=210=IaV6oTvVVkYHNAF4jAd6QCgzeVwo8H6_-WrWJX8468zCf4p6izAYX0CIggELGI-ETd_s3StcGbVyL18sOiLgGlEHQQ8IeeMSFWiQazsJD69QOeAQVDGIlSQe3KbY70rfkYH9tSSbmIKJPwsKNy7fr2YH8H-UqIpAIiNl5Nawf7w","X-Requested-With":"com.android.browser","ContentType":"application/x-www-form-urlencoded;charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; G011A Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36"})
    cookies ="AEThL"+ re.search("&quot;AEThL(.*?)&quot", ress.text).groups(0)[0]
th.Thread(target=get_cookie).start()
print("""
             [ Gmail Checker ]
             [ Codded By @404.erroz ] 
             [ github.com\itserrozz ]\n------------------------------------------------""")
input("Press Enter To Start Check ..")
available = 0
taken = 0
for email in email_list:
    if check(email):
        available += 1
        print(f"          Available [ {available} ] | Taken [ {taken} ]",
              end='\r')
    else:
       taken+=1
print("\nFinished Check All Emails")
print(f"[ Available : {available} | Taken : {taken} ]")
input("Press Enter to exit .. ")
exit(code=0)