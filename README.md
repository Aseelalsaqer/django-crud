## Overview :
adding CRUD functionality : by building a Django project that allows Creating, Reading, Updating and Deleting.


PR link : https://github.com/Aseelalsaqer/django-crud/pull/1


## Feature Tasks and Requirements:
- [x] Create snacks_crud_project Django project
- [x] Create snacks app
- [x] Create Snack model : 
   - [x] title field
   - [x] purchaser field
   - [x] description field
   - [x] Register model with admin
- [x] Create SnackListView that extends appropriate generic view
   - [x] associated url path is an empty string
- [x] Create SnackDetailView that extends appropriate generic view
  - [x] associated url path is <int:pk>/
- [x] Create SnackCreateView that extends appropriate generic view
  - [x] associated url path is create/
- [x] Create SnackUpdateView that extends appropriate generic view
  - [x] associated url path is <int:pk>/update/
- [x] Create SnackDeleteView that extends appropriate generic view
  - [x] associated url path is <int:pk>/delete/
- [x] Add urls to support all views, with appropriate names
- [x] Add templates to support all views
- [x] Add navigation links in appropriate locations to access all pages
- [x] Make all necessary changes to project level files for project to run
