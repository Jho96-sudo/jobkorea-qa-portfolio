import pytest

@pytest.mark.p1
def test_produt_list_displayed(logged_in_page):
    """
    [잡코리아 TC-001] 키워드 검색 정상 실행
    → [SauceDemo] 로그인 후 상품 목록 정상 표시
    
    매핑 근거
    잡코리아: 검색 결과 1건 이상 표시 
    SauceDemo: 상품 목록 6건 표시

    잡코리아: 공고 카드 회사명, 직무, 지역 표시 
    SauceDemo: 상품 카드 이름, 가격, 설명 표시
    """

    page = logged_in_page

    items = page.locator(".inventory_item").all()
    assert len(items) > 0, \
        "상품 목록이 1건 이상 표시되어야 합니다."
    
    first = items[0]
    name = first.locator(".inventory_item_name").text_content()
    price = first.locator(".inventory_item_price").text_content()
    desc = first.locator(".inventory_item_desc").text_content()

    assert name != "", "상품명이 표시되어야 합니다."
    assert price != "", "가격이 표시되어야 합니다."
    assert desc != "", "설명이 표시되어야 합니다."
    assert "$" in price, "가격에 $ 기호가 포함되어야 합니다."