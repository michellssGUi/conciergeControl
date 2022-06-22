from multiprocessing import context
from django.views.generic import TemplateView
from .models import Apartamento, Leitura 

class IndexView(TemplateView):
    template_name = 'index.html'

    #def get_context_data(self, **kwargs):
    #    context = super(IndexView, self).get_context_data(**kwargs)
    #    context['certificado'] = Certificado.objects.order_by('?').all()
    #    return context
    
class LeituraView(TemplateView):
    template_name = 'leitura.html'
    
    def get_context_data(self, **kwargs):
        context = super(LeituraView, self).get_context_data(**kwargs)
        context['leitura'] = Leitura.objects.order_by('data').all().reverse().order_by('apartamento').reverse()
        return context