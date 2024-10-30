from django.db import models
from eventex.subscriptions.validators import validate_cpf


class Registration(models.Model):
    student = models.ForeignKey('subscriptions.Subscription', verbose_name='Aluno', on_delete=models.PROTECT)
    cpf = models.CharField('CPF', max_length=14, validators=[validate_cpf])
    phone = models.CharField('Telefone', max_length=20, blank=True)
    talk = models.ForeignKey(
        'core.Talk', verbose_name='Nome da Palestra', null=True, blank=True,
        on_delete=models.PROTECT, related_name='registrations_as_talks')
    course = models.ForeignKey(
        'core.Course', verbose_name='Nome do Curso', null=True, blank=True,
        on_delete=models.PROTECT, related_name='registrations_as_courses')
    name_speaker = models.CharField('Nome do Palestrante', max_length=255, null=True, blank=True)
    start_time = models.TimeField('Horário de Início', null=True, blank=True)
    observation = models.CharField('Observação', max_length=2500, blank=True)

    class Meta:
        verbose_name_plural = "Participantes"
        verbose_name = "Participante"

    def __str__(self):
        return self.student.name
