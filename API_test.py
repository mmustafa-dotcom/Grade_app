import requests

def test_simple_post():
    url = "http://127.0.0.1:8000/api/calculate_grade"
    data = {
        "a": 98, "b": 90, "c": 90, "d": 100, "e": 100, "f": 100
    }

    response= requests.post(url, json=data)
    assert response.status_code == 201


def test_post_missing_field():
    url = "http://127.0.0.1:8000/api/calculate_grade"
    data = {
        "a": 98, "b": 90, "c": 90, "d": 100, "e": 100
        # f yoxdur
    }

    response = requests.post(url, json=data)

    assert response.status_code == 400