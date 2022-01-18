from catalogo.views import HomeView
#from hostal.views import ParentCreateView


from django.urls import include, path



urlpatterns = [
    path('',HomeView, name = 'home'),
  ]