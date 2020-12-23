from django.urls import path
from .views import MainPageView, FeedbackView

urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('feedback/', FeedbackView.as_view(), name='post_feedback')
]
