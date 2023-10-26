"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from authentication.views import LoginPage, SignupForm, logout_user
from feed.views import feed, posts, create_ticket, create_review, create_ticket_and_review, edit_review, edit_ticket

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication App related
    path('', LoginPage.as_view(), name='login'),
    path('signup/', SignupForm.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),

    # Feed App related
    path('feed/', feed, name='feed'),
    path('posts/', posts, name='posts'),
    path('create-ticket/', create_ticket, name=create_ticket),
    path('edit-ticket/<int:ticket_id>/', edit_ticket, name='edit_ticket'),

    path('create-review/<int:ticket_id>/', create_review, name=create_review),
    path('create-review/', create_ticket_and_review,
         name='create_ticket_and_review'),
    path('edit-review/<int:review_id>/', edit_review, name='edit_review'),

]
