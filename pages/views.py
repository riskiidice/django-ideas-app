from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import View, FormView, CreateView
from newsletter.forms import JoinForm
from .models import Page
# Create your views here.

# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'pages/home.html')

class HomeView(SuccessMessageMixin,CreateView):
    template_name = 'pages/home.html'
    form_class = JoinForm
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['page_obj'] = Page.objects.all().first()
        return context

    def get_success_message(self, cleaned_data):
        print (cleaned_data)
        return "Thank your for joining !"
