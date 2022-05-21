from rest_framework.exceptions import APIException


class UNAUTHORIZED_USER_EXCEPTION(APIException):
    status_code = 404
    default_detail = "Not Found"
    default_code = "Records unavailable"
