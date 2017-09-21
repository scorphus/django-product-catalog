"""Managers of Zinnia"""

from django.db import models
from django.utils import timezone

DRAFT = 0
HIDDEN = 1
PUBLISHED = 2

def product_published(queryset):
    """
    Return only the entries published.
    """
    now = timezone.now()
    return queryset.filter(
        models.Q(start_publication__lte=now) |
        models.Q(start_publication=None),
        models.Q(end_publication__gt=now) |
        models.Q(end_publication=None),
        status=PUBLISHED)


class ProductPublishedManager(models.Manager):
    """
    Manager to retrieve published entries.
    """

    def get_queryset(self):
        """
        Return published entries.
        """
        return product_published(
            super(ProductPublishedManager, self).get_queryset())

class ProductsRelatedPublishedManager(models.Manager):
    """
    Manager to retrieve objects associated with published entries.
    """

    def get_queryset(self):
        """
        Return a queryset containing published entries.
        """
        now = timezone.now()
        return super(
            ProductsRelatedPublishedManager, self).get_queryset().filter(
            models.Q(products__start_publication__lte=now) |
            models.Q(products__start_publication=None),
            models.Q(products__end_publication__gt=now) |
            models.Q(products__end_publication=None),
            products__status=PUBLISHED
            ).distinct()
