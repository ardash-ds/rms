from rest_framework.exceptions import APIException


class IncorrectFileFormatException(APIException):
    """An exception class to represent HTTP 400 errors for incorrect file formats.

    Attributes:
    - status_code (int): The HTTP status code for this error (400).
    - default_detail (str): Incorrect file format
    - default_code (str): bad_request

    Usage:
    When a file has an incorrect format, an instance of IncorrectFileFormat class is raised
    along with a message 'Incorrect file format'.
    """
    
    status_code = 400
    default_detail = "Incorrect file format"
    default_code = "bad_request"
    