""" Models """

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Cashbook(models.Model):
    """ Model for Cashbook """
    book_title = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='cashbooks')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    book_category = models.TextField()
    spend_item = models.TextField()
    spend_amount = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """ Ensures cashbooks are listed in date order """
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        """ Function ensuring a user created cashbook generates a new slug """
        self.slug = slugify(self.created_on)
        super(Cashbook, self).save(*args, **kwargs)

    def __str__(self):
        """ Returns the book_title """
        return f"{self.book_title}"

    def __str__(self):
        """ Returns the book_category """
        return f"{self.book_category}"

    def get_absolute_url(self):
        """ Obtains cashbook_detail page after user edits """
        return reverse('cashbook_detail', kwargs={'slug': self.slug})
