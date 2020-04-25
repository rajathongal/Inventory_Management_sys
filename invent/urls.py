from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('laptops/',views.display_laptops,name='display_Laptops'),
    path('desktops/',views.display_desktops,name='display_Desktops'),
    path('mobiles/',views.display_mobiles,name='display_Mobiles'),
    path('add_Laptop/',views.add_laptop,name='add_laptop'),
    path('add_mobile/',views.add_mobile,name='add_mobile'),
    path('add_desktop/',views.add_desktop,name='add_desktop'),
    path('edit_desktop/<int:prod_id>/',views.edit_Desktop,name='edit_Desktop'),
    path('edit_laptop/<int:prod_id>/',views.edit_Laptop,name='edit_Laptop'),
    path('edit_mobile/<int:prod_id>/',views.edit_Mobile,name='edit_Mobile'),
    path('delete_desktop/<int:prod_id>/',views.delete_desktop,name='delete_Desktop'),
    path('delete_laptop/<int:prod_id>/',views.delete_laptop,name='delete_Laptop'),
    path('delete_mobile/<int:prod_id>/',views.delete_mobile,name='delete_Mobile'),
    


]
