from django.views.decorators.http import require_http_methods
from .models import Stock
from django.http import HttpResponse
from django.core import serializers
import jwt
from datetime import datetime


@require_http_methods(["GET"])
def getstock(request):
    params = request.GET
    ts = int(jwt.decode(params["token"], "login", algorithms="HS256")["exp"])
    print(datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"))
    try:

        stock = Stock.objects.all().filter(code=params["code"])
        return HttpResponse(
            status=200, content=serializers.serialize("json", list(stock))
        )
    except jwt.ExpiredSignatureError:
        return HttpResponse(status=401, content="Token expired")
    except:
        return HttpResponse(status=400)
