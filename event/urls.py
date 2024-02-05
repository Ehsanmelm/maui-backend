from . import views
from django.urls import path


urlpatterns = [
    path('create_event/<int:id>/' , views.CreateEventUserView.as_view()),
    path('select_event/<int:id>/' , views.EvetnUserView.as_view()),
    path('event_list/' , views.ShowEventsView.as_view()),
    # path('create_event/<int:id>/<int:event_id>' , views.CreateEventUserView..as_view())
]