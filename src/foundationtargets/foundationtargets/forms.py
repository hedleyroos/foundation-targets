import datetime

from django import forms
from django.conf import settings
from django.utils.datastructures import SortedDict

from foundationtargets.models import Determinant, DataPoint

class DeterminantEditForm(forms.Form):
    instance = None

    def __init__(self, data=None, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super(DeterminantEditForm, self).__init__(data, *args, **kwargs)

    def clean(self):
        for k, v in self.data.items():
            if k.startswith('month_'):
                dc, month, year, value_type = k.split('_')
                try: 
                    int(v)
                except ValueError:
                    raise forms.ValidationError("%s is not a valid integer." % v)

    def save(self, commit=True):
        # Trust the request. Yes, I know you're supposed to sanitise but this 
        # method is callable by staff only.
        for k, v in self.data.items():
            if k.startswith('month_'):
                dc, month, year, value_type = k.split('_')
                dt_month = datetime.date(int(year), int(month), 1)
                try:
                    dp = DataPoint.objects.get(determinant=self.instance, month=dt_month)
                except DataPoint.DoesNotExist:
                    dp = DataPoint(determinant=self.instance, month=dt_month, target=0, actual=0) 
                setattr(dp, value_type, int(v))
                dp.save()

        return self.instance

    @property
    def structure(self):
        result = SortedDict()
        year = datetime.datetime.now().year
        for n in range(year, year+2):
            result[n] = []

        datapoints_map = {}
        datapoints = DataPoint.objects.filter(determinant=self.instance).order_by('month')
        for datapoint in datapoints:
            datapoints_map[datapoint.month] = datapoint

        for year in result.keys():
            for month in range(1, 13):
                dt_month = datetime.date(year, month, 1)
                di = dict(date=dt_month, target=None, actual=None)

                for value_type in ('target', 'actual'):
                    v = self.data.get('month_%d_%d_%s' % (month, year, value_type), None)
                    if v:
                        try:
                            di[value_type] = int(v)
                        except ValueError:
                            pass

                    if (di[value_type] is None):
                        if datapoints_map.has_key(dt_month):
                            di[value_type] = getattr(datapoints_map[dt_month], value_type)
                        else:
                            di[value_type] = 0

                result[year].append(di)
                
        return result

