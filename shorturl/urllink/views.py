from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from urllink.models import Link

def link(request,name) :
    link = get_object_or_404(Link, name=name)
    return HttpResponseRedirect(link.url)


