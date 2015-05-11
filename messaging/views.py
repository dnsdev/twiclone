from django.shortcuts import render
from django.views import generic
from .models import *

class IndexView(generic.ListView):
    model = Nachricht
    template_name = 'messaging/index.html'
    paginate_by = 10
    page_kwarg = 'p'

    def get_queryset(self):
        return Nachricht.objects.all()