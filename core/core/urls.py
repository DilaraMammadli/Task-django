
from django.contrib import admin
from django.urls import path, include
# from hometask.views import product_list_view, product_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("hometask.urls"))
#     path("list/", product_list_view),
#     path("detail/<id>", product_detail_view),
]
