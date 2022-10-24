# -*- coding: utf-8 -*-
{
    'name': "event_external_ticket",

    'summary': """
        This module makes it possible to link the event-registration button to an external site.
    """,

    'description': """
        This module makes it possible to link the event-registration button to an external site.
    """,

    'author': "Snakebyte Development",
    'website': "https://snakebyte-development.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '16.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['website_event'],

    # always loaded
    'data': [
        'views/event_event_views.xml',
        'views/event_templates_pages_registration.xml',
    ],
}
