class OdooWrapException(Exception):

    def __init__(self, error_type, error_message):
        error = '{}: {}'.format(error_type, error_message)
        super(APIException, self).__init__(error)


class APIException(OdooWrapException):
    pass


class ClientException(OdooWrapException):
    pass
