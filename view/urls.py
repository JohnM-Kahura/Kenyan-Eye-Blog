from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import landing_page,discover_view,blog_details_view,write_view,update_blog_view,delete_blog_view
from users.views import login_view,signup_view,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page,name='landing_page'),
    # path('discover/', discover_view,name='discover'),
    path('read/<int:pk>', blog_details_view,name='blog_details'),
    # path('write/',write_view,name='write'),
    # path('update/<int:pk>',update_blog_view,name='update'),
    # path('delete/<int:pk>',delete_blog_view,name='delete'),
    path('login/', login_view,name='login'),
    path('signup/', signup_view,name='signup'),
    path('logout/', logout_view,name='logout'),
    path('accounts/login/', login_view,name='login'),
    # static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    path('reset/',auth_views.PasswordResetView.as_view(template_name='User/password_reset.html'),name='reset_password'),
    path('reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name='User/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/ ',auth_views.PasswordResetConfirmView.as_view(template_name='User/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_pass_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='User/password_reset_complete.html'),name='password_reset_complete'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
