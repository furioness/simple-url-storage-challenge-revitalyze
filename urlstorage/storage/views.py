from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import URL



class ListURLsView(LoginRequiredMixin, ListView):
    template_name = "storage/url_list.html"
    context_object_name = "urls"
    model = URL
    
    def get_queryset(self):
        return self.request.user.urls.all()


class AddURLView(LoginRequiredMixin, CreateView):
    template_name = "storage/url_add.html"
    model = URL
    fields = ('url', )
    success_url = reverse_lazy("storage:url_add")
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    