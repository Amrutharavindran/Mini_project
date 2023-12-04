# Generated by Django 3.2.21 on 2023-11-09 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('Post', models.CharField(max_length=100)),
                ('Pin', models.BigIntegerField()),
                ('Phone', models.BigIntegerField()),
                ('Email', models.CharField(max_length=100)),
                ('Dob', models.CharField(max_length=100)),
                ('Photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Assign_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Status', models.CharField(max_length=100)),
                ('AGENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.agent_table')),
            ],
        ),
        migrations.CreateModel(
            name='Claim_request_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reason', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('Documents', models.FileField(upload_to='')),
                ('ASSIGN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.assign_table')),
            ],
        ),
        migrations.CreateModel(
            name='login_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Policy_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Policyname', models.CharField(max_length=100)),
                ('Policydetails', models.CharField(max_length=500)),
                ('Date', models.DateField()),
                ('type', models.CharField(max_length=60)),
                ('premium', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Request_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Status', models.CharField(max_length=100)),
                ('POLICY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.policy_table')),
            ],
        ),
        migrations.CreateModel(
            name='vehicle_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=100)),
                ('vehicle_no', models.CharField(max_length=100)),
                ('rcbook', models.FileField(upload_to='')),
                ('REQUEST', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.request_table')),
            ],
        ),
        migrations.CreateModel(
            name='User_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('Post', models.CharField(max_length=100)),
                ('Dob', models.DateField()),
                ('Phone', models.BigIntegerField()),
                ('Pin', models.BigIntegerField()),
                ('Email', models.CharField(max_length=100)),
                ('Photo', models.FileField(upload_to='')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.login_table')),
            ],
        ),
        migrations.AddField(
            model_name='request_table',
            name='USERID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.user_table'),
        ),
        migrations.CreateModel(
            name='Policy_details_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('Type', models.CharField(max_length=100)),
                ('Dependents_count', models.IntegerField()),
                ('Dependents_agelimit', models.CharField(max_length=100)),
                ('POLICY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.policy_table')),
            ],
        ),
        migrations.CreateModel(
            name='payment_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Amount', models.BigIntegerField()),
                ('POLICY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.policy_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.CharField(max_length=200)),
                ('Date', models.DateField()),
                ('Rating', models.CharField(max_length=200)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='family_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('id_proof', models.FileField(upload_to='')),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=100)),
                ('REQUEST', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.request_table')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complaint', models.CharField(max_length=200)),
                ('Reply', models.CharField(max_length=200)),
                ('Date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.user_table')),
            ],
        ),
        migrations.CreateModel(
            name='Claim_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('claimamount', models.BigIntegerField()),
                ('Photo', models.FileField(upload_to='')),
                ('CLAIM_REQ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.claim_request_table')),
            ],
        ),
        migrations.CreateModel(
            name='Chat_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=200)),
                ('Date', models.DateField()),
                ('FromID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FromID', to='sapp.login_table')),
                ('ToID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ToID', to='sapp.login_table')),
            ],
        ),
        migrations.AddField(
            model_name='assign_table',
            name='REQUEST',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.request_table'),
        ),
        migrations.AddField(
            model_name='agent_table',
            name='LOGIN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sapp.login_table'),
        ),
    ]
