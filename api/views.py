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
  
class UbigeoView(APIView):    
    def get(self,request):
        dataUbigeo = Ubigeo.objects.all()
        serUbigeo = UbigeoSerializer(dataUbigeo,many=True)
        return Response({'ok':True,'content':serUbigeo.data})
    
class Tipo_documentoView(APIView):    
    def get(self,request):
        dataTipo_documento = Tipo_documento.objects.all()
        serTipo_documento = Tipo_documentoSerializer(dataTipo_documento,many=True)
        return Response({'ok':True,'content':serTipo_documento.data})

class ClientesView(APIView):    
    def get(self,request):
        dataClientes = Clientes.objects.all()
        serClientes = ClientesSerializer(dataClientes,many=True)
        return Response({'ok':True,'content':serClientes.data})
    
    def post(self,request):
        ClientesSer = ClientesSerializer(data=request.data)
        ClientesSer.is_valid(raise_exception=True)
        ClientesSer.save()
        
        context = {
            'ok':True,
            'content':ClientesSer.data
        }
        return Response(context)
    
    def put(self,request,clientes_codigo):
        ClientesData = Clientes.objects.get(pk=clientes_codigo)
        ClientesSer = ClientesSerializer(ClientesData,data=request.data)
        ClientesSer.is_valid(raise_exception=True)
        ClientesSer.save()
        context = {
            'ok':True,
            'content':ClientesSer.data
        }
        return Response(context)
    
    def delete(self,request,clientes_codigo):
        ClientesData = Clientes.objects.get(pk=clientes_codigo)
        ClientesSer = ClientesSerializer(ClientesData)
        ClientesData.delete()
        context = {
            'ok':True,
            'content':ClientesSer.data
        }
        return Response(context)
    
class PedidoView(APIView):    
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        dataPedido = Pedido.objects.all()
        serPedido = PedidoSerializer(dataPedido,many=True)
        return Response({'ok':True,'content':serPedido.data})
      
    def post(self,request):
        PedidoSer = PedidoSerializer(data=request.data)
        PedidoSer.is_valid(raise_exception=True)
        PedidoSer.save()
        
        context = {
            'ok':True,
            'content':PedidoSer.data
        }
        return Response(context)
    
    def put(self,request,pedido_codigo):
        PedidoData = Pedido.objects.get(pk=pedido_codigo)
        PedidoSer = PedidoSerializer(PedidoData,data=request.data)
        PedidoSer.is_valid(raise_exception=True)
        PedidoSer.save()
        context = {
            'ok':True,
            'content':PedidoSer.data
        }
        return Response(context)
    
    def delete(self,request,pedido_codigo):
        PedidoData = Pedido.objects.get(pk=pedido_codigo)
        PedidoSer = PedidoSerializer(PedidoData)
        PedidoData.delete()
        context = {
            'ok':True,
            'content':PedidoSer.data
        }
        return Response(context)
    
class PedidoDetalleView(APIView):    
    # permission_classes = [IsAuthenticated]
    def get(self,request):
        dataPedidoDetalle = PedidoDetalle.objects.all()
        serPedidoDetalle = PedidoDetalleSerializer(dataPedidoDetalle,many=True)
        return Response({'ok':True,'content':serPedidoDetalle.data})
      
    def post(self,request):
        PedidoDetalleSer = PedidoDetalleSerializer(data=request.data)
        PedidoDetalleSer.is_valid(raise_exception=True)
        PedidoDetalleSer.save()
        
        context = {
            'ok':True,
            'content':PedidoDetalleSer.data
        }
        return Response(context)
    
    def put(self,request,pedidodetalle_codigo):
        PedidoDetalleData = PedidoDetalle.objects.get(pk=pedidodetalle_codigo)
        PedidoDetalleSer = PedidoDetalleSerializer(PedidoDetalleData,data=request.data)
        PedidoDetalleSer.is_valid(raise_exception=True)
        PedidoDetalleSer.save()
        context = {
            'ok':True,
            'content':PedidoDetalleSer.data
        }
        return Response(context)
    
    def delete(self,request,pedidodetalle_codigo):
        PedidoDetalleData = PedidoDetalle.objects.get(pk=pedidodetalle_codigo)
        PedidoDetalleSer = PedidoDetalleSerializer(PedidoDetalleData)
        PedidoDetalleData.delete()
        context = {
            'ok':True,
            'content':PedidoDetalleSer.data
        }
        return Response(context)