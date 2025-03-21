
from store.models import product  # Use lowercase 'product' to match the model name
# cart.py

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prod(self):
        product_ids = self.cart.keys()
        products = product.objects.filter(id__in=product_ids)
        return products


