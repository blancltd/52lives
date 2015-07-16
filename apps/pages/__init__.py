# -*- coding: utf-8 -*-

import blanc_pages

default_app_config = 'pages.apps.PagesConfig'


class DefaultLayout(blanc_pages.BlancPageLayout):
    template_name = 'blanc_pages/default.html'
    title = 'Default'
    columns = {
        'Intro': {
            'width': 960,
            'image_width': 960,
        },
        'Content': {
            'width': 960,
            'image_width': 960,
        },
    }


class HomeLayout(blanc_pages.BlancPageLayout):
    template_name = 'blanc_pages/homepage.html'
    title = 'Default'
    columns = {
        'Intro': {
            'width': 960,
            'image_width': 960,
        },
        'Content': {
            'width': 960,
            'image_width': 960,
        },
    }


blanc_pages.register_template(DefaultLayout)
blanc_pages.register_template(HomeLayout)
