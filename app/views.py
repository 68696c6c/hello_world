# Create your views here.
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect

from app.models import Rock


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'banner': 'Index.html',
            'img_path': 'images/meaganfoxy.jpg',
            'data': {
                'url_path': "'rocks/list'",
                'view_path': 'templates/rocks/list.html',
                'request': request,
                'args': args,
                'kwargs': kwargs,
            },
        }
        return self.render_to_response(context)


class RockList(ListView):
    model = Rock
    template_name = 'rocks/list.html'

    def get_context_data(self):
        context = {
            'rocks': Rock.objects.all().order_by('?'),
            'banner': 'Rocks/List.html',
            'img_path': '',
            'data': {
                'url_path': "'rocks/list'",
                'view_path': 'templates/rocks/list.html',
            },
        }
        return context


class RockDetail(TemplateView):
    template_name = 'rocks/detail.html'

    def get(self, request, *args, **kwargs):
        context = {
            'rock': Rock.objects.get(id=kwargs['id']),
            'banner': 'Rocks/Detail.html',
            'img_path': '',
            'data': {
                'url_path': "'rocks/detail'",
                'view_path': 'templates/rocks/detail.html',
                'request': request,
                'args': args,
                'kwargs': kwargs,
            },
        }
        return self.render_to_response(context)


class CreateRock(TemplateView):
    template_name = 'rocks/create.html'

    def get(self, request, *args, **kwargs):

        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # When a server gets a POST request, it indicates that the request
            # intends to *create* a new thing.  Since a POST request is about
            # trying to create something, the request will always be accompanied
            # with additional data, called the request "body", about the thing
            # to be created. In our case, the data (or POST body) comes from our form.

            # create a form instance and populate it with data from the request:
            form = Rock(request.POST)

            # check whether it's valid:
            if form.is_valid():
                # save the rock

                # redirect to a new URL:
                return HttpResponseRedirect('/rocks/list/')

        # if a GET (or any other method) we'll create a blank form
        else:
            # A GET request is the standard type of request.  It indicates that
            # the client (the machine that sent the request) is trying to look
            # at, or *read* something.  The List and Detail views are using GET
            # requests.  If we get a GET request to this view, it means the client
            # just wants to see the form.
            form = Rock()

        context = {
            'rock': form,
            'banner': 'Rocks/Create.html',
            'img_path': '',
            'data': {
                'url_path': "'rocks/create'",
                'view_path': 'templates/rocks/detail.html',
                'request': request,
                'args': args,
                'kwargs': kwargs,
            },
        }
        return self.render_to_response(context)
