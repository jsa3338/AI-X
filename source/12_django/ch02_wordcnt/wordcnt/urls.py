# wordcnt 패키지만의 urls.py
# /wordcnt : text 입력 form (POST/GET)
# /wordcnt/about : 입력된 text wordcount
# /wordcnt/result : 도움말 페이지

from django.urls import path
from wordcnt import views
app_name = 'wordcnt'
urlpatterns = [
    path('', views.wordinput, name='wordinput'), # wordcnt/
    path('about/', views.about, name='about'),  # wordcnt/about/
    path('result/', views.result, name='result'),  # wordcnt/result/

]