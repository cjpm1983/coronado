from django.http.response import HttpResponseRedirect
from django.shortcuts import render

#from django.contrib.auth.decorators import login_required
from catalogo.models import Catalogo_Coronado as Catalogo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import re
from unicodedata import normalize
from django.db.models import Q
#from unidecode import unidecode

# Create your views here.

#@login_required(login_url="")
def HomeView(request):
    
    catalogos_list = []
    if request.method == 'POST':

        filter = request.POST['filter']
        valor = request.POST['valor']
        
        #quitar acentos
        s = valor
        s = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", s), 0, re.I )
        #s = unidecode(s)
        # -> NFC
        s = normalize( 'NFC', s)

        #print( s )

        if (filter=="autor"):
            #return HttpResponseRedirect('/thanks/'+str(valor))
            #catalogos_list = Catalogo.objects.filter(Q(autor__icontains=valor)|Q(autor__icontains=s)).all()#.order_by('id')
            catalogos_list = Catalogo.objects.filter(autor__icontains=valor).all()
            #catalogos_list = Catalogo.objects.all()
        if (filter=="titulo"):
            #return HttpResponseRedirect('/thanks/'+str(valor))
            catalogos_list = Catalogo.objects.filter(titulo__icontains=valor).all()
            #catalogos_list = Catalogo.objects.filter(Q(titulo__icontains=valor)|Q(titulo__icontains=s)).all()#.order_by('id')
            #catalogos_list = Catalogo.objects.all()

    else:
        catalogos_list = Catalogo.objects.all()#.filter(Reservado_Por=request.user).order_by('-id')
    

    page = request.GET.get('page', 1)

    paginator = Paginator(catalogos_list, 50)
    try:
        catalogos = paginator.page(page)
    except PageNotAnInteger:
        catalogos = paginator.page(1)
    except EmptyPage:
        catalogos = paginator.page(paginator.num_pages)

    
    return render(request,'catalogo/catalogos.html',{'catalogos':catalogos})



#filetr
import django_filters
class CatalogoFilter(django_filters.FilterSet):
    autor = django_filters.CharFilter(name="autor", lookup_type="contains")
    titulo = django_filters.CharFilter(name="titulo", lookup_type="contains")

    class Meta:
        model = Catalogo
        fields = ['autor', 'titulo']

from catalogo.serializers import CatalogoSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class CatalogoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Catalogo.objects.all()
    serializer_class = CatalogoSerializer
    #permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'head']
    
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['autor', 'titulo']
    
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['autor', 'titulo']

    #filter_class = CatalogoFilter

    def get_queryset(self):
        autor_name = self.request.query_params.get('autor', "")
        titulo_name= self.request.query_params.get('titulo', "")

        if 'autor' not in self.request.query_params and 'titulo' not in self.request.query_params:    
            queryset = Catalogo.objects.all()
        elif (autor_name is not None and titulo_name is not None):
            queryset = Catalogo.objects.filter(autor__icontains=autor_name, titulo__icontains=titulo_name).all()
            #catalogos_list = Catalogo.objects.all()
        elif (autor_name is not None):
            queryset = Catalogo.objects.filter(autor__icontains=autor_name).all()
            #catalogos_list = Catalogo.objects.all()
        elif (titulo_name is not None):
            #return HttpResponseRedirect('/thanks/'+str(valor))
            queryset = Catalogo.objects.filter(titulo__icontains=titulo_name).all()  
        else:
            queryset = Catalogo.objects.all()

        return queryset
