from django.db import models
from django.template.defaultfilters import slugify

from django_geckoboard import decorators

class GeckoWidget(models.Model):
    title = models.CharField(max_length=128)    
    decorator_title = models.CharField(max_length=64, help_text='The name of the decorator in django-geckoboard.')

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not hasattr(decorators, self.decorator_title):
            raise RuntimeError, "%s is not a valid decorator" % self.decorator_title
        super(GeckoWidget, self).save(*args, **kwargs)

    @property
    def decorator(self):
        return getattr(decorators, self.decorator_title)


class Determinant(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(editable=False, max_length=255, db_index=True, unique=True)
    gecko_widget = models.ForeignKey(GeckoWidget)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Determinant, self).save(*args, **kwargs)

    @property
    def gecko_result(self):
        return [1,77]

    @property
    def gecko_decorator(self):
        return self.gecko_widget.decorator


class DataPoint(models.Model):
    determinant = models.ForeignKey(Determinant)
    month = models.DateField()
    target = models.PositiveIntegerField()
    actual = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('determinant', 'month',)
        unique_together = ('determinant', 'month')

    def __unicode__(self):
        return '%s > %s' % (self.determinant.title, self.month.strftime('%B %Y'))

