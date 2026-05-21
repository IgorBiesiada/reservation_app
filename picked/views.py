from django.shortcuts import render
from picked.models import Favorite
from rooms.models import BaseResource
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def add_to_favorite(request, pk):
    if request.user.is_authenticated:
        valid_data = Favorite.objects.filter(resource=pk)
        if valid_data:
            Favorite.objects.delete(user=request.user, resource=pk)
            return redirect('rooms:resource_list')
        
        else:
            Favorite.objects.create(user=request.user, resource=pk)
            return redirect('rooms:resource_list')
    
    else:
        favorite_resource = request.session.get('favorite', [])
        
        if pk in favorite_resource:
           favorite_resource.remove(pk)
        
        else:
            favorite_resource.append(pk)

        request.session['favorite'] = favorite_resource
        request.session.modyfied = True

def favorite_list(request):
    template_name = 'picked/favorite_list.html'
    
    if request.user.is_authenticated:
        favorite_ids = Favorite.objects.filter(user=request.user)
        resource = BaseResource.objects.filter(id__in=favorite_ids)
        
        
        context = {
            'resource': resource 
        }

        return render(request, template_name, context)
    
    else:
        favorite_ids = request.session.get('favorite', [])
        resource = BaseResource.objects.filter(id__in=favorite_ids)

        context = {
            'resource': resource
        }

        return render(request, template_name, context)  