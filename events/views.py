from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .models import EventRun


def index(request):
    return render(request, 'events/index.html')


def event_listing(request):
    events = Event.objects.all()
    return render(request, 'events/event_listing.html', {'events':events})


def event_detail(request, pk):

    event = Event.objects.get(pk=pk)
    event_runs = EventRun.objects.filter(event=pk)

    if event:
        return render(request, 'events/event_detail.html', {'event':event, 'event_runs':event_runs})
    else:
        return HttpResponse('No such event in offering for now')
