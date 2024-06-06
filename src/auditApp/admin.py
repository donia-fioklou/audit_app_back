from django.contrib import admin

from auditApp.models.Utilisateur import User
from auditApp.models.Annexe import Annexe
from auditApp.models.Chapitre import Chapitre
from auditApp.models.SousChapitre import SousChapitre
# Register your models here.
admin.site.register(User)
admin.site.site_header = "Audit"
admin.site.site_title = "Audit"
admin.site.index_title = "Audit"
#admin.site.site_url = "/audit/"
admin.site.register(Annexe)
admin.site.register(Chapitre)
admin.site.register(SousChapitre)

