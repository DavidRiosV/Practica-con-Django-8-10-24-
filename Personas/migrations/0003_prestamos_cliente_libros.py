# Generated by Django 5.1.1 on 2024-10-08 09:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0002_libro_autores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateTimeField(default=django.utils.timezone.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personas.cliente')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Personas.libro')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='libros',
            field=models.ManyToManyField(through='Personas.Prestamos', to='Personas.libro'),
        ),
    ]
