from django.contrib import admin
from .models import Etudiant, Enseignement, Annee, Semestre, Evaluation

# Register your models here.
@admin.register(Etudiant)

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'num_matricule')
    search_fields = ('nom', 'prenom', 'num_matricule')


@admin.register(Enseignement)

class EnseignementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code', 'classe')
    search_fields = ('nom', 'code')
    list_filter = ('classe',)


@admin.register(Annee)

class AnneeAdmin(admin.ModelAdmin):
    list_display = ('annee_scolaire', 'filieres')
    search_fields = ('annee_scolaire',)


@admin.register(Semestre)

class SemestreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee')
    list_filter = ('annee',)


@admin.register(Evaluation)

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'enseignement', 'semestre', 'note')
    list_filter = ('semestre', 'enseignement')
    search_fields = ('etudiant__nom', 'enseignement__nom')
    list_select_related = ('etudiant', 'enseignement', 'semestre')
    ordering = ('-note',)



