from django.shortcuts import render
from django.views import View
from .forms import CakeDesigningForm
from rest_framework.views import APIView
from .models import Feeling, Taste
from rest_framework.response import Response
from .serializers import FeelingSerializers, TasteSerializers


# Create your views here.

class CakeDesigning(View):
    def get(self, request):
        f = CakeDesigningForm()
        print(f)
        return render(request, 'Cake_designing/cake_design.html', {'form': f})


class FeelingAndTasteAPI(APIView):
    def get(self, request, feeling_id, taste_id):
        feeling = Feeling.objects.get(id=feeling_id)
        taste = Taste.objects.get(id=taste_id)
        feeling_serial = FeelingSerializers(feeling)
        taste_serial = TasteSerializers(taste)
        f = feeling_serial.data
        t = taste_serial.data

        return Response({'feeling':f, 'taste':t})
