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
