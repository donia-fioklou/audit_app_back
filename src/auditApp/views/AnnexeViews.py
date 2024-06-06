from rest_framework.views import APIView
from rest_framework.response import Response
from auditApp.models.Chapitre import Chapitre
from auditApp.models.SousChapitre import SousChapitre
from auditApp.serializers.Chapitre import ChapitreSerializer
from auditApp.serializers.SousChapitre import SousChapitreSerializer
from auditApp.serializers.ResponseSousChapitreSerializer import ResponseSousChapitreSerializer
from auditApp.models.ResponseSousChapitre import ReponseSousChapitre
from rest_framework.response import Response
from rest_framework import status
class ChapitreList(APIView):
    def get(self, request):
        chapitres = Chapitre.objects.all()
        serializer = ChapitreSerializer(chapitres, many=True)
        return Response(serializer.data)
    
class SousChapitreList(APIView):
    def get(self, request):
        chapitres = Chapitre.objects.all()
        response_data = []
        for chapitre in chapitres:
                sous_chapitres = SousChapitre.objects.filter(chapitre=chapitre)
                sous_chapitres_serializer = SousChapitreSerializer(sous_chapitres, many=True)
                response_data.append({
                    'chapitre_id': chapitre.id,
                    'chapitre_nom': chapitre.nom,
                    'sous_chapitres': sous_chapitres_serializer.data
                })

        return Response(response_data)

    def post(self, request):
        reponses_data = request.data.get('reponses', [])
        try:
            for reponse_data in reponses_data:
                print('reponse_data', reponse_data)
                sous_chapitre_obj = SousChapitre.objects.get(id=reponse_data['sous_chapitre_id'])
                reponse = reponse_data['reponse']
                if not reponse :
                    reponse = 0
                
                if ReponseSousChapitre.objects.filter(sous_chapitre=sous_chapitre_obj).exists():
                    ReponseSousChapitre.objects.filter(sous_chapitre=sous_chapitre_obj).delete()
                ReponseSousChapitre.objects.create(
                    sous_chapitre=sous_chapitre_obj,
                    point=reponse
                )
            return Response({"message": "Reponses saved successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('Error saving reponses:', e)
            return Response({"message": "Error saving reponses"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChapitreStatsActuelDetail(APIView):
    def get(self, request):
        chapitre_detail = []
        chapitres = Chapitre.objects.all()
        for chapitre in chapitres:
            sous_chapitres = SousChapitre.objects.filter(chapitre=chapitre)
            num_sous_chap = [sous_chapitre.numero for sous_chapitre in sous_chapitres]
            note_sous_chap = [ReponseSousChapitre.objects.filter(sous_chapitre=sous_chapitre).last().point for sous_chapitre in sous_chapitres]
            chapitre_detail.append({
                'nom':chapitre.nom,
                'num_sous_chap':num_sous_chap,
                'note_sous_chap':note_sous_chap,
            })
           

        return Response(chapitre_detail)