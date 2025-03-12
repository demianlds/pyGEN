from django.urls import path
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, MovimientoCreateView, CategoriaCreateView, CategoriaListView
urlpatterns = [
    path('', ProductoListView.as_view(), name='productos_lista'),
    # path('crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('producto/crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('movimiento/crear/<int:product_id>/', MovimientoCreateView.as_view(), name='movimiento_crear'),
    path('categorias/', CategoriaListView.as_view(), name='categorias_lista'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'),
]
