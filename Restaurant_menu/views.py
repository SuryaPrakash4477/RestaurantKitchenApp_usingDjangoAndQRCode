from typing import Any
from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE

# Create your views here.
class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = 'menulist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "itemdetail.html"


def about(request):
    return render(request, "about.html")