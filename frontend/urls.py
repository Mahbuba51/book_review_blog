from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # This will match any URL and serve the React app's index.html
    path('', TemplateView.as_view(template_name='index.html'), name='react-app'),
]
