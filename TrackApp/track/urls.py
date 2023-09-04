"""
The urls.py contains url defined unser the customer app.
"""
from django.urls import path
from .views.unit_views import UnitView
from .views.visit_views import VisitView


urlpatterns = [
    path('unit', UnitView.as_view(), name='unit_list_create'),

    path('visit', VisitView.as_view(), name='visit_list_create'),
]
