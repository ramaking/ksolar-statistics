import requests
from bs4 import BeautifulSoup

def login(user_id, password):
    session = requests.Session()
    login_url = "http://iplug.dasstech.com/loginRequest"
    login_data = {"id": user_id, "pass": password}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "Referer": "http://iplug.dasstech.com/login",
        "Origin": "http://iplug.dasstech.com"
    }
    session.post(login_url, data=login_data, headers=headers)
    return session

def get_project_list(session, page):
    url = f"http://iplug.dasstech.com/monitoring/getProjectList.json?currentPage={page}"
    res = session.get(url)
    return res.json().get("list", [])

def get_generation_stats(session, site_code, search_date, search_unit="month"):
    url = (
        f"http://iplug.dasstech.com/monitoring/dataSearch/netgenerationstats"
        f"?SITE_CODE={site_code}&SEARCH_DATE={search_date}&CALC_PRICE=&SEARCH_UNIT={search_unit}"
    )
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    rows = soup.select("table.tstyle1 tbody tr")
    result = {}
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            date = cols[0].get_text(strip=True)
            gen = cols[1].get_text(strip=True)
            result[date] = gen
    return result