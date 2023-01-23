""" Views """

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
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

    def get_queryset(self):
        """
        Function which filters the my cashbooks page to those
        created by the user.
        """
        return Cashbook.objects.filter(author=self.request.user)


class CashbookDetail(generic.DetailView):
    """
    This view is used to allow users to view cashbooks in detail.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        This function obtains cashbook data to display to the user.
        """
        cashbook = Cashbook.objects.get(slug=slug)
        return render(request, "cashbook_detail.html", {"cashbook": cashbook})


class CashbookCreate(SuccessMessageMixin,
                     generic.CreateView):
    """
    This view is used to allow the logged in user to create their own cashbook.
    """
    form_class = CashbookForm
    template_name = 'create_cashbook.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        This method ensures that the user is set as the
        author of the cashbook.
        """
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function adds the cashbook title into the success message.
        Credit to the Django Documentation.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.book_title,
        )

    def get_success_url(self):
        return reverse('my_cashbooks')


class CashbookUpdate(SuccessMessageMixin,
                     generic.UpdateView):
    """
    This view is used to allow the logged in user to update their cashbook.
    """
    queryset = Cashbook.objects.all()
    form_class = CashbookForm
    template_name = 'update_cashbook.html'
    success_message = "%(calculated_field)s was updated successfully"

    def form_valid(self, form):
        """
        This method ensures that the user is set as the
        creator of the cashbook.
        """
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function adds the cashbook title into the success message.
        Credit to the Django Documentation.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.book_title,
        )


class CashbookDelete(generic.DeleteView):
    """
    This view is used to allow the logged in user to delete their cashbook.
    """
    queryset = Cashbook.objects.all()
    template_name = 'delete_cashbook.html'
    success_message = "Cashbook was deleted successfully"
    success_url = reverse_lazy('my_cashbooks')

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display a delete message.
        Credit to Stack Overflow.
        """
        messages.warning(self.request, self.success_message)
        return super(CashbookDelete, self).delete(request, *args, **kwargs)
