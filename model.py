# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    idauthorsofbooks = models.AutoField(db_column='idAuthorsOfBooks', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Authors'


class Authorsofbooks(models.Model):
    idauthorsofbooks = models.AutoField(db_column='idAuthorsOfBooks', primary_key=True)  # Field name made lowercase.
    books_idbooks = models.ForeignKey('Books', models.DO_NOTHING, db_column='Books_idBooks')  # Field name made lowercase.
    authors_idauthorsofbooks = models.ForeignKey(Authors, models.DO_NOTHING, db_column='Authors_idAuthorsOfBooks')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuthorsOfBooks'


class Books(models.Model):
    idbooks = models.AutoField(db_column='idBooks', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    god_izdaniya = models.CharField(db_column='God_izdaniya', max_length=4)  # Field name made lowercase.
    genres_idgenres = models.ForeignKey('Genres', models.DO_NOTHING, db_column='Genres_idGenres')  # Field name made lowercase.
    publishinghome_idpublishinghome = models.ForeignKey('Publishinghome', models.DO_NOTHING, db_column='PublishingHome_idPublishingHome')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Books'


class Genres(models.Model):
    idgenres = models.AutoField(db_column='idGenres', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genres'


class Instance(models.Model):
    idinstance = models.AutoField(db_column='idInstance', primary_key=True)  # Field name made lowercase.
    dateofreceipt = models.DateField(db_column='DateOfReceipt')  # Field name made lowercase.
    provider_idprovider = models.ForeignKey('Provider', models.DO_NOTHING, db_column='Provider_idProvider')  # Field name made lowercase.
    books_idbooks = models.ForeignKey(Books, models.DO_NOTHING, db_column='Books_idBooks')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Instance'


class Provider(models.Model):
    idprovider = models.IntegerField(db_column='idProvider', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Provider'


class Publishinghome(models.Model):
    idpublishinghome = models.AutoField(db_column='idPublishingHome', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PublishingHome'


class Readerticket(models.Model):
    idreaderticket = models.AutoField(db_column='idReaderTicket', primary_key=True)  # Field name made lowercase.
    dateofissue = models.DateField(db_column='DateOfIssue')  # Field name made lowercase.
    extensionperiod = models.DateField(db_column='ExtensionPeriod')  # Field name made lowercase.
    returnofbooks = models.CharField(db_column='ReturnOfBooks', max_length=45)  # Field name made lowercase.
    readers_idreaders = models.ForeignKey('Readers', models.DO_NOTHING, db_column='Readers_idReaders')  # Field name made lowercase.
    instance_idinstance = models.ForeignKey(Instance, models.DO_NOTHING, db_column='Instance_idInstance')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReaderTicket'


class Readers(models.Model):
    idreaders = models.AutoField(db_column='idReaders', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=100)  # Field name made lowercase.
    passport = models.CharField(db_column='Passport', max_length=12)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=45)  # Field name made lowercase.
    home = models.CharField(db_column='Home', max_length=3)  # Field name made lowercase.
    apartmentnumber = models.CharField(db_column='ApartmentNumber', max_length=4)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Readers'


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
