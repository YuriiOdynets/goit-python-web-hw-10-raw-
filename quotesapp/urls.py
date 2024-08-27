from django.urls import path
from . import views

app_name="quotesapp"

urlpatterns=[
    path('', views.main, name = 'index'),
    path('author/<int:author_id>/', views.author_detail, name='author_details'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('delete_author/<int:author_id>', views.delete_author, name='delete_author'),
    path('delete_quote/<int:note_id>', views.delete_quote, name='delete_quote'),
]