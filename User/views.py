from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404

# Create your views here.
class RegView(CreateView):
    model = Register
    form_class = RegFrom
    template_name = "Basic.html"
    success_url = "Good"
    
class OrderView(CreateView):
    model = Order
    form_class = OrderFrom
    template_name = "order.html"
    success_url = "Good"
    
class UpdateView(UpdateView):
    model = Register
    form_class = UpdateFrom
    template_name = "Update.html"
    success_url = "Good"

class OrderListView(ListView):
    model = Order
    template_name = 'order-list.html'
    context_object_name = 'orders'
    def get(self, request, pk): 
        user = get_object_or_404(Register, pk=pk) 
        return Order.objects.filter(card=user)
    
class UserListView(ListView):
    model = Register
    form_class = User_listFrom
    template_name = 'user-list.html'
    context_object_name = 'users'
    
class UserDeleteView(ListView):
    model = Register
    form_class = UserDeleterom
    template_name = 'Delete.html'
    success_url = "Good"
    
class LogView(CreateView):
    model = Register
    form_class = LogFrom
    template_name = "Login.html"
    success_url = "Good"
    def form_valid(self, form):
        # Retrieve the username and password from the form
        username = form.cleaned_data['ism']
        password = form.cleaned_data['password']

        # Authenticate the user
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            # Invalid credentials, add an error to the form
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)