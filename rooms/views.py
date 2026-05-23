from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from  rooms.models import BaseResource
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rooms.map import RESOURCE_CONFIG

class AddResourceView(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('rooms:resource_list')
    
    def dispatch(self, request, *args, **kwargs):
        self.resource_config = RESOURCE_CONFIG[self.kwargs['resource_type']]
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.resource_config['model'].objects.all()

    def get_form_class(self):
        return self.resource_config['form']

    def get_template_names(self):
        return [self.resource_config['template']]

    def form_valid(self, form):

        form.instance.creator = self.request.user

        form.instance.category = self.resource_config['category']

        return super().form_valid(form)

class DeleteResourceView(LoginRequiredMixin, DeleteView):
    model = BaseResource
    success_url = reverse_lazy("rooms:resource_list") 
    template_name = 'rooms/accept_delete_form.html'


# View for listing all resources
class ResourceListView(ListView):
    model = BaseResource  
    template_name = 'rooms/resource_list.html'  
    context_object_name = 'resources'  
        

@login_required
def edit_resource(request, pk):
    base_resource = get_object_or_404(BaseResource, pk=pk)

    form_class = RESOURCE_CONFIG[base_resource._meta.model_name.replace('resource', '')]['form']
    
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=base_resource)
        if form.is_valid():
            form.save()
            return redirect('rooms:resource_list')
    
    else:
        form = form_class(instance=base_resource)
    
    return render(request, 'rooms/edit_resource.html', {'form': form})

def detail_resource(request, pk):
    base_resource = get_object_or_404(BaseResource, pk=pk)

    template_name = base_resource.get_template(template_type='detail') 

    return render(request, template_name, {'resource': base_resource})
        

