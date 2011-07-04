from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from django_geckoboard import decorators

from foundationtargets.models import Determinant

def gecko_xml(request, slug):
    determinant = get_object_or_404(Determinant, slug=slug)
    # Below is complex due to the way decorators are defined in 
    # django-geckoboard.
    func = determinant.gecko_decorator(lambda request: determinant.gecko_xml)
    return HttpResponse(func(request)) 
