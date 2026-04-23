import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}

@pytest.fixture(scope="module")
def auth_token():
    res = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "admin", "password": "password123"},
        headers=HEADERS
    )
    assert res.status_code == 200, "인증 실패"
    return res.json()["token"]

@pytest.fixture(scope="module")
def booking_id(auth_token):
    """테스트용 예약 생성 후 ID 반환"""
    payload = {
        "firstname":    "QA",
        "lastname":     "Tester",
        "totalprice":   150,
        "depositpaid":  True,
        "bookingdates": {
            "checkin":  "2026-05-01",
            "checkout": "2026-05-10"
        },
        "additionalneeds": "잡코리아 QA 포트폴리오 테스트"
    }

    res = requests.post(
        f"{BASE_URL}/booking",
        json=payload, headers=HEADERS)
    assert res.status_code == 200
    return res.json()["bookingid"]
    
@pytest.mark.api
def test_get_booking_list():
    """[TC-001 매핑] 검색 결과 목록 정상 표시"""
    res = requests.get(f"{BASE_URL}/booking")
    assert res.status_code == 200
    assert len(res.json()) > 0, \
        "예약 목록이 1건 이상 조회되어야 합니다."
    
@pytest.mark.api
def test_filter_booking_by_name():
    """[TC-002 매핑] 필터 적용"""
    res = requests.get(
        f"{BASE_URL}/booking",
        params={"firstname": "QA"}
    )
    assert res.status_code == 200

@pytest.mark.api
def test_get_single_booking(booking_id):
    """[TC-005 매핑] 단건 조회 시 필수 필드 확인"""
    res = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert res.status_code == 200

    data = res.json()
    assert "firstname"          in data
    assert "lastname"           in data
    assert "totalprice"         in data
    assert "bookingdates"      in data
    assert data["firstname"] == "QA"

@pytest.mark.api
def test_empty_required_field():
    """[TC-004 매핑] 필수값 누락 시 오류 응답"""
    payload = {
        "lastname":     "Tester",
        "totalprice":   100,
        "depositpaid":   True,
        "bookingdates": {
            "checkin":  "2026-05-01",
            "checkout": "2026-05-10"
        }
    }
    
    res = requests.post(
        f"{BASE_URL}/booking",
        json=payload, headers=HEADERS)
    assert res.status_code in [400, 500], \
        f"필수값 누락 시 오류 응답이어야 합니다. 실제: {res.status_code}"
    
@pytest.mark.api
def test_delect_booking(auth_token, booking_id):
    """[TC-018 매핑] 삭제 후 404 확인"""
    res = requests.delete(
        f"{BASE_URL}/booking/{booking_id}",
        headers={
            "Cookie":   f"token={auth_token}",
            "Content-Type": "application/json"
        }
    )
    assert res.status_code in [200, 201]

    res_after = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert res_after.status_code == 404, \
        "삭제된 예약 조회 시 404가 반환되어야 합니다."