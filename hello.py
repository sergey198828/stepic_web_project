def wsgi_application(environ, start_responce):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    body = environ['QUERY_STRING'].split("&")
    start_responce(status, headers)
    return body