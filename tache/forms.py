from django import forms
from .models import *
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


# class AddBoard(forms.ModelForm):
#     class Meta:
#         model = ListBoard
#         fields = ('board_name',)
#
class AddBoard(BSModalForm):
    class Meta:
        model = ListBoard
        fields = ('board_name',)


class AddList(BSModalForm):
    class Meta:
        model = ListList
        fields = ('list_board', 'list_name', 'list_description',)


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']