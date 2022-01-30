from django.forms import forms
from board.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'contents')