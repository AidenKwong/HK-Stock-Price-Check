from django.views.decorators.http import require_http_methods
from .models import Stock
from django.http import HttpResponse
from django.core import serializers


@require_http_methods(["GET"])
def getstock(request):
    params = request.GET
    try:
        stock = Stock.objects.all().filter(code=params["code"])
        return HttpResponse(
            status=200, content=serializers.serialize("json", list(stock))
        )
    except:
        return HttpResponse(status=400)
