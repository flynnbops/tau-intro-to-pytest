import pytest
import requests


# This is a public instance of restful booker, so returend data will change
@pytest.mark.api
@pytest.mark.restfulbooker
def test_restfulbooker_booking():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response = requests.get(url)
    body = response.json()

    print(body)

    assert response.ok
    assert 'Jim' in body['firstname']
    assert 'Brown' in body['lastname']
