from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import HouseInfo


def homepage(request):
    return render(request, 'Base.html')


class Postlistview(ListView):
    model = HouseInfo
    context_object_name = 'HouseInfo'
    template_name = 'HouseInfo.html'
    ordering=['-Date_Posted']



class Postcreateview(CreateView):
    model = HouseInfo
    template_name = 'HouseInfo_form.html'
    context_object_name = 'form'
    fields = "__all__"

    # def form_valid(self, form):
    #     form.instance.Author=self.request.user
    #     return super().form_valid(form)
