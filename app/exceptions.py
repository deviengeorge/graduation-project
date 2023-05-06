from rest_framework.views import exception_handler
from http import HTTPStatus
from rest_framework.views import Response


def api_exception_handler(exc: Exception, context) -> Response:
    """Custom API exception handler."""

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        # Using the description's of the HTTPStatus class as error message.
        http_code_to_message = {v.value: v.description for v in HTTPStatus}

        error_payload = {
            "status_code": 0,
            "message": "",
            "errors": [],
        }
        status_code = response.status_code

        error_payload["status_code"] = status_code
        error_payload["message"] = http_code_to_message[status_code]

        print(response.data)

        if "detail" in response.data:
            if response.data["detail"].code == "permission_denied":
                error_payload["message"] = "Permission Denied"
            elif response.data["detail"].code == "not_authenticated":
                error_payload["message"] = "Not Authenticated"
        else:
            error_payload["errors"] = {
                key: value[0] for (key, value) in response.data.items()
            }
        response.data = error_payload
    return response
