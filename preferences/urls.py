from django.urls import re_path, path

from preferences import views

app_name = 'preferences'

urlpatterns = [
    re_path(r'^account/preferences/(?P<pk>[0-9]+)$',
            views.GetDeleteUpdatePreference.as_view(),
            name='get_delete_update_movie',
            ),
    path('account/preferences',
         views.ListCreatePreferences.as_view(),
         name='list_create_preferences',
         ),
    path('getRecommendation',
         views.RecommendationView.as_view(),
         name='get_recommendations',
         ),
]
