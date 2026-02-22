from django.db import models

# Create your models here.
class Etudiant(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    num_matricule = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Enseignement(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    classe = models.ForeignKey('Annee', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} ({self.code})"


class Annee(models.Model):
    id = models.AutoField(primary_key=True)
    annee_scolaire = models.CharField(max_length=20, unique=True)
    filieres = models.CharField(max_length=150)

    def __str__(self):
        return self.annee_scolaire


class Semestre(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    annee = models.ForeignKey(Annee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} - {self.annee}"


class Evaluation(models.Model):
    id = models.BigAutoField(primary_key=True)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    enseignement = models.ForeignKey(Enseignement, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    note = models.FloatField()

    class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=['etudiant', 'enseignement', 'semestre'],
                    name='unique_evaluation'
                )
            ]


    def __str__(self):
        return f"{self.etudiant} - {self.enseignement} - {self.note}"
