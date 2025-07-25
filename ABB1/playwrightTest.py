from playwright.sync_api import sync_playwright

def login_to_sunnyportal(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"})

        page.goto("http://iortu.com/", wait_until="networkidle")

        # 로그인 폼 입력
        page.fill("input[name='usrId']", username)
        page.fill("input[name='usrPw']", password)

        # 로그인 제출 버튼 클릭
        page.click("zr-touch[type='submit']")
        page.wait_for_load_state("networkidle")

        # 로그인 후 페이지 확인
        print("현재 URL:", page.url)
        print("페이지 타이틀:", page.title())

        while True:
            try:
                # '다음' 버튼 기다리기 (최대 3초)
                next_btn = page.wait_for_selector("zr-touch.zr-button.x48.next >> text=다음", timeout=3000)
                next_btn.click()
                print("다음 버튼 클릭")
                # 클릭 후 잠시 대기 (팝업 전환 시간)
                page.wait_for_timeout(1000)
            except TimeoutError:
                print("더 이상 다음 버튼 없음, 팝업 종료")
                break

        browser.close()

# 예시 호출 (아이디/비밀번호 직접 입력)
login_to_sunnyportal("케이솔라", "1234")  # Replace with actual credentials