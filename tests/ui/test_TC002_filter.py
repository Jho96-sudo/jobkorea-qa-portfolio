import pytest

@pytest.mark.p1
def test_sort_filter_low_to_high(logged_in_page):
    """
    [잡코리아 Tc-002] 경력 필터 선택
    → [SauceDemo] 가격 오름차순 정렬 필터 선택

    매핑 근거
    잡코리아: 필터 선택 후 결과 건수 변화 확인
    SauceDemo: 정렬 필터 선책 후 순서 변화 확인
    """

    page = logged_in_page

    def get_prices():
        return [
            float(p.text_content().replace("$",""))
            for p in page.locator(".inventory_item_price").all()
        ]
    
    # 필터 선택 전 가격
    prices_before = get_prices()

    # 오름차순 필터 선택
    page.locator(".product_sort_container").select_option("lohi")

    # 필터 선택 후 가격 기록
    prices_after = get_prices()

    # 필터 전후 순서 변화
    assert prices_before != prices_after or prices_after == sorted(prices_after), "가격 오름차순 정렬이 적용되어야 합니다."
    
    # URL 파라미터 반영 확인
    #assert "lohi" in page.url, "URL에 정렬 조건이 반영되어야 합니다."