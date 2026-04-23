import pytest

@pytest.mark.p2
def test_sort_name_a_to_z(logged_in_page):
    """
    [잡코리아 TC-013] 정렬 기능 최신순
    → [SauceDemo] 이름 A→Z 정렬
    """

    page = logged_in_page
    page.locator(".product_sort_container").select_option("az")

    names = [
        n.text_content()
        for n in page.locator(".inventory_item_name").all()
    ]
    assert names == sorted(names), "이름 A→Z 정렬 후 알파벳 순서여야 합니다."
    
@pytest.mark.p2
def test_sort_price_high_to_low(logged_in_page):
    """가격 내림차순 정렬"""
    page = logged_in_page
    page.locator(".product_sort_container").select_option("hilo")

    prices = [
        float(p.text_content().replace("$", ""))
        for p in page.locator(".inventory_item_price").all()
    ]
    assert prices == sorted(prices, reverse=True), "가격 내림차순 정렬이 적용되어야 합니다."