"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from web import views
from django.urls import path
app_name='web'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout,name='logout'),
    path('', views.login,name='login'),
    # path('', views.main,name='main'),
    # path('register/', views.register, name='register'),
    path('orm/', views.orm),
    path('pic/', views.pic_list, name='pic_list'),
    path('csv/', views.Smote_csv_list, name='Smote_csv_list'),
    path('loophole/', views.loophole_list, name='loophole_list'),

    #用户管理 添加四个对应数据
    path('user/list/',views.user_list,name='user_list'),
	path('user/info/',views.user_info),
    path('user/edit/',views.user_edit,name='user_edit'),
    path('user/delete/',views.user_delete),

    # Smote 模型
    path('Smote/list/', views.Smote_list, name='Smote_list'),
    path('Smote/info/', views.Smote_info),
    path('Smote/save/', views.Smote_save),
    path('Smote/delete/', views.Smote_delete)

]
