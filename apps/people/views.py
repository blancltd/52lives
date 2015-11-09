# -*- coding: utf-8 -*-

from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from addresses.forms import AddressForm
from addresses.models import Address

from .models import Person
from .forms import NominateForm, NominatorFormSet


class NomineeCreateView(CreateView):
    form_class = NominateForm
    template_name = 'peoples/nominate_form.html'
    model = Person

    def get_all_forms(self):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        nominee_form = NominatorFormSet()
        nominee_form.forms[0].initial = {
            'first_name': 'Cat',
            'last_name': 'Mouse',
            'email': 'ziogas@gmail.com',
            'phone': '01214131231',
            'relation': 'TESTING relation',
            'why_help': 'TEsting why help',
            'what_need': 'TEsting what need',
        }
        address_form = AddressForm()
        nominate_form_data = {
            'first_name': 'Kazys',
            'last_name': 'Test',
            'email': 'lol@gmail.com',
            'home_phone': '012141231',
            'hear_about_us': 'cat',
        }
        address_form_data = {
            'line_1': '91 Anglesey street',
            'city': 'Birmingham',
            'country': 'West Midlands',
            'postcode': 'b19 1ax',
            'country': '1',
        }
        address_form.initial = address_form_data
        form.initial = nominate_form_data
        context = {
            'form': form,
            'nominee_form': nominee_form,
            'address_form': address_form,
        }
        return context

    def get(self, request, *args, **kwargs):
        self.object = None
        forms = self.get_all_forms()
        return self.render_to_response(
            self.get_context_data(**forms)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()

        form = self.get_form(form_class)
        nominee_form = NominatorFormSet(request.POST)
        address_form = AddressForm(request.POST)
        if (form.is_valid() and nominee_form.is_valid() and address_form.is_valid()):
            return self.form_valid(form, nominee_form, address_form)
        nominee_form.is_valid()
        return self.form_invalid(form, nominee_form, address_form)

    def form_valid(self, form, nominee_form, address_form):
        self.object = form.save()
        nominee_form.instance = self.object
        nominees = nominee_form.save()
        address = address_form.save(commit=False)
        address = Address.objects.create_address(address, nominees[0], self.request.user)
        return HttpResponseRedirect('/nominate/thanks/')

    def form_invalid(self, form, nominee_form, address_form):
        return self.render_to_response(
            self.get_context_data(
                form=form, nominee_form=nominee_form, address_form=address_form, is_invalid=True
            )
        )

    def get_context_data(self, **kwargs):
        context = super(NomineeCreateView, self).get_context_data(**kwargs)
        return context
