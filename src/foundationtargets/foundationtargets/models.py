from django.db import models

class GeckoWidget(models.Model):
    title = models.CharField(max_length=128)    

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title


class Determinant(models.Model):
    title = models.CharField(max_length=128)
    gecko_widget = models.ForeignKey(GeckoWidget)

    class Meta:
        ordering = ('title',)

    def __unicode__(self):
        return self.title


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

