from plone import api

from collective.contact.core.browser.contactable import BaseView
from collective.contact.core.browser.utils import get_ttw_fields,\
    date_to_DateTime
from collective.contact.core.interfaces import IContactable
from collective.contact.core.behaviors import IBirthday


class Contact(BaseView):

    start_date = ''
    end_date = ''
    birthday = ''
    gender = ''
    position = None
    organizations = []

    def update(self):
        super(Contact, self).update()
        held_position = self.context

        self.portal_url = api.portal.get().absolute_url()

        start_date = held_position.start_date
        if start_date is not None:
            start_date = date_to_DateTime(start_date)
            self.start_date = self.context.toLocalizedTime(start_date)

        end_date = held_position.end_date
        if end_date is not None:
            end_date = date_to_DateTime(end_date)
            self.end_date = self.context.toLocalizedTime(end_date)

        person = held_position.get_person()
        self.person = person
        self.fullname = person.Title()
        self.title = held_position.Title()

        if IBirthday.providedBy(person):
            birthday = person.birthday
            if birthday is not None:
                birthday = date_to_DateTime(birthday)
                self.birthday = self.context.toLocalizedTime(birthday)
        else:
            self.birthday = None

        self.gender = person.gender or ''

        self.position = held_position.get_position()

        organization = held_position.get_organization()
        self.organizations = organization and organization.get_organizations_chain() or []

        contactable = IContactable(held_position)
        contact_details = contactable.get_contact_details()
        self.email = contact_details['email']
        self.phone = contact_details['phone']
        self.cell_phone = contact_details['cell_phone']
        self.fax = contact_details['fax']
        self.im_handle = contact_details['im_handle']
        self.website = contact_details['website']
        self.address = contact_details['address']

        # also show fields that were added TTW
        self.ttw_fields = get_ttw_fields(held_position)
