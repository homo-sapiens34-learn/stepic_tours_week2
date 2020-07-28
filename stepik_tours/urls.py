from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from tours.views import MainView, DepartureView, TourView

urlpatterns = [
                  path('', MainView.as_view()),
                  path('admin/', admin.site.urls),
                  path('departure/<str:departure>/', DepartureView.as_view()),
                  path('tour/<int:id>/', TourView.as_view()),
                  # path('static/')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
