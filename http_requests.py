import requests


def perform_get_request():
    """Perform GET request to given URL and return the response"""
    url = 'https://httpbin.org/get'
    pass


def perform_get_request_with_params():
    """Perform GET request to given URL sending any parameter and return the response"""
    url = 'https://httpbin.org/get'
    pass


def perform_post_request():
    """Perform POST request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/post'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    pass


def perform_put_request():
    """Perform PUT request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/put'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    pass


def perform_patch_request():
    """Perform PATCH request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/patch'
    data = {
        'first_name': 'Guido'
    }
    pass


def perform_delete_request():
    """Perform DELETE request to given URL and return the response"""
    url = 'https://httpbin.org/delete'
    pass
