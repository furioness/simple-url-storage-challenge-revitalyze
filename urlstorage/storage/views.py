from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.utils import IntegrityError
from django.http import HttpResponseRedirect

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
    success_message = "URL {} added successfully."
    duplicate_message = "URL {} is already stored."
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = form.cleaned_data['url']

        try:
            self.object = form.save()
        except IntegrityError:
            messages.info(self.request, self.duplicate_message.format(url))
        else: 
            messages.success(self.request, self.success_message.format(url))

        return HttpResponseRedirect(reverse_lazy("storage:add"))
        
    