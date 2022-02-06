from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import *
from .serializers import *

from rest_framework.permissions import IsAuthenticated
class IndexView(APIView):    
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
    
class UnidadMedidaView(APIView):    
    def get(self,request):
        dataUnidadMedida = UnidadMedida.objects.all()
        serUnidadMedida = UnidadMedidaSerializer(dataUnidadMedida,many=True)
        return Response({'ok':True,'content':serUnidadMedida.data})
    
class MonedaView(APIView):    
    def get(self,request):
        dataMoneda = Moneda.objects.all()
        serMoneda = MonedaSerializer(dataMoneda,many=True)
        return Response({'ok':True,'content':serMoneda.data})
        
class ProductoView(APIView):    
    permission_classes = [IsAuthenticated]
    def get(self,request):
        dataProducto = Producto.objects.all()
        serProducto = ProductoSerializer(dataProducto,many=True)
        return Response({'ok':True,'content':serProducto.data})
      
    def post(self,request):
        ProductoSer = ProductoSerializer(data=request.data)
        ProductoSer.is_valid(raise_exception=True)
        ProductoSer.save()
        
        context = {
            'ok':True,
            'content':ProductoSer.data
        }
        return Response(context)
    
    def put(self,request,producto_codigo):
        ProductoData = Producto.objects.get(pk=producto_codigo)
        ProductoSer = ProductoSerializer(ProductoData,data=request.data)
        ProductoSer.is_valid(raise_exception=True)
        ProductoSer.save()
        context = {
            'ok':True,
            'content':ProductoSer.data
        }
        return Response(context)
    
    def delete(self,request,producto_codigo):
        ProductoData = Producto.objects.get(pk=producto_codigo)
        ProductoSer = ProductoSerializer(ProductoData)
        ProductoData.delete()
        context = {
            'ok':True,
            'content':ProductoSer.data
        }
        return Response(context)