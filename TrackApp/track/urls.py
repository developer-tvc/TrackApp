"""
The urls.py contains url defined unser the customer app.
"""
from django.urls import path
from .views.worker_views import WorkView, WorkerDescriptionDetail
from .views.unit_views import UnitView, UnitDescriptionDetail
from .views.visit_views import VisitView


urlpatterns = [
    path('worker', WorkView.as_view(), name='worker_list_create'),
    path('worker/<worker_id>', WorkerDescriptionDetail.as_view(), name='single_worker'),

    path('unit', UnitView.as_view(), name='unit_list_create'),
    path('unit/<unit_id>', UnitDescriptionDetail.as_view(), name='single_unit'),

    path('visit', VisitView.as_view(), name='visit_list_create'),
]
