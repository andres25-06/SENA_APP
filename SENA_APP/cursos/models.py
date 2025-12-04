from django.db import models

# Create your models here.

class Curso(models.Model):
    ESTADO_CHOICES = [
        ('PRO', 'Programado'),
        ('INI', 'Iniciado'),
        ('EJE', 'En Ejecución'),
        ('FIN', 'Finalizado'),
        ('CAN', 'Cancelado'),
        ('SUS', 'Suspendido'),
    ]

    code = models.CharField(max_length=30, unique=True, verbose_name="Código del Curso")
    name = models.CharField(max_length=200, verbose_name="Nombre del Curso")
    program = models.ForeignKey('programas.Programa', on_delete=models.CASCADE, verbose_name="Programa de Formación")
    instructor_coordinator = models.ForeignKey('instructores.instructores', on_delete=models.CASCADE, related_name='cursos_coordinados', verbose_name="Instructor Coordinador")
    instructors = models.ManyToManyField('instructores.instructores', through='InstructorCurso', related_name='cursos_impartidos', verbose_name="Instructores")
    aprendices = models.ManyToManyField('aprendices.aprendices', through='AprendizCurso', related_name='cursos', verbose_name="Aprendices")
    start_date = models.DateField(verbose_name="Fecha de Inicio")
    end_date = models.DateField(verbose_name="Fecha de Finalización")
    schedule = models.CharField(max_length=100, verbose_name="Horario")
    classroom = models.CharField(max_length=50, verbose_name="Aula/Ambiente")
    max_capacity = models.PositiveIntegerField(verbose_name="Cupos Máximos")
    state = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='PRO', verbose_name="Estado del Curso")
    observations = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.code} - {self.name}"

    def cupos_disponibles(self):
        return self.max_capacity - self.aprendices.count()

    def porcentaje_ocupacion(self):
        if self.max_capacity > 0:
            return (self.aprendices.count() / self.max_capacity) * 100
        return 0


class InstructorCurso(models.Model):
    teacher = models.ForeignKey('instructores.Instructores', on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, verbose_name="Rol en el Curso")
    assignment_date = models.DateField(auto_now_add=True, verbose_name="Fecha de Asignación")

    class Meta:
        verbose_name = "Instructor por Curso"
        verbose_name_plural = "Instructores por Curso"
        unique_together = ['teacher', 'course']

    def __str__(self):
        return f"{self.teacher} - {self.course} ({self.role})"


class AprendizCurso(models.Model):
    ESTADO_CHOICES = [
        ('INS', 'Inscrito'),
        ('ACT', 'Activo'),
        ('DES', 'Desertor'),
        ('GRA', 'Graduado'),
        ('SUS', 'Suspendido'),
    ]

    student = models.ForeignKey('aprendices.aprendices', on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    inscription_date = models.DateField(auto_now_add=True, verbose_name="Fecha de Inscripción")
    state = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='INS', verbose_name="Estado en el Curso")
    final_grade = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True, verbose_name="Nota Final")
    observations = models.TextField(blank=True, null=True, verbose_name="Observaciones")

    class Meta:
        verbose_name = "Aprendiz por Curso"
        verbose_name_plural = "Aprendices por Curso"
        unique_together = ['student', 'course']

    def __str__(self):
        return f"{self.student} - {self.course} ({self.state})"