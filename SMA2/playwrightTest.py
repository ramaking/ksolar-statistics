from playwright.sync_api import sync_playwright

def login_to_sunnyportal(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.sunnyportal.com", wait_until="networkidle")

        # 쿠키 동의
        try:
            page.click("a.cmpboxbtnyes", timeout=5000)
            print("쿠키 동의 완료")
        except:
            print("쿠키 동의 버튼 없음")

        # 로그인 페이지 이동 버튼 클릭
        page.click("#ctl00_ContentPlaceHolder1_Logincontrol1_SmaIdLoginButton")
        page.wait_for_load_state("networkidle")

        # 로그인 폼 입력
        page.fill("input[name='username']", username)
        page.fill("input[name='password']", password)

        # 로그인 제출 버튼 클릭
        page.click("button[type='submit']")
        page.wait_for_load_state("networkidle")

        # 로그인 후 페이지 확인
        print("현재 URL:", page.url)
        print("페이지 타이틀:", page.title())

        # Plants 페이지 이동
        page.goto("https://www.sunnyportal.com/Plants", wait_until="networkidle")
        print("Plants 페이지 타이틀:", page.title())
        print(page.content())

        browser.close()

# 예시 호출 (아이디/비밀번호 직접 입력)
login_to_sunnyportal("k2248163347@hanmail.net", "Ksolar1234!")  # Replace with actual credentials