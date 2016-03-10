# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView

from .models import Company


class CompanyListView(ListView):
    model = Company
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        return context
