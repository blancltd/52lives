# -*- coding: utf-8 -*-

from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import messages

from .forms import AddressForm
from .models import Address


class AddressInline(GenericTabularInline):
    template = 'admin/addresses/address/edit_inlines/addresses.html'
    dialog_data = {
        'form': AddressForm(),
        'title': 'Add address',
        'dialog_class': 'add-address-dialog',
        'form_class': 'add-address-form',
    }
    model = Address
    extra = 0
    min_num = 0
    can_delete = True
    list_per_page = 2

    fieldsets = (
        (
            'Notes', {
                'classes': ('collapse',),
                'fields': (
                    'line_1', 'line_2', 'line_3', 'city', 'county', 'postcode', 'country',
                    'created_by', 'created_at', 'updated_at',
                )
            }
        ),
    )
    readonly_fields = (
        'line_1', 'line_2', 'line_3', 'city', 'county', 'postcode', 'country',
        'created_by', 'created_at', 'updated_at',
    )

    class Media:
        js = ('js/admin/addresses/addresses.js',)

    @staticmethod
    def create_address(request, obj):
        """ Add address. """
        context = {}
        add_address_form = AddressForm(request.POST)
        if add_address_form.is_valid():
            address = add_address_form.save(commit=False)
            address.content_object = obj
            address.created_by = request.user
            address.save()
            messages.success(request, 'The address "{}" was added successfully.'.format(
                address.line_1
            ))
            context.update({'success': True})
        else:
            context.update(add_address_form.errors)
        return context

