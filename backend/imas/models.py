from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutoAnswerTask(models.Model):
    user_id = models.IntegerField()
    train_model_id = models.IntegerField()
    status = models.IntegerField()
    question = models.CharField(max_length=1024)
    picture_path = models.CharField(max_length=128, blank=True, null=True)
    answer = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_answer_task'


class Dataset(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=512)
    data_format = models.CharField(max_length=20)
    is_labeled = models.IntegerField()
    is_single_case = models.IntegerField()
    with_picture = models.IntegerField()
    status = models.IntegerField()
    dataset_path = models.CharField(max_length=128, blank=True, null=True)
    after_train_dataset_path = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataset'


class DeepLearningModel(models.Model):
    name = models.CharField(max_length=20)
    category_id = models.IntegerField()
    introduction = models.CharField(max_length=1024, blank=True, null=True)
    article_title = models.CharField(max_length=50, blank=True, null=True)
    article_url = models.CharField(max_length=128, blank=True, null=True)
    code_url = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deep_learning_model'


class Department(models.Model):
    department = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class KnowledgeGraph(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    disease_case_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'knowledge_graph'


class ModelCategory(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'model_category'


class Question(models.Model):
    user_id = models.IntegerField()
    department_id = models.IntegerField()
    content = models.CharField(max_length=1024)
    picture_path = models.CharField(max_length=128, blank=True, null=True)
    answer = models.CharField(max_length=1024, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'question'


class SimilarCase(models.Model):
    knowledge_graph_id = models.IntegerField()
    similar_graph_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'similar_case'


class SingleDiseaseCaseInfo(models.Model):
    user_id = models.IntegerField()
    dataset_id = models.IntegerField()
    picture_path = models.CharField(max_length=128, blank=True, null=True)
    disease = models.CharField(max_length=128, blank=True, null=True)
    medicine = models.CharField(max_length=128, blank=True, null=True)
    diagnosis = models.CharField(max_length=128, blank=True, null=True)
    symptom = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'single_disease_case_info'


class TrainModelTask(models.Model):
    user_id = models.IntegerField()
    task_name = models.CharField(max_length=50)
    dataset_id = models.IntegerField()
    model_id = models.IntegerField()
    epoch = models.IntegerField(blank=True, null=True)
    batch_size = models.IntegerField(blank=True, null=True)
    rnn_cell = models.CharField(max_length=20, blank=True, null=True)
    embedding = models.CharField(max_length=20, blank=True, null=True)
    constructor = models.CharField(max_length=20, blank=True, null=True)
    train_set_proportion = models.IntegerField()
    test_set_proportion = models.IntegerField()
    valid_set_proportion = models.IntegerField()
    status = models.IntegerField()
    after_train_model_path = models.CharField(max_length=128, blank=True, null=True)
    f1 = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    recall = models.IntegerField(blank=True, null=True)
    precision = models.IntegerField(blank=True, null=True)
    bleu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_model_task'


class UserInfo(models.Model):
    login_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.IntegerField()
    age = models.IntegerField()
    name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    marriage = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'
