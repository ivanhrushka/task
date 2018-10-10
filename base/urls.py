from django.urls import path
from .views import FileUploadView, GetOrderDataApiView


urlpatterns = [
    path('csv/upload/', FileUploadView.as_view(), name='csv-upload'),
    path('orders/<int:inner_id>/', GetOrderDataApiView.as_view(), name='get-order-data'),
]
