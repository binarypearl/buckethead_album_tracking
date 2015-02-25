from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

from django.views import generic

from django.utils import timezone

from batapp.models import Album

class IndexView (generic.ListView):
  template_name = 'batapp/index.html'
  context_object_name = 'latest_album_list'
  
  def get_queryset(self):
    'return all records'
    return Album.objects.order_by('pike_number')
  
class DetailView(generic.DetailView):
  # I don'k know why, but at a minimum you need this model=some_class
  # Otherwise it syntax error's all over the place.
  # What this allows us to do though, is to use {{ object.database_column_name }} directly in the detail.html
  # Strange, and yes it really uses 'object' . something.
  model = Album
  
  template_name = 'batapp/detail.html'
  

#def index(request):
#  latest_album_list = Album.objects.order_by('pike_number')
#  #template = loader.get_template ('batapp/index.html')
#  context = {'latest_album_list': latest_album_list}
#  
#  return render (request, 'batapp/index.html', context)
  
#def detail(request, batapp_id):
#  return HttpResponse("This page will list the details of the album: %s." % batapp_id)
		      
