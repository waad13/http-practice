import pytest
from http_requests import *


def test_1_perform_get_request():
    response = perform_get_request()

    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.request.url == 'https://httpbin.org/get'
    assert 'args' in response.json()
    assert response.json()['args'] == {}
    assert 'headers' in response.json()
    assert 'origin' in response.json()
    assert 'url' in response.json()


def test_2_perform_get_request_with_params():
    response = perform_get_request_with_params()

    assert response.status_code == 200
    assert response.request.method == 'GET'
    assert response.request.url.startswith('https://httpbin.org/get?')
    assert 'args' in response.json()
    assert response.json()['args'] != {}
    assert 'headers' in response.json()
    assert 'origin' in response.json()
    assert 'url' in response.json()


def test_3_perform_post_request():
    response = perform_post_request()

    expected = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }

    assert response.status_code == 200
    assert response.request.method == 'POST'
    assert response.request.url == 'https://httpbin.org/post'
    assert response.json()['json'] == expected


def test_4_perform_put_request():
    response = perform_put_request()

    expected = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }

    assert response.status_code == 200
    assert response.request.method == 'PUT'
    assert response.request.url == 'https://httpbin.org/put'
    assert response.json()['json'] == expected


def test_5_perform_patch_request():
    response = perform_patch_request()

    expected = {
        'first_name': 'Guido'
    }

    assert response.status_code == 200
    assert response.request.method == 'PATCH'
    assert response.request.url == 'https://httpbin.org/patch'
    assert response.json()['json'] == expected


def test_6_perform_delete_request():
    response = perform_delete_request()

    assert response.status_code == 200
    assert response.request.method == 'DELETE'
    assert response.request.url == 'https://httpbin.org/delete'


def test_7_perform_redirect_request():
    location_header = perform_redirect_request()

    assert location_header == '/get'
