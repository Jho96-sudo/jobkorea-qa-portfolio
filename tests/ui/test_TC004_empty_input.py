import pytest

@pytest.mark.p1
def test_empty_username_shows_error(page):
    """
    [잡코리아 TC-004] 빈 검색어 처리 → Fail
    → [SauceDemo] 빈 아이디 입력 시 오류 메시지 표시 → Pass

    비교 포인트
    잡코리아: 빈 입력 시 안내 메시지 미표시 (Fail)
    SauceDemo: 빈 입력 시 오류 메시지 정상 표시 (Pass)
    """

    page.goto("https://www.saucedemo.com")
    page.locator("#login-button").click()

    error = page.locator("[data-test='error']")
    assert error.is_visible(), "빈 입력 시 오류 메시지가 표시되어야 합니다."
    assert "Username is required" in error.text_content(), "안내 메시지 내용이 올바르지 않습니다."
    
@pytest.mark.p1
def test_space_only_input(page):
    """
    [잡코리아 TC-006] 공백 스페이스 검색어 처리
    → [SauceDemo] 공백만 입력 시 오류 메시지 표시
    """

    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill(" ")
    page.locator("#password").fill(" ")
    page.locator("#login-button").click()

    error = page.locator("[data-test='error']")
    assert error.is_visible(), "공백 입력 시 오류 메시지가 표시되어야 합니다."