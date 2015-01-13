# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations


presentations = [
    {
        "title": "Django 1.7 and Django-CMS 3.0",
        "slug": "django-1.7-and-django-cms-3.0",
        "description": "",
        "state": 0,
    }
]

states = [
    {
        "pk": 1,
        "path": "0001",
        "depth": 1,
        "name": "pre",
        "is_default_state": True,
        "order": 1,
        "children": [
            {
                "pk": 4,
                "path": "00010001",
                "depth": 2,
                "name": "voting",
                "is_default_state": False,
                "order": 11,
                "children": [],
            },
        ],
    },
    {
        "pk": 2,
        "path": "0002",
        "depth": 1,
        "name": "live",
        "is_default_state": False,
        "order": 2,
        "children": [],
    },
    {
        "pk": 3,
        "path": "0003",
        "depth": 1,
        "name": "post",
        "is_default_state": False,
        "order": 3,
        "children": [],
    },
]

slides = [
    {
        "presentation": 0,
        "path": "0001",
        "depth": 1,
        "title": "Django 1.7 and Django-CMS 3.0",
        "slug": "django-1.7-and-django-cms-3.0",
        "votable": False,
        "sms_value": None,
        "color": "",
        "states": [1, 2, 3, ],
        "children": [
            {
                "presentation": 0,
                "path": "00010001",
                "depth": 2,
                "title": "Hello",
                "slug": "hello",
                "votable": False,
                "sms_value": None,
                "color": "0f3e62",
                "states": [2, ],
                "children": [
                    {
                        "presentation": 0,
                        "path": "000100010001",
                        "depth": 3,
                        "title": "Voting",
                        "slug": "voting",
                        "votable": False,
                        "sms_value": None,
                        "color": "",
                        "states": [1, 2, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100010002",
                        "depth": 3,
                        "title": "Voting (Final)",
                        "slug": "voting-final",
                        "votable": False,
                        "sms_value": None,
                        "color": "",
                        "states": [3, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100010003",
                        "depth": 3,
                        "title": "Introduction",
                        "slug": "introduction",
                        "votable": False,
                        "sms_value": None,
                        "color": "",
                        "states": [2, 3, ],
                        "children": [],
                    },
                ],
            },
            {
                "presentation": 0,
                "path": "00010002",
                "depth": 2,
                "title": "Django 1.7",
                "slug": "django-1.7",
                "votable": False,
                "sms_value": None,
                "color": "0C4B33",
                "states": [2, 3, 4, ],
                "children": [
                    {
                        "presentation": 0,
                        "path": "000100020001",
                        "depth": 3,
                        "title": "New and Deprecated",
                        "slug": "new-and-deprecated",
                        "votable": False,
                        "sms_value": None,
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100020002",
                        "depth": 3,
                        "title": "Model Layer",
                        "slug": "model-layer",
                        "votable": True,
                        "sms_value": "model",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [
                            {
                                "presentation": 0,
                                "path": "0001000200020001",
                                "depth": 4,
                                "title": "What's in",
                                "slug": "whats-in",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                            {
                                "presentation": 0,
                                "path": "0001000200020002",
                                "depth": 4,
                                "title": "What's out",
                                "slug": "whats-out",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                            {
                                "presentation": 0,
                                "path": "0001000200020003",
                                "depth": 4,
                                "title": "Schema Migration",
                                "slug": "schema-migration",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                            {
                                "presentation": 0,
                                "path": "0001000200020004",
                                "depth": 4,
                                "title": "Shadowing model fields",
                                "slug": "shadowing-model-fields",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                        ],
                    },
                    {
                        "presentation": 0,
                        "path": "000100020003",
                        "depth": 3,
                        "title": "App Loading Refactor",
                        "slug": "app-loading-refactor",
                        "votable": True,
                        "sms_value": "loading",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100020004",
                        "depth": 3,
                        "title": "System Checks Framework",
                        "slug": "system-checks-framework",
                        "votable": True,
                        "sms_value": "checks",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100020005",
                        "depth": 3,
                        "title": "View Layer",
                        "slug": "view-layer",
                        "votable": True,
                        "sms_value": "view",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [
                            {
                                "presentation": 0,
                                "path": "0001000200050001",
                                "depth": 4,
                                "title": "What's in",
                                "slug": "whats-in",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                            {
                                "presentation": 0,
                                "path": "0001000200050002",
                                "depth": 4,
                                "title": "Forms",
                                "slug": "forms",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                            {
                                "presentation": 0,
                                "path": "0001000200050003",
                                "depth": 4,
                                "title": "Templates",
                                "slug": "templates",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                        ],
                    },
                    {
                        "presentation": 0,
                        "path": "000100020006",
                        "depth": 3,
                        "title": "The Admin",
                        "slug": "admin",
                        "votable": True,
                        "sms_value": "admin",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [
                            {
                                "presentation": 0,
                                "path": "0001000200060001",
                                "depth": 4,
                                "title": "Customization",
                                "slug": "customization",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                            {
                                "presentation": 0,
                                "path": "0001000200060002",
                                "depth": 4,
                                "title": "Change list improvements",
                                "slug": "change-list-improvements",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                            {
                                "presentation": 0,
                                "path": "0001000200060003",
                                "depth": 4,
                                "title": "Shortcuts",
                                "slug": "shortcuts",
                                "votable": False,
                                "sms_value": None,
                                "color": "",
                                "states": [2, 3, 4, ],
                                "children": [],
                            },
                        ],
                    },
                    {
                        "presentation": 0,
                        "path": "000100020007",
                        "depth": 3,
                        "title": "Django 1.8",
                        "slug": "django-1.8",
                        "votable": True,
                        "sms_value": "checks",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                ]
            },
            {
                "presentation": 0,
                "path": "00010003",
                "depth": 2,
                "title": "Django CMS",
                "slug": "django-cms",
                "votable": False,
                "sms_value": None,
                "color": "0f3e62",
                "states": [2, 3, 4, ],
                "children": [
                    {
                        "presentation": 0,
                        "path": "000100030001",
                        "depth": 3,
                        "title": "Features",
                        "slug": "features",
                        "votable": True,
                        "sms_value": "features",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100030002",
                        "depth": 3,
                        "title": "Installation and Configuration",
                        "slug": "installation-and-configuration",
                        "votable": True,
                        "sms_value": "install",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100030003",
                        "depth": 3,
                        "title": "Pages and Templates",
                        "slug": "pages-and-templates",
                        "votable": True,
                        "sms_value": "pages",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100030004",
                        "depth": 3,
                        "title": "Plugins",
                        "slug": "plugins",
                        "votable": True,
                        "sms_value": "plugins",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100030005",
                        "depth": 3,
                        "title": "Permissions",
                        "slug": "permissions",
                        "votable": True,
                        "sms_value": "permissions",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                    {
                        "presentation": 0,
                        "path": "000100030006",
                        "depth": 3,
                        "title": "Django CMS 3.1",
                        "slug": "django-cms-3.1",
                        "votable": True,
                        "sms_value": "checks",
                        "color": "",
                        "states": [2, 3, 4, ],
                        "children": [],
                    },
                ]
            },
        ],
    }
]


def _create_state(State, data):
    states = []

    state = State()
    state.pk = data['pk']
    state.depth = data['depth']
    state.path = data['path']
    state.numchild = 0
    state.name = data['name']
    state.is_default_state = data['is_default_state']
    state.order = data['order']
    states.append(state)

    for child in data['children']:
        states.extend(_create_state(State, child))

    return states


def _create_slide(Slide, data, presentations):
    slides = []
    slide = Slide()
    slide.presentation = presentations[data['presentation']]
    slide.depth = data['depth']
    slide.path = data['path']
    slide.numchild = len(data['children'])
    slide.title = data['title']
    slide.votable = data['votable']
    slide.sms_value = data['sms_value']
    slide.color = data['color'] or None
    slides.append(slide)

    for child in data['children']:
        slides.extend(_create_slide(Slide, child, presentations))

    return slides


def create_states(State):
    orm_states = []

    for root_state in states:
        orm_states.extend(_create_state(State, root_state))

    return orm_states


def create_slides(Slide, presentations):
    orm_slides = []

    for root_slide in slides:
        orm_slides.extend(_create_slide(Slide, root_slide, presentations))

    return orm_slides


def create_presentations(Presentation, State, db_alias):
    orm_presentations = []
    states = State.objects.using(db_alias).all().order_by('path')
    for data in presentations:
        presentation = Presentation()
        presentation.title = data['title']
        presentation.slug = data['slug']
        presentation.description = data['description']
        presentation.state = states[data['state']]
        presentation.save(using=db_alias)
        orm_presentations.append(presentation)
    return orm_presentations


def _link(Slide, db_alias, data):
    slide = Slide.objects.using(db_alias).get(path=data['path'])
    for state_id in data['states']:
        slide.visible_states.add(state_id)

    slide.save(using=db_alias)

    for child in data['children']:
        _link(Slide, db_alias, child)


def link_all(Slide, db_alias):
    for root_slide in slides:
        _link(Slide, db_alias, root_slide)


def add_default_data(apps, schema_editor):
    Presentation = apps.get_model("slides", "Presentation")
    State = apps.get_model("slides", "State")
    Slide = apps.get_model("slides", "Slide")
    db_alias = schema_editor.connection.alias
    State.objects.using(db_alias).bulk_create(create_states(State))
    presentations = create_presentations(Presentation, State, db_alias)
    Slide.objects.using(db_alias).bulk_create(create_slides(Slide, presentations))
    link_all(Slide, db_alias)


def remove_default_data(apps, schema_editor):
    Presentation = apps.get_model("slides", "Presentation")
    State = apps.get_model("slides", "State")
    Slide = apps.get_model("slides", "Slide")
    db_alias = schema_editor.connection.alias
    Slide.objects.using(db_alias).all().delete()
    Presentation.objects.using(db_alias).delete()
    State.objects.using(db_alias).all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_default_data,
            reverse_code=remove_default_data,
        ),
    ]
