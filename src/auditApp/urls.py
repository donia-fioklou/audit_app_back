from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from auditApp.views.AnnexeViews import ChapitreList
from auditApp.views.AnnexeViews import SousChapitreList,ChapitreStatsActuelDetail
from auditApp.views.dashbordViews import ChapitreStatsNoteCible,ChapitreStatsActuel,SousChapitreStatsActuel

urlpatterns = [
    path('chapitre',ChapitreList.as_view() , name='chapitre'),
    path('sous/chapitre',SousChapitreList.as_view() , name='sous-chapitre'),
    path('chapitre-stats-note-cible/', ChapitreStatsNoteCible.as_view(), name='chapitre-stats-note-cible'),
    path('chapitre-stats-actuel/', ChapitreStatsActuel.as_view(), name='chapitre-stats-actuel'),
    path('sous-chapitre-stats-actuel/', SousChapitreStatsActuel.as_view(), name='sous-chapitre-stats-actuel'),
    path('chapitre-stats-actuel/detail/', ChapitreStatsActuelDetail.as_view(), name='chapitre-stats-actuel-detail'),

]
urlpatterns = format_suffix_patterns(urlpatterns)