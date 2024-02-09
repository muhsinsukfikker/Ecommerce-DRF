from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router=DefaultRouter()
router.register('products',views.ProductView,basename='products')
router.register('baskets',views.BasketView,basename='baskets')
router.register('baskets/item',views.BasketItemView,basename='basketitem')
urlpatterns = [

    path('register/',views.RegisterView.as_view(),name='register'),
    path('token/',ObtainAuthToken.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    
]+ router.urls
