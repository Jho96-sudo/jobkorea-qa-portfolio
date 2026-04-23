import pytest

@pytest.mark.p2
def test_filter_reset_to_default(logged_in_page):
    """
    [잡코리아 TC-009] 필터 초기화 기능
    → [SauceDemo] 정렬 필터 변경 후 기본값 복귀
    """

    page = logged_in_page
    sort = page.locator(".product_sort_container")

    # 기본값 확인
    default = sort.input_value()
    assert default == "az", f"기본 정렬값이 'az'여야 합니다. 실제: {default}"
    
    # 필터 변경
    sort.select_option("lohi")
    assert sort.input_value() == "lohi"

    # 기본값으로 초기화
    sort.select_option("az")
    assert sort.input_value() == "az", "필터 초기화 후 기본 정렬로 복귀해야 합니다."
    
    # 초기화 후 목록 정상 표시 확인
    items = page.locator(".inventory_item").all()
    assert len(items) > 0, "필터 초기화 후 상품 목록이 표시되어야 합니다."