from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from . forms import SportForm, OfficeForm, EventForm, BeautyForm, LivingForm
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class AddSportsResourceView(LoginRequiredMixin, CreateView):
    model = models.SportResource
    form_class = SportForm
    template_name = "rooms/sport_form.html"
    context_object_name = "sport"
    success_url = 'resource/list'


class AddOfficeResourceView(LoginRequiredMixin, CreateView):
    model  = models.OfficeResource
    form_class = OfficeForm
    template_name = "rooms/office_form.html"
    context_object_name = "office"


class AddEventResourceView(LoginRequiredMixin, CreateView):
    model = models.EventResource
    form_class = EventForm
    template_name = "rooms/event_form.html"
    context_object_name = "event"


class AddBeautyResourceView(LoginRequiredMixin, CreateView):
    model = models.BeautyResource
    form_class = BeautyForm
    template_name = "rooms/beauty_form.html"
    context_object_name = "beauty"


class AddLivingResourceView(LoginRequiredMixin, CreateView):
    model = models.LivingResource
    form_class = LivingForm
    template_name = "rooms/living_form.html"
    context_object_name = "living"


class DeleteResourceView(LoginRequiredMixin, DeleteView):
    model = models.BaseResource
    success_url = reverse_lazy("rooms:resource_list") 
    template_name = 'rooms/accept_delete_form.html'


# View for listing all resources
class ResourceListView(ListView):
    model = models.BaseResource  
    template_name = 'rooms/resource_list.html'  
    context_object_name = 'resources'  

    def get_queryset(self):
        return models.BaseResource.objects.select_related(
            'sportresource', 
            'officeresource', 
            'eventresource', 
            'beautyresource', 
            'livingresource'
        ).all()
        

@login_required
def edit_resource(request, pk):
    base_resource = get_object_or_404(models.BaseResource, pk=pk)

    if hasattr(base_resource, 'sportresource'):
        instance = base_resource.sportresource
        form_class = SportForm
    elif hasattr(base_resource, 'officeresource'):
        instance = base_resource.officeresource
        form_class = OfficeForm
    elif hasattr(base_resource, 'eventresource'):
        instance = base_resource.eventresource
        form_class = EventForm
    elif hasattr(base_resource, 'beautyresource'):
        instance = base_resource.beautyresource
        form_class = BeautyForm
    elif hasattr(base_resource, 'livingresource'):
        instance = base_resource.livingresource
        form_class = LivingForm
    
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('rooms:resource_list')
    
    else:
        form = form_class(instance=instance)
    
    return render(request, 'rooms/edit_resource.html', {'form': form})

def detail_resource(request, pk):
    base_resource = get_object_or_404(models.BaseResource, pk=pk)

    instance = base_resource
    template_name = 'rooms/base_detail.html' 

    # 2. Sprawdzamy konkretne typy
    if hasattr(base_resource, 'sportresource'):
        instance = base_resource.sportresource
        template_name = 'rooms/sport_detail.html'
    
    elif hasattr(base_resource, 'officeresource'):
        instance = base_resource.officeresource
        template_name = 'rooms/office_detail.html'
    
    elif hasattr(base_resource, 'eventresource'):
        instance = base_resource.eventresource
        template_name = 'rooms/event_detail.html'
    
    elif hasattr(base_resource, 'beautyresource'):
        instance = base_resource.beautyresource
        template_name = 'rooms/beauty_detail.html'
    
    elif hasattr(base_resource, 'livingresource'):
        instance = base_resource.livingresource
        template_name = 'rooms/living_detail.html'

    
    return render(request, template_name, {'resource': instance})
        

