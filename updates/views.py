import json

from django.http import JsonResponse, HttpResponse
from django.views.generic import View

from .mixins import JsonResponseMixin
from updates.forms import UpdateModelForm
from .models import Update


def json_example_view(request):
    '''
    URL -- for a REST API
    GET -- Retrieve
    '''

    data = {
        "count": 1000,
        "content": "Some new content",
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content",
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content",
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=4)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')