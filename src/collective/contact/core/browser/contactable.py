import os.path

from zope.globalrequest import getRequest
from five import grok
from Acquisition import aq_base

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.dexterity.browser.view import DefaultView
from plone.dexterity.utils import getAdditionalSchemata

from collective.contact.core.browser import TEMPLATES_DIR
from collective.contact.core.browser.address import get_address
from collective.contact.core.behaviors import IContactDetails
from collective.contact.core.interfaces import IContactable
from collective.contact.widget.interfaces import IContactContent


class Contactable(grok.Adapter):
    """Base adapter class for objects that have the IContactDetails behavior fields"""
    grok.provides(IContactable)
    grok.context(IContactContent)
    grok.baseclass()

    @property
    def person(self):
        return None

    @property
    def position(self):
        return None

    @property
    def organizations(self):
        return []

    def _get_contactables(self):
        """
        Build a list of objects which have the IContactDetails behavior
        for each contact information (email, phone, ...)
        we use the one of the first object in this list which have this information
        """
        contactables = []
        related_items = [self.context, self.person, self.position] + list(reversed(self.organizations))
        for related_item in related_items:
            if related_item is not None \
              and IContactDetails.providedBy(related_item) \
              and related_item not in contactables:
                contactables.append(related_item)

        return contactables

    def _get_address(self, contactables):
        for obj in contactables:
            obj = aq_base(obj)
            if obj.use_parent_address is True:
                continue
            else:
                address = get_address(obj)
                if address:
                    return address

        return {}

    def get_contact_details(self):
        contact_details = {}
        contact_details_fields = ['email', 'phone', 'cell_phone', 'fax', 'website', 'im_handle']
        contactables = self._get_contactables()
        for field in contact_details_fields:
            # search the object that carries the field
            for obj in contactables:
                obj = aq_base(obj)
                value = getattr(obj, field, '') or ''
                if value:
                    contact_details[field] = value
                    break
            else:
                contact_details[field] = ''

        contact_details['address'] = self._get_address(contactables)
        return contact_details

    def get_parent_address(self):
        contactables = self._get_contactables()
        url = self.context.REQUEST.URL
        # we don't want self.context address if the object is already created
        if '/++add++' not in url and '/@@add' not in url:
            contactables.remove(self.context)

        address = self._get_address(contactables)
        if not address:
            # Very important to return unicode here, RichTextWidget needs it.
            return u''

        template_path = os.path.join(TEMPLATES_DIR, 'address.pt')
        template = ViewPageTemplateFile(template_path)
        self.request = getRequest()
        return template(self, address)


class BaseView(DefaultView):

    @property
    def additionalSchemata(self):
        # we don't want IContactDetails in behaviors
        additional_schemata = list(getAdditionalSchemata(context=self.context))
        if IContactDetails in additional_schemata:
            additional_schemata.remove(IContactDetails)
        return additional_schemata

    def render_address(self):
        template_path = os.path.join(TEMPLATES_DIR, 'address.pt')
        template = ViewPageTemplateFile(template_path)
        return template(self, self.address)
