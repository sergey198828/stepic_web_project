def wsgi_application(environ, start_responce):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    body = [
        (p + "\n").encode("utf-8") for p in environ['QUERY_STRING'].split("&")
    ]
    start_responce(status, headers)
    return body
