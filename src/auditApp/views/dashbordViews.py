from rest_framework.views import APIView
from rest_framework.response import Response
from auditApp.models import Chapitre
from auditApp.models.ResponseSousChapitre import ReponseSousChapitre
from auditApp.models.SousChapitre import SousChapitre

class ChapitreStatsNoteCible(APIView):
    def get(self,request):
        chapitres = Chapitre.objects.all()
        chapitre_num = [chapitre.numero for chapitre in chapitres]
        chapitre_note_cible = [chapitre.NoteCible for chapitre in chapitres]
        reponse = {
            'chapitre_num': chapitre_num,
            'chapitre_note_cible': chapitre_note_cible
        }

        return Response(reponse)

class ChapitreStatsActuel(APIView):
    def get(self, request):
        dic_stats_actuel = {'chapitre_num':[],'moy_chap':[]}
        chapitres = Chapitre.objects.all()
        for chapitre in chapitres:
            dic_stats_actuel['chapitre_num'].append(chapitre.numero)
            sous_chapitres = SousChapitre.objects.filter(chapitre=chapitre)
            nbre_sous_chap = len(sous_chapitres)
            note_sous_chap = 0
            for sous_chapitre in sous_chapitres:
                reponse_sous_chap = ReponseSousChapitre.objects.filter(sous_chapitre=sous_chapitre).last()
                if reponse_sous_chap :
                    note_sous_chap += reponse_sous_chap.point
            moy_chap = round((note_sous_chap/nbre_sous_chap),2)
            dic_stats_actuel['moy_chap'].append(moy_chap)

        return Response(dic_stats_actuel)
    
class SousChapitreStatsActuel(APIView):
    def get(self, request):
        sous_chapitres = SousChapitre.objects.all()
        sous_chapitre_num = [sous_chapitre.numero for sous_chapitre in sous_chapitres]
        sous_chapitre_note_cible = [ReponseSousChapitre.objects.filter(sous_chapitre=sous_chapitre).last().point for sous_chapitre in sous_chapitres]
        reponse = {
            'sous_chapitre_num': sous_chapitre_num,
            'sous_chapitre_note_cible': sous_chapitre_note_cible
        }

        return Response(reponse)