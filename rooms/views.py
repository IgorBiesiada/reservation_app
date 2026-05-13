from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from . import forms
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class AddResourceView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('rooms:resource_list')
    
    def get_queryset(self):
        resource_type = self.kwargs.get('resource_type')
        if resource_type == 'sport':
            return models.SportResource.objects.all()
        
        elif resource_type == 'office':
            return models.OfficeResource.objects.all()
        
        elif resource_type == 'event':
            return models.EventResource.objects.all()
        
        elif resource_type == 'beauty':
            return models.BeautyResource.objects.all()
        
        elif resource_type == 'living':
            return models.LivingResource.objects.all()

        return models.BaseResource.objects.all()
    
    #def get_context_data(self, **kwargs):
    #    context =  super().get_context_data(**kwargs)
    #    context['creator'] = get_object_or_404(models.User, self.kwargs.get('pk'))
    #    return context

    
    def get_form_class(self):
        resource_type = self.kwargs.get('resource_type')
        if resource_type == 'sport':
            return forms.SportForm
        
        elif resource_type == 'office':
            return forms.OfficeForm
        
        elif resource_type == 'event':
            return forms.EventForm
        
        elif resource_type == 'beauty':
            return forms.BeautyForm
        
        elif resource_type == 'living':
            return forms.LivingForm
        
    def get_template_names(self):
        resource_type = self.kwargs.get('resource_type')

        if resource_type == 'sport':
            return ['rooms/sport_form.html']
        
        elif resource_type == 'office':
            return ['rooms/office_form.html']
        
        elif resource_type == 'event':
            return ['rooms/event_form.html']
        
        elif resource_type == 'beauty':
            return ['rooms/beauty_form.html']
        
        elif resource_type == 'living':
            return ['rooms/living_form.html']
    
    def form_valid(self, form):
        resource_type = self.kwargs.get('resource_type')
        form.instance.creator = self.request.user
        if resource_type == 'sport':
            form.instance.category = 'SPORT'
        
        elif resource_type == 'office':
            form.instance.category = 'OFFICE'
        
        elif resource_type == 'event':
            form.instance.category = 'EVENT'
        
        elif resource_type == 'beauty':
            form.instance.category = 'BEAUTY'
        
        elif resource_type == 'living':
            form.instance.category = 'LIVING'
        
        return super().form_valid(form)

    


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
        form_class = forms.SportForm
    elif hasattr(base_resource, 'officeresource'):
        instance = base_resource.officeresource
        form_class = forms.OfficeForm
    elif hasattr(base_resource, 'eventresource'):
        instance = base_resource.eventresource
        form_class = forms.EventForm
    elif hasattr(base_resource, 'beautyresource'):
        instance = base_resource.beautyresource
        form_class = forms.BeautyForm
    elif hasattr(base_resource, 'livingresource'):
        instance = base_resource.livingresource
        form_class = forms.LivingForm
    
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
        

