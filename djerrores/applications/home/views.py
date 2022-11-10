from django.shortcuts import render
from django.http import  HttpResponseServerError
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView
)

class HomeView(TemplateView):
    template_name = "home/index.html"


class VistaEmjemplo(TemplateView):
    template_name = "home/ejemplo.html"
    
    
    def get_context_data(self, **kwargs):
        context = super(VistaEmjemplo, self).get_context_data(**kwargs)
        a = 'prueba'
        print(a/10)
        return context


class Error404View(TemplateView):
    template_name = "home/error_404.html"


class Error505View(TemplateView):
    template_name = "home/error_500.html"

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view


