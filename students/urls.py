# Import the necessary modules
from django.urls import path
from . import views


# Define URL patterns for the student management app
urlpatterns = [
    path('', views.student_list, name='student_list'),  # URL pattern for listing all students. Maps to the student_list view function
    path('create/', views.create_student, name='create_student'),  # URL pattern for creating a new student record. Maps to the create_student view function
    path('<int:student_id>/update/', views.update_student, name='update_student'),  # URL pattern for updating a specific student record. Uses a student_id parameter to identify the student. Maps to the update_student view function
    path('<int:student_id>/delete/', views.delete_student, name='delete_student'),    # URL pattern for deleting a specific student record. Uses a student_id parameter to identify the student. Maps to the delete_student view function
]
