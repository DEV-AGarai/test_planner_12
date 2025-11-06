from django.http import HttpResponse
from django.template import loader
from .models import TestSchedule


# Create your views here.
def table(request):
    mytests= TestSchedule.objects.all().order_by('date').values()
    template = loader.get_template('table.html')
    context = {
        'mytests': mytests
    }
    return HttpResponse(template.render(context, request))
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def syllabus(request,id):
    mytest= TestSchedule.objects.get(id=id)
    template = loader.get_template('syllabus.html')
    context = {
        'mytest': mytest
    }
    return HttpResponse(template.render(context, request))