from django.views.generic import TemplateView


class ShopListView(TemplateView):
    template_name = 'shop/checkout.html'
