# HTTP Practice

Basic practice to learn HTTP concepts using `requests` python library, and [this website](https://httpbin.org/) that brings many endpoints for different usages.

You can find the solution to all this exercises inside the `solution` branch of this repository.

### 1. Perform a simple GET request

This exercise is done for you as an example. We just wrote a function that uses the `requests` python library to perform a GET request, and return the response that we get. As part of the response you'll be able to find things like which HTTP method was used, the [status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) that we get, the headers that were sent, etc.


### 2. Perform a GET request with parameters

In this case you'll need to add GET parameters as part of the URL. Those parameters are used when we need to send extra data while doing the request.


### 3. Perform a POST request

For this exercise you'll need to use another HTTP method which is called POST. This method is also used to send data as part of the request, but in this case the data doesn't goes inside the URL, but it goes as a separate payload that you'll need to build beforehand. As the data isn't in the URL anymore, it is harder to see it while it travels during the request.


### 4. Perform a PUT request

This HTTP method works the same way as the used before. You'll need to send the data as a separate payload while doing the request. PUT method is usually used when you want to perform a full update of any data model in your backend service. Anyways, that is out of the scope of this practice.


### 5. Perform a PATCH request

Similar to the method used before, but this one is usually used to perform a partial update of any data model.


### 6. Perform a DELETE request

Perform a requests using the DELETE HTTP method. This one is usually used when you want to remove any object saved in a database.


### 7. Inspect headers during a redirect request

In this case you'll have to perform a GET request to the given URL (which already handles the redirect). The status code that you'll get is going to be inside the 3XX group which means 'Redirection'.

Inspect the headers that came in the response and return the "Location" one. Make sure to use the `allow_redirects` parameter while performing the request, to work with the response that comes before the redirect is done.
