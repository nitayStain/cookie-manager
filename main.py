
def StringToCookieDict(cookies_content: str):
    """
    Returns a new dictionary that contains a special string convertion from the http request header
    Example:
        StringToCookieDict("now_date=02052022;") -> {"now_date": "02052022"}
    """
    if len(cookies_content) == 0 or not cookies_content:
        return {"🍪": "🍪"}
    idk_if_they_are_cookies = {}
    not_a_cookie = cookies_content.split(";")
    cookie_items = []
    if not not_a_cookie:
        return False
    for i in range(len(not_a_cookie)):
        if not_a_cookie[i] == "" or not_a_cookie[i] == " ":
            not_a_cookie.pop(i)
    for item in not_a_cookie:
        cookie_items.append(item.split("="))
    for a in cookie_items:
        idk_if_they_are_cookies[a[0]] = a[1]
    return idk_if_they_are_cookies


def CookieDictToString(cookies: dict):
    """
    Returns a special string value from a dictionary of cookies
    Example:
        CookieDictToString({"auth_token": "goz01kwsoAOSD01lz,c,;aasdoLASDO"}) -> "auth_token=goz01kwsoAOSD01lz,c,;aasdoLASDO;"
    """
    if len(cookies.items()) == 0 or not cookies.items():
        return "🍪"

    combinations = []
    for k, v in cookies.items():
        combinations.append(f"{k}={v}")

    return ";".join(combinations) + ";"
