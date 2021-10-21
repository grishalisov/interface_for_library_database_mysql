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

    
    def __str__(self):
        return f"{self.idauthorsofbooks}, {self.fullname}"


    class Meta:
        managed = False
        db_table = 'Authors'


class Authorsofbooks(models.Model):
    idauthorsofbooks = models.AutoField(db_column='idAuthorsOfBooks', primary_key=True)  # Field name made lowercase.
    books_idbooks = models.ForeignKey('Books', models.DO_NOTHING, db_column='Books_idBooks')  # Field name made lowercase.
    authors_idauthorsofbooks = models.ForeignKey(Authors, models.DO_NOTHING, db_column='Authors_idAuthorsOfBooks')  # Field name made lowercase.
    
    def __str__(self):
        return f"{self.idauthorsofbooks}, {books_idbooks}, {authors_idauthorsofbooks}"



    class Meta:
        managed = False
        db_table = 'AuthorsOfBooks'


class Books(models.Model):
    idbooks = models.AutoField(db_column='idBooks', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    god_izdaniya = models.CharField(db_column='God_izdaniya', max_length=4)  # Field name made lowercase.
    genres_idgenres = models.ForeignKey('Genres', models.DO_NOTHING, db_column='Genres_idGenres')  # Field name made lowercase.
    publishinghome_idpublishinghome = models.ForeignKey('Publishinghome', models.DO_NOTHING, db_column='PublishingHome_idPublishingHome')  # Field name made lowercase.

    def __str__(self):
        return f"{self.idbooks}, {self.name}, {self.god_izdaniya}, {self.genres_idgenres}, {self.publishinghome_idpublishinghome}"


    class Meta:
        managed = False
        db_table = 'Books'


class Genres(models.Model):
    idgenres = models.AutoField(db_column='idGenres', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return f"{self.idgenres}, {self.name}"


    class Meta:
        managed = False
        db_table = 'Genres'


class Instance(models.Model):
    idinstance = models.AutoField(db_column='idInstance', primary_key=True)  # Field name made lowercase.
    dateofreceipt = models.DateField(db_column='DateOfReceipt')  # Field name made lowercase.
    provider_idprovider = models.ForeignKey('Provider', models.DO_NOTHING, db_column='Provider_idProvider')  # Field name made lowercase.
    books_idbooks = models.ForeignKey(Books, models.DO_NOTHING, db_column='Books_idBooks')  # Field name made lowercase.

    def __str__(self):
        return f"{self.idinstance}, {self.dateofreceipt}, {self.provider_idprovider}, {self.books_idbooks}"


    class Meta:
        managed = False
        db_table = 'Instance'


class Provider(models.Model):
    idprovider = models.IntegerField(db_column='idProvider', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return f"{self.idprovider}, {self.name}"


    class Meta:
        managed = False
        db_table = 'Provider'


class Publishinghome(models.Model):
    idpublishinghome = models.AutoField(db_column='idPublishingHome', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return f"{self.idpublishinghome}, {self.name}"


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

    def __str__(self):
        return f"{self.idreaderticket}, {self.dateofissue}, {self.extensionperiod}, {self.returnofbooks}, {self.readers_idreaders}, {self.instance_idinstance}"


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

    def __str__(self):
        return f"{self.idreaders}, {self.fullname}, {self.passport}, {self.dob}, {self.street}, {self.home}, {self.apartmentnumber}, {self.phonenumber}"


    class Meta:
        managed = False
        db_table = 'Readers'
