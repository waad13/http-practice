# HTTP Practice

<p align="center">
  <a href="https://www.youtube.com/watch?v=N1BMyypbNaM">
    <img width="460" height="300" src="http://img.youtube.com/vi/N1BMyypbNaM/maxresdefault.jpg">
  </a>
</p>
<p align="center">
  <i>(Explanation of project video on YouTube)</i>
</p>

<!-- This video absolutely needs to be rerecorded with better audio -->

This project will give you practice in order to learn some basic HTTP concepts using the [`requests`](http://docs.python-requests.org/) python library, and [this website](https://httpbin.org/) that lets you experiment with endpoints for different usages.

You can find the solution to all these exercises inside the `solution` branch of this repository.

# Install Instructions
Fork this repo and create a new workspace as we do with all of our projects. Then follow the usual steps:

```bash
$ mkvirtualenv http-practice -p /usr/bin/python3
$ pip install -r requirements.txt
```

# Assignments:

### 1. Perform a simple GET request

```bash
$ py.test tests.py -k test_1
```

This exercise is already done to serve as an example. We wrote a function for you that uses the `requests` python library to perform a `GET` request, and returns the response that we receive. As part of the response you'll be able to find things like which HTTP method was used, the [status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) that we received, the headers that were sent, etc.


### 2. Perform a GET request with parameters

```bash
$ py.test tests.py -k test_2
```

In this case you'll need to add `GET` parameters (also called query params some times) as part of the URL. These parameters are used when we need to send extra data while doing a request. An example of a query params are the Google search terms. When you perform a simple google search, the browser sends the query params with your search query (`https://www.google.com/search?q=python+language`):

![image](https://user-images.githubusercontent.com/872296/38690816-6c950602-3e55-11e8-996b-1c78585f9b7f.png)

### 3. Perform a POST request

```bash
$ py.test tests.py -k test_3
```

For this exercise you'll need to use another HTTP method called `POST`. This method is also used to send data as part of the request, but in this case the data doesn't go in the URL, but is sent as a separate payload that you'll need to build beforehand. As the data isn't in the URL anymore, it is harder to inspect while it travels during the request.

### 4. Perform a PUT request

```bash
$ py.test tests.py -k test_4
```

This HTTP method works in a similar way as the one we just used. You'll need to send the data as a separate payload while doing the request. The `PUT` method is usually used when you want to perform a full update of any data model in your back-end service. For now, that's a little out of the scope of this practice.

### 5. Perform a PATCH request

```bash
$ py.test tests.py -k test_5
```

Similar to the previous method, but this one is usually used to perform a partial update of any data model.

### 6. Perform a DELETE request

```bash
$ py.test tests.py -k test_6
```

Perform a request using the `DELETE` HTTP method. This one is usually used when you want to remove an object saved in a database.

### 7. Inspect headers during a redirect request

```bash
$ py.test tests.py -k test_7
```

In this case you'll have to perform a `GET` request to the given URL (which already handles the redirect). The status code that you'll receive is going to be inside the 3XX group which means 'Redirection'.

Inspect the headers that came in the response and return the "Location" header. Make sure to use the `allow_redirects` parameter while performing the request, to be able to work with the response that comes before the redirect is finished.
