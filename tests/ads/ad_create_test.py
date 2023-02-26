import pytest


@pytest.mark.django_db
def test_create_ad(client, access_token, user, category):
    data = {"author": user.pk,
            "category": category.pk,
            "name": "Ноутбук",
            "price": 45000,
          }
    expected_data = {
        "id": 21,
        "is_published": False,
        "name": "Ноутбук MacBook Air",
        "price": 45000,
        "description": None,
        "image": None,
        "author": user.pk,
        "category": category.pk
        }

    response = client.post(f"/ad/", data, HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data
