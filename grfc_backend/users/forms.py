from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import GrfcUser

class GrfcUserCreationForm(UserCreationForm):

    class Meta:
        model = GrfcUser
        fields = ('username', 'email', 'first_name', 'last_name', 'patronymic', 'fio', 'fio_r', 'fio_d', 'fio_t', )

class GrfcUserChangeForm(UserChangeForm):

    class Meta:
        model = GrfcUser
        fields = ('username', 'email', 'first_name', 'last_name', 'patronymic', 'fio', 'fio_r', 'fio_d', 'fio_t', )
