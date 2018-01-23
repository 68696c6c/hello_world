# Create your views here.
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from hellow_world_app.models import Rock


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
            'banner': 'Rocks/List.html',
            'img_path': '',
            'rocks': Rock.objects.all().order_by('?'),
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
            'banner': 'Rocks/Detail.html',
            'img_path': '',
            'rock': Rock.objects.get(id=kwargs['id']),
            'data': {
                'url_path': "'rocks/detail'",
                'view_path': 'templates/rocks/detail.html',
                'request': request,
                'args': args,
                'kwargs': kwargs,
            },
        }
        return self.render_to_response(context)
