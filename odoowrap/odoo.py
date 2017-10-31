from xmlrpc import client

from . import models


class Odoo(object):
    '''
    The Odoo class provides easy manipulation and retrieval of odoo resources.
    '''

    def __init__(self, username=None, password=None, url=None, database=None):
        self._username = username
        self._password = password
        self._database = database
        self._common_proxy = client.ServerProxy(
            '{}/xmlrpc/2/common'.format(url))
        self._uid = self._common_proxy.authenticate(database, username,
                                                    password, {})
        self._model_proxy = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

        self.lead = models.Lead(self)

    def call(self, model, method, list_args=[[]], dict_args={}):
        return self._model_proxy.execute_kw(self._database, self._uid,
                                            self._password, model, method,
                                            list_args, dict_args)
