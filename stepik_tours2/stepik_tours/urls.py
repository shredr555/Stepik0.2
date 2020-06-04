from django.contrib import admin
from django.urls import path
from tours.views import MainView
from tours.views import DepartureView
from tours.views import TourView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('departure/<str:departure>/', DepartureView.as_view()),
    path('tour/<int:id>/', TourView.as_view()),
]
