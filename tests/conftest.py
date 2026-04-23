import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture(scope="function")
def page():
    """
    각 테스트마다 브라우저를 열고 닫는 fixture
    headless=False → 브라우저 창이 실제로 열림
    headless=True → 창 없이 백그라운드 실행
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def logged_in_page(page):
    """
    로그인 완료된 페이지를 제공하는 fixture
    """
    page.goto(BASE_URL)
    page.locator("#user-name").fill(USERNAME)
    page.locator("#password").fill(PASSWORD)
    page.locator("#login-button").click()
    page.wait_for_url("**/inventory.html")
    yield page