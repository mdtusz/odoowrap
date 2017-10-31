from .base import BaseModel


class Lead(BaseModel):

    model_name = 'crm.lead'

    def __init__(self, odoo):
        super(Lead, self).__init__(odoo)

    def get(self):
        return self.call('search_read')

    def create(self, first_name, last_name, email, phone, company, note,
               team_id, medium):
        lead_object = {
            'name': '{} {}'.format(first_name, last_name),
            'contact_name': '{} {}'.format(first_name, last_name),
            'team_id': team_id,
            'phone': phone,
            'description': note
        }

        self.call('create', [lead_object])
