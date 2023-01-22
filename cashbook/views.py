""" Views """

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Cashbook
from .forms import CashbookForm


class CashbookList(generic.ListView):
    """
    This view is used to allow the user to view a list of cashbooks.
    """
    model = Cashbook
    queryset = Cashbook.objects.order_by("-created_on")
    template_name = 'my_cashbooks.html'
    paginate_by = 9


class CashbookDetail(generic.DetailView):
    """
    This view is used to allow users to view cashbooks in detail.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        This function obtains recipe data to display to the user.
        """
        cashbook = Cashbook.objects.get(slug=slug)
        return render(request, "cashbook_detail.html", {"cashbook": cashbook})
