from django.contrib import admin
from django.urls import path
from . import views
from blog import views as blogViews
from about import views as aboutViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blogViews.index),
    path('about/', aboutViews.index),
    path('', views.index)
]
