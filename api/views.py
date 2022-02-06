from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import *
from .serializers import *

from rest_framework.permissions import IsAuthenticated
class IndexView(APIView):    
    # permission_classes = [IsAuthenticated]    
    def get(self,request):
        context = {'ok':True,
                   'message':'el servidor está activo!'
                   }
        return Response(context)
    
class LineaView(APIView):    
    def get(self,request):
        dataLinea = Linea.objects.all()
        serLinea = LineaSerializer(dataLinea,many=True)
        return Response({'ok':True,'content':serLinea.data})
    
class MarcaView(APIView):    
    def get(self,request):
        dataMarca = Marca.objects.all()
        serMarca = MarcaSerializer(dataMarca,many=True)
        return Response({'ok':True,'content':serMarca.data})
        