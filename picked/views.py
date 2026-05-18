from django.shortcuts import render
from picked.models import Favorite
from rooms.models import BaseResource
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def add_to_favorite(request, resource_pk):
    if request.user.is_authenticated:
        valid_data = Favorite.objects.filter(resource=resource_pk)
        if valid_data:
            Favorite.objects.delete(user=request.user, resource=resource_pk)
            return redirect('rooms:resource_list')
        
        else:
            Favorite.objects.create(user=request.user, resource=resource_pk)
            return redirect('rooms:resource_list')
    
    else:
        favorite_resource = request.session.get('favorite', [])
        
        if resource_pk in favorite_resource:
           favorite_resource.remove(resource_pk)
        
        else:
            favorite_resource.append(resource_pk)

        request.session['favorite'] = favorite_resource
        request.session.modyfied = True

def favorite_list(request):
    template_name = 'picked/favorite_list.html'
    
    if request.user.is_is_authenticated:
        favorite_ids = Favorite.objects.all(user=request.user)
        
        
        
        context = {
            'favorite': data
        }

        return render(request, template_name, context)
    
    else:
        favorite_ids = request.session.get('favorite', [])
        