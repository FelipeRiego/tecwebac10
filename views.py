# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
#from django.core.urlresolvers import reverse_lazy
from ac9.models import Inscricao
from ac9.forms import InscricaoForm

def home(request):
        return render(request,'index.html')

class Criar(CreateView):
        template_name = 'cadastro.html'
        model = Inscricao
        fields = "__all__" 
        #success_url = reverse_lazy('lista')

class Lista(ListView):
        template_name = 'lista.html'
        model = Inscricao
        context_object = 'nome'
        fields = "__all__" 