from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseRedirect, HttpResponseNotFound, HttpResponseBadRequest
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
from django.views import View
import json
from django.urls import reverse

class JsonNormalizer(View):
    def get(self, req):
        return HttpResponse("json running")
    def post(self, req: HttpRequest):
        if req.body:
            data = json.loads(req.body)
            for k, v in data.items():
                if k == "name":
                    data.update({k: v.capitalize()})
            print(data)
            return JsonResponse(data, safe=False) 
            
        return HttpResponse("no body")

class CheckUserAgent(View):
    def get(self, req: HttpRequest):
        agent = req.META.get('HTTP_USER_AGENT', '')

        if "Mobile" in agent:
            return HttpResponseRedirect(reverse("mobile-page"))
        
        return HttpResponse("Welcome back!")
        


def mobile_page(req):
    return HttpResponse("this is mobile page")


data_dict = {}


def get_data( req: HttpRequest, key: str):
    if key in data_dict:
        return HttpResponse(data_dict[key])
    return HttpResponseNotFound()

def post_data( req: HttpRequest):
    if req.body:
        data = json.loads(req.body)
        data_dict.update(data)
        return JsonResponse(data_dict)
    return HttpResponseBadRequest()