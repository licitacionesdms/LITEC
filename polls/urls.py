from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, login_user, logout_user, homevis, get_columns, registrar_usuario, dispositivos, dispositivos_vis
from .views import subir_licitacion_vis, editar_dispositivos, subir_licitacion, vencimiento, trazabilidad
from .views import eventos_vencimiento, agregar_evento, password_reset_request, edicion_masiva, descargar_dispositivos
from .views import subir_dispositivos_mapeo, get_columns_dispositivos, agregar_dispositivo_individual, eliminar_dispositivo, descargar_formato_licitacion


urlpatterns = [
    path("", login_user, name="login"),  # Página de inicio de sesión
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('homevis/', homevis, name='homevis'),
    path('registrarse/', registrar_usuario, name='registro'),
    path("ver_dispositivos/",dispositivos,name="dispositivos"),
    path("ver_dispositivos_visualizador/",dispositivos_vis,name="dispositivos_vis"),
    path("editar_dispositivos/",editar_dispositivos,name="editar_dispositivos"),
    path("edicion_masiva/",edicion_masiva,name="edicion_masiva"),
    path("licitaciones_visualizador",subir_licitacion_vis,name="licitaciones_vis"),
    path("trazabilidad/",trazabilidad,name="trazabilidad"),
    path('subir/', subir_licitacion, name='licitaciones'),
    path('get_columns/', get_columns, name='get_columns'),
    path("password_change/",auth_views.PasswordChangeView.as_view(template_name="password.html"),name="password_change",),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"),name="password_change_done",),
    path("alertas_vencimiento/",vencimiento,name="vencimiento"),
    path('api/events/', eventos_vencimiento, name='api_events'),
    path('agregar-evento/',agregar_evento, name='agregar_evento'),
    path('password_reset/', password_reset_request, name='password_reset'),
    path('descargar-dispositivos/',descargar_dispositivos, name='descargar_dispositivos'),
    path('subir_dispositivos_mapeo/', subir_dispositivos_mapeo, name='subir_dispositivos_mapeo'),
    path('get_columns_dispositivos/', get_columns_dispositivos, name='get_columns_dispositivos'),
    path('agregar_dispositivo_individual/', agregar_dispositivo_individual, name='agregar_dispositivo_individual'),
    path('dispositivos/eliminar/<int:id>/',eliminar_dispositivo, name='eliminar_dispositivo'),
    path('descargar-formato-licitacion/', descargar_formato_licitacion, name= 'descargar_formato_licitacion')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

