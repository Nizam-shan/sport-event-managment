from new_admin.models import Tournaments
from django.forms import ModelForm

class TournamentsForm(ModelForm):
    class Meta:
        model = Tournaments
        fields = "__all__"