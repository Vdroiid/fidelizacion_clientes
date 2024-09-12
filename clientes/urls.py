from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clientes.views import IndexView, ClienteView, MyModelViewSet

from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register(r'UsuarioPersonalizado', MyModelViewSet)


urlpatterns = [
    path('inde/', IndexView),
    path('', include(router.urls)),
    path('tabla_clientes/', views.ClienteView, name="clientes_view"),

    # Otras URLS de tu aplicación
    # TOKENS
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #path('admin/', admin.site.urls),  # URL para el panel de administración
]
