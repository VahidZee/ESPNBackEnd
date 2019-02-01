# General Imports
from django.urls import path

# Views Import
from . import views as comment_views

urlpatterns = [
    path('<int:id>',
         comment_views.get_comment_field,
         name='get_comment_field_by_id'
         ),
]
