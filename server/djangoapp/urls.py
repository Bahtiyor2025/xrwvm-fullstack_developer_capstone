from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration
    path('register/', views.registration, name='register'),

    # Path for login
    path(route='login', view=views.login_user, name='login'),

    # Path for logout
    path('logout/', views.logout_user, name='logout'),

    # Path for dealer reviews view (future implementation)
    # path('dealer-reviews/', views.get_dealer_reviews, name='dealer_reviews'),

    # Path for adding a review (future implementation)
    # path('add-review/', views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
