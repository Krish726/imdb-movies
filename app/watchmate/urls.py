from django.contrib import admin
from django.urls import path, include
#from watchlist_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/', include('watchlist_app.api.urls')),
    path('account/',include('user_app.api.urls')),
    # now we are using our own authentication. hats why not using temp login
    #path('api-auth/',include('rest_framework.urls')) 
]
