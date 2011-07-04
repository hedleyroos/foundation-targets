import datetime

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
        if self.gecko_decorator is decorators.geck_o_meter:
            now = datetime.datetime.now()
            dt_month = datetime.date(now.year, now.month, 1)
            try:
                datapoint = self.datapoint_set.get(month=dt_month)
            except DataPoint.DoesNotExist:
                return [0, 0, 0]
            else:                                
                return [0, datapoint.actual, datapoint.target]

        elif self.gecko_decorator is decorators.line_chart:
            year = datetime.datetime.now().year
            datapoints = self.datapoint_set.filter(month__year=year).order_by('month')
            values = []
            x_axis = []
            v_min = 1000000000
            v_max = 0
            for dp in datapoints:
                values.append(dp.actual)
                x_axis.append(dp.month.strftime('%b'))
                if dp.target < v_min:
                    v_min = dp.target
                if dp.actual < v_min:
                    v_min = dp.actual
                if dp.target > v_max:
                    v_max = dp.target
                if dp.actual > v_max:
                    v_max = dp.actual
            if v_min == 1000000000:
                v_min = 0
            y_axis = [v_min, v_max]
            return (values, x_axis, y_axis)

        else:
            raise RuntimeError, "This Gecko decorator is not implemented"

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

