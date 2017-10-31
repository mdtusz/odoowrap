from ..exceptions import ClientException


class BaseModel(object):

    def __init__(self, odoo):
        '''
        Initialize a model instance.

        :param odoo:    An instance of :class:`.Odoo`.
        '''
        self._odoo = odoo

    def call(self, method, list_args=[[]], dict_args={}):
        if self.model_name is None:
            raise ClientException

        return self._odoo.call(self.model_name, method, list_args, dict_args)
