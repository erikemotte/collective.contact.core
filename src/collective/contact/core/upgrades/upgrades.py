# -*- coding: utf-8 -*-

from zc.relation.interfaces import ICatalog
from z3c.relationfield.event import updateRelations
from z3c.relationfield.interfaces import IHasRelations
from zope.component import getUtility

from plone import api

from ecreall.helpers.upgrade.interfaces import IUpgradeTool
from collective.contact.widget.interfaces import IContactContent


def reindex_relations(context):
    """Clear the relation catalog to fix issues with interfaces that don't exist anymore.
    This actually fixes the from_interfaces_flattened and to_interfaces_flattened indexes.
    """
    rcatalog = getUtility(ICatalog)
    rcatalog.clear()
    catalog = api.portal.get_tool('portal_catalog')
    brains = catalog.searchResults(object_provides=IHasRelations.__identifier__)
    for brain in brains:
        obj = brain.getObject()
        updateRelations(obj, None)


def v2(context):
    tool = IUpgradeTool(context)
    tool.runProfile('collective.contact.core.upgrades:v2')
    catalog = api.portal.get_tool(name='portal_catalog')
    catalog.clearFindAndRebuild()
    reindex_relations(context)


def v3(context):
    catalog = api.portal.get_tool('portal_catalog')
    brains = catalog.unrestrictedSearchResults(object_provides=IContactContent.__identifier__)
    for brain in brains:
        obj = brain.getObject()
        obj.is_created = True
