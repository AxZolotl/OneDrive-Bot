from urllib.parse import urlparse, parse_qs
from configparser import SectionProxy
from msal import ConfidentialClientApplication

class Graph:
    settings: SectionProxy

    def __init__(self, config: SectionProxy):
        self.settings = config
        app_id = self.settings['CLIENT_ID']
        client_secret = self.settings['CLIENT_SECRET']
        tenant_id = self.settings['TENANT_ID']
        graph_scopes = self.settings['SCOPES'].split(' ')
        
        authority = f"https://login.microsoftonline.com/{tenant_id}"
        
        client = ConfidentialClientApplication(
            client_id=app_id,
            client_credential=client_secret,
            authority=authority
        )
        
        response_url = 'https://localhost:8000/getToken?code=0.AVQAjQVpL7qO3k2RzmwjdEhXMfWmQeHdDSRIn_BEDuV83olUAL4.AgABAAIAAAD--DLA3VO7QrddgJg7WevrAgDs_wUA9P9Zf89SwYvl4PjbOdTEFX45CGeuUGkwhIbQew8XRavi-f9fHYP1zpjhMdCYe8_b5mDCdT7XLRwYTiyGvisbEg-O9QOosVp6U3KZDQXxFvGY9TGCj4LatTtivGyNwMfg91DwRWr64_-hajBnSAcWGjqc-VgT2wcr-j7otK6ogfgHwQjVQuL0prIqCuEQ_SomudvQzppB2wyHZnWWkUOmwat8Omy1PFYxLi4Su-Ivtz__IHTW0yt0Kt-_iHDNXXKys9OxmBKAw9rtQHpPPGRnABMhnZccqo9o6IHhoFk4n8PLf41QZGNf2YkCWwzksBwMgG7W0EdUE9p6BK7-Ss8zPcrr8v8CLk_E1PBsUK9Jvi-veB1wHKmOECpW5gTzxCYGtGbRtMsulOYmMyeaYbQ24ZIdxtV2DsK9eP8F5UWmo0h-ieVtd9jtFx3x4s3YgdtUxjKfuBs3CGxlB95I_2ARuNIGxI46JxYgjlYO0ECwQT9TH7gZaW-_OOEtaSD_LTdF_ps2FfLzUGWTktjxVZlGcU0M_cwV9HsNCn2VlC23tFdN50111tcFxHQywh34C-YrwCn3H0Vtn4K1fc8_xswxgdTly-mqRZO6Qo9Nqh-Ivd8zeDyUKYDQ2hYeWsy2yxtlZvi0ulibmLhSJ5kr1GvAD9ZQH3xWwIsb1W5HB9A6yJWlwxWba7CWVp50H1OzbNZJWoSVQRD2rJ91k02BBAjED6iloSl0xMCUXQdXuK45CXb97D2PsFl9Nan08loBo9cQ4jVBw7QxNhos15uvM0W8MQEZBYW1&session_state=bc38fd16-2b28-47e0-82f4-2f39d82fa328#'
        query_dict = parse_qs(urlparse(response_url).query)
        auth_code = query_dict['code'][0]
        print(auth_code)
        access_token = client.acquire_token_by_authorization_code(code=auth_code, scopes=graph_scopes)
        print(access_token)