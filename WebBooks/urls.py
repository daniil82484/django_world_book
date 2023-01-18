from django.contrib import admin
from django.urls import path
from catalog import views
from django.urls import path, include, re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('authors_add/', views.authors_add, name="authors_add"),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookListView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorsListView.as_view(), name='authors'),

    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),

    re_path(r'mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
