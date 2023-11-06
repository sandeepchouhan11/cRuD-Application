from django.urls import path
from.import views
urlpatterns = [
   path('',views.index),
   path('ragistration/', views.ragistration),
   path("table/",views.table),
   path("delete/<int:pk>/", views.user_delete, name='delete '),
   path("update/<int:uid>/", views.update_deatials, name='update'),
   path('update_view/',views.update_view),
]


 