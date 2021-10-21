from django.contrib import admin

from .models import Authors, Authorsofbooks, Books, Genres, Instance, Provider, Publishinghome, Readerticket, Readers

#admin.site.register(Authors) #отображение элементов в виде объектов

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
	list_display = ("idauthorsofbooks", "fullname") 
	list_filter = ("idauthorsofbooks", "fullname") 
	search_fields = ["fullname"]


@admin.register(Authorsofbooks)
class AuthorsfbooksAdmin(admin.ModelAdmin):
	list_display = ("idauthorsofbooks", "books_idbooks", "authors_idauthorsofbooks")
	list_filter = ("idauthorsofbooks", "books_idbooks", "authors_idauthorsofbooks") #filter
	search_fields = ["idauthorsofbooks", "books_idbooks", "authors_idauthorsofbooks"]

#admin.site.register(Books) #отображение элементов в виде объектов
@admin.register(Books)
class Books(admin.ModelAdmin):
	list_display = ("idbooks", "name", "god_izdaniya", "genres_idgenres", "publishinghome_idpublishinghome")
	list_filter = ("idbooks", "name", "genres_idgenres")
	search_fields = ["idbooks", "name", "genres_idgenres"]


#admin.site.register(Genres) #отображение элементов в виде объектов

@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
	list_display = ("idgenres", "name")
	list_filter = ("idgenres", "name") #filter
	search_fields = ["idbooks", "name", "god_izdaniya", "genres_idgenres", "publishinghome_idpublishinghome"]


#admin.site.register(Instance) #отображение элементов в виде объектов

@admin.register(Instance)
class Instance(admin.ModelAdmin):
	list_display = ("idinstance", "dateofreceipt", "provider_idprovider", "books_idbooks")
	list_filter = ("idinstance", "dateofreceipt", "provider_idprovider", "books_idbooks") #filter
	search_fields = ["idinstance", "dateofreceipt", "provider_idprovider", "books_idbooks"]



#admin.site.register(Provider) #отображение элементов в виде объектов

@admin.register(Provider)
class Provider(admin.ModelAdmin):
	list_display = ("idprovider", "name")
	list_filter = ("idprovider", "name") #filter
	search_fields = ["idprovider", "name"]




#admin.site.register(Publishinghome) #отображение элементов в виде объектов

@admin.register(Publishinghome)
class PublishinghomeAdmin(admin.ModelAdmin):
	list_display = ("idpublishinghome", "name")
	list_filter = ("idpublishinghome", "name") #filter
	search_fields = ["idpublishinghome", "name"]

 
#admin.site.register(Readerticket) #отображение элементов в виде объектов

@admin.register(Readerticket)
class ReaderticketAdmin(admin.ModelAdmin):
	list_display = ("idreaderticket", "dateofissue", "extensionperiod", "returnofbooks", "readers_idreaders", "instance_idinstance")
	list_filter = ("idreaderticket", "dateofissue", "extensionperiod", "returnofbooks", "readers_idreaders", "instance_idinstance") #filter
	search_fields = ["idreaderticket", "dateofissue", "extensionperiod", "returnofbooks", "readers_idreaders", "instance_idinstance"]



#admin.site.register(Readers) #отображение элементов в виде объектов

@admin.register(Readers)
class ReadersAdmin(admin.ModelAdmin):
	list_display = ("idreaders", "fullname", "passport", "dob", "street", "home", "apartmentnumber", "phonenumber")
	list_filter = ("idreaders", "fullname", "phonenumber") #filter
	search_fields = ["idreaders", "fullname", "passport", "phonenumber"]





