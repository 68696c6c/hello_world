# Create your views here.
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from app.models import Rock


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'banner': 'Index.html',
            'img_path': 'images/meaganfoxy.jpg',
        }
        return self.render_to_response(context)


class RockList(ListView):
    model = Rock
    template_name = 'rocks/list.html'

    def get_context_data(self):
        context = {
            'rocks': Rock.objects.all().order_by('?'),
            'banner': 'Rocks/List.html',
        }
        return context


class RockDetail(TemplateView):
    template_name = 'rocks/detail.html'

    def get(self, request, *args, **kwargs):
        context = {
            'rock': Rock.objects.get(id=kwargs['id']),
            'banner': 'Rocks/Detail.html',
            'img_path': '',
        }
        return self.render_to_response(context)


class UpdateRock(UpdateView):
    template_name = 'rocks/update.html'
    model = Rock
    fields = ['name', 'description', 'slug']


class CreateRock(CreateView):
    template_name = 'rocks/create.html'
    model = Rock
    fields = ['name', 'description', 'slug']
