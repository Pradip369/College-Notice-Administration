from django.urls import path
from college import views
from django.views.generic.base import RedirectView
# from rest_framework import routers
# from rest_framework_jwt.views import obtain_jwt_token
from django.urls.conf import include



# router = routers.DefaultRouter()
# router.register(r'branch_api',views.BranchViewSet)
# router.register(r'notice_api',views.NoticeViewSet)



urlpatterns = [
    path('mylist/',views.Mylist.as_view()),
    path('question/create/',views.QuestionCreateview.as_view(success_url="/college/notice")),
    path('profile/edit/<int:pk>',views.ProfileUpdateview.as_view(success_url="/college/notice"),name = 'my_profile'),
    path('notice/<int:pk>',views.Noticedetailview.as_view()),
    path('notice/',views.NoticeListview.as_view()),
    
    # path(r'api/',include(router.urls)),
    # path(r'api-token-auth',obtain_jwt_token),
    
    path('', RedirectView.as_view(url="notice/")),
]
