from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required

from django_geckoboard import decorators

from foundationtargets.models import Determinant
from foundationtargets.forms import DeterminantEditForm

def gecko_xml(request, slug):
    determinant = get_object_or_404(Determinant, slug=slug)
    # Below is complex due to the way decorators are defined in 
    # django-geckoboard.
    func = determinant.gecko_decorator(lambda request: determinant.gecko_result)
    return HttpResponse(func(request)) 

@staff_member_required
def determinant_datapoints_edit(request, id):
    """Surface form"""
    determinant = get_object_or_404(Determinant, id=id)
    if request.method == 'POST':
        form = DeterminantEditForm(request.POST, instance=determinant) 
        if form.is_valid():
            determinant = form.save()
            request.user.message_set.create(message="The determinant has been saved.")
            return HttpResponseRedirect('/admin/foundationtargets/determinant/')
    else:
        form = DeterminantEditForm(instance=determinant) 

    extra = dict(form=form)
    return render_to_response('foundationtargets/determinant_edit.html', extra, context_instance=RequestContext(request))

