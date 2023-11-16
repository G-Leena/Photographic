"""
URL configuration for ClienT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MYapp import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.renderPage),
    path('contactus',views.contactus),
    path('contact_form',views.contact_form),
    path('enquiry',views.enquiry),
    path('admin-login/',views.admin_login, name="admin_login"),
    path('admin-logout/',views.admin_logout, name="admin_logout"),
    path('admin-home/',views.admin_home, name="admin_home"),
    path('add_update/',views.add_or_update_img, name="add_image"),
    path('add_update/<int:id>/',views.add_or_update_img, name="update_image"),
    path('delete-image/<int:id>/',views.delete_image, name="delete_image"),
    path('image-view/<str:category>/',views.image_view, name="image_view"),
    path('upper-slider/',views.upper_slider, name="upper_slider"),
    path('middle-slider/',views.middle_slider, name="middle_slider"),
    


] + static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
