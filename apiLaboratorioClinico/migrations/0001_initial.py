# Generated by Django 4.2.3 on 2023-08-03 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='analisis',
            fields=[
                ('analisis_id', models.AutoField(primary_key=True, serialize=False)),
                ('analisis_nombre', models.CharField(max_length=50)),
                ('analisis_fregistro', models.DateTimeField(auto_now_add=True)),
                ('analisis_estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='especialidad',
            fields=[
                ('especialidad_id', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad_nombre', models.CharField(max_length=50)),
                ('especialidad_fregistro', models.DateTimeField(auto_now_add=True)),
                ('especialidad_estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='examen',
            fields=[
                ('examen_id', models.AutoField(primary_key=True, serialize=False)),
                ('examen_nombre', models.CharField(max_length=50)),
                ('examen_fregistro', models.DateTimeField(auto_now_add=True)),
                ('examen_estado', models.BooleanField(default=True)),
                ('analisis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.analisis')),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('paciente_id', models.AutoField(primary_key=True, serialize=False)),
                ('paciente_nombre', models.CharField(max_length=100)),
                ('paciente_apepat', models.CharField(max_length=100)),
                ('paciente_apemat', models.CharField(max_length=100)),
                ('paciente_ine', models.CharField(max_length=18)),
                ('paciente_telefono', models.CharField(max_length=8)),
                ('paciente_edad', models.IntegerField()),
                ('paciente_sangre', models.CharField(max_length=2)),
                ('paciente_sexo', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='realizar_examen',
            fields=[
                ('realizar_examen_id', models.AutoField(primary_key=True, serialize=False)),
                ('realizar_examen_fecha', models.DateTimeField()),
                ('realizar_examen_estado', models.BooleanField(default=True)),
                ('realizar_examen_indica', models.CharField(max_length=255)),
                ('realizar_examen_noindica', models.CharField(max_length=255)),
                ('paciente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='realizar_examen_detalle',
            fields=[
                ('rdetalle_id', models.AutoField(primary_key=True, serialize=False)),
                ('analisis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.analisis')),
                ('examen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.examen')),
                ('realizar_examen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.realizar_examen')),
            ],
        ),
        migrations.CreateModel(
            name='resultado',
            fields=[
                ('resultado_id', models.AutoField(primary_key=True, serialize=False)),
                ('resultado_fregistro', models.DateTimeField(auto_now_add=True)),
                ('resultado_estado', models.BooleanField(default=True)),
                ('paciente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_nombre', models.CharField(max_length=20)),
                ('rol_fregistro', models.DateTimeField(auto_now_add=True)),
                ('rol_estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_nombre', models.CharField(max_length=20)),
                ('usuario_contrasenia', models.CharField(max_length=20)),
                ('usuario_email', models.CharField(max_length=255)),
                ('usuario_foto', models.CharField(max_length=255)),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.rol')),
            ],
        ),
        migrations.CreateModel(
            name='resultado_detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado_detalle_archivo', models.CharField(max_length=255)),
                ('analisis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.analisis')),
                ('rdetalle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.realizar_examen_detalle')),
                ('resultado_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.resultado')),
            ],
        ),
        migrations.AddField(
            model_name='resultado',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.usuario'),
        ),
        migrations.AddField(
            model_name='realizar_examen',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.usuario'),
        ),
        migrations.CreateModel(
            name='medico',
            fields=[
                ('medico_id', models.AutoField(primary_key=True, serialize=False)),
                ('medico_nombre', models.CharField(max_length=50)),
                ('medico_apepat', models.CharField(max_length=50)),
                ('medico_apemat', models.CharField(max_length=50)),
                ('medico_direreccion', models.CharField(max_length=50)),
                ('medico_telefono', models.CharField(max_length=8)),
                ('meduco_fecha_nacimiento', models.DateTimeField()),
                ('medico_nrocolegiatura', models.CharField(max_length=8)),
                ('medico_nrodocumento', models.CharField(max_length=8)),
                ('especialidad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.especialidad')),
                ('usario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiLaboratorioClinico.usuario')),
            ],
        ),
    ]
