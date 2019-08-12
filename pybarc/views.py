from django.http import HttpResponse
from django.template import loader
from pybarc.barcode import handle_rendering

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def handle_image(request, prodcode):
    return HttpResponse(handle_rendering(prodcode))
