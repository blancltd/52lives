# -*- coding: utf-8 -*-

from django.views.generic.list import ListView

from .models import Live


class LivesListView(ListView):
    queryset = Live.objects.active()
    model = Live
    paginate_by = 52

