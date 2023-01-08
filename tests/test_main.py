
import pytest
from tests.data_for_tests import *


@pytest.mark.parametrize("url", [PARAMETRS1, PARAMETRS2, PARAMETRS3, PARAMETRS4,
                                 PARAMETRS5, PARAMETRS6, PARAMETRS7, PARAMETRS8])
def test_get_form_positive(client, url):
    """
    REST Api: Positive Test Get Form
    """
    response = client.post(f'/get_form/{url}')
    assert response.status_code == 200, 'Status code 200 - OK!'
    assert response.text == RES
    print(response.status, response.text, sep="\n")


@pytest.mark.parametrize("url, res", [(PARAMETRS9, RESPONSE1),
                                      (PARAMETRS10, RESPONSE2),
                                      (PARAMETRS11, RESPONSE3),
                                      (PARAMETRS12, RESPONSE4)])
def test_get_form_negative(client, url, res):
    """
    REST Api: Negative Test Get Form
    """
    response = client.post(f'/get_form/{url}')
    assert response.status_code == 200, 'Status code 200 - OK!'
    assert response.json == res
    print(response.status, response.text, sep="\n")
