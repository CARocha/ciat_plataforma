from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Biblioteca
from django.db.models import Q

# Create your views here.

class IndexView(TemplateView):
    template_name = "biblioteca/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['resultados'] = Biblioteca.objects.all()

        return context

def buscador(request):
    if request.method == "GET":
        search_text = request.GET['q']
        print search_text
        if search_text is not None and search_text != u"":
            search_text = request.GET['q']
            resultados = Biblioteca.objects.filter(Q(titulo__icontains=search_text) |
                 Q(autor__icontains=search_text) |
                 Q(descripcion__icontains=search_text) |
                 Q(cita__icontains=search_text) |
                 Q(palabras_claves__icontains=search_text) |
                 Q(proyecto__nombre__icontains=search_text) |
                 Q(temas__nombre__icontains=search_text)
                 ).distinct()
        else:
            resultados = []

    return render(request, 'biblioteca/index.html', {'resultados':resultados})


def detalle_libro(request, id_libro=None, template="biblioteca/detail-biblioteca.html"):
    detalle = Biblioteca.objects.get(id=id_libro)

    return render(request, template, locals())
