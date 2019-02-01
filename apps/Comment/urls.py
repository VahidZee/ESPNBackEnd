# General Imports
from django.urls import path

# Views Import
from . import views as comment_views

urlpatterns = [
    path('<int:commented_id>',
         comment_views.get_comment_field,
         name='get_comment_field_by_id'
         ),
    path('like/<int:comment_id>',
         comment_views.like_comment,
         name='like_comment_by_id'
         )
]
