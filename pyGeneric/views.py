from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto, Movimiento, Categoria
from .forms import ProductoForm
class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'pyGeneric/categoria_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['name']
    template_name = 'pyGeneric/categoria_form.html'
    success_url = reverse_lazy('categorias_lista')

    def form_valid(self, form):
        messages.success(self.request, 'Categoría creada con éxito.')
        return super().form_valid(form)

from django.contrib.auth.mixins import LoginRequiredMixin

class ProductoListView(LoginRequiredMixin, ListView):
    model = Producto
    context_object_name = 'object_list'
    template_name = 'pyGeneric/producto_list.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        categoria_id = self.request.GET.get('category')
        if categoria_id:
            context['object_list'] = Producto.objects.filter(category_id=categoria_id)
        return context

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'pyGeneric/producto_form.html'  # El template que vamos a crear para el formulario
    fields = ['name','category', 'min_stock', 'actual_stock']  # Los campos del formulario
    success_url = reverse_lazy('productos_lista')  # Redirige a la lista de productos después de guardar el nuevo producto

    def form_valid(self, form):
        producto = form.save()
        if producto.actual_stock < producto.min_stock:
            messages.warning(self.request, 'El stock actual es inferior al mínimo.')
        return super().form_valid(form)

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos_lista')

class MovimientoCreateView(CreateView):
    model = Movimiento
    template_name = 'pyGeneric/movimiento_form.html'
    fields = ['type', 'amount', 'user']
    success_url = reverse_lazy('productos_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Producto, id=self.kwargs['product_id'])
        return context

    def form_valid(self, form):
        # Obtener el producto basado en el ID
        movimiento = form.save(commit=False)
        movimiento.product = get_object_or_404(Producto, id=self.kwargs['product_id'])

        # Validar stock para salida
        if movimiento.type == 'salida' and movimiento.amount > movimiento.product.actual_stock:
            form.add_error('amount', 'No hay suficiente stock disponible.')
            return self.form_invalid(form)

        # Guardar movimiento y actualizar stock
        movimiento.save()
        if movimiento.type == 'entrada':
            movimiento.product.actual_stock += movimiento.amount
        elif movimiento.type == 'salida':
            movimiento.product.actual_stock -= movimiento.amount
        movimiento.product.save()

        messages.success(self.request, 'Movimiento registrado exitosamente.')
        return super().form_valid(form)

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos_lista')
    template_name = 'pyGeneric/producto_list.html'

