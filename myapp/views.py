from datetime import date
from django.shortcuts import render
from django.views import generic
from accounts.models import Application
import datetime


def index(request):
    return render(
        request,
        'app/about.html'
    )


class main(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'app/main.html'

    def get_queryset(self):
        return Application.objects.filter(status='ready')
        # str(datetime.datetime.today().day())
