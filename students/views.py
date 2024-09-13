# Import necessary modules and functions
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import is_ajax


# View function to list all students. Requires user to be logged in.
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


# View function to create a new student record. Requires user to be logged in.
@login_required
def create_student(request):
    if request.method == 'POST' and is_ajax(request): # Check if the request method is POST and the request is an AJAX request
        # Retrieve student data from the POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        enrollment_date = request.POST.get('enrollment_date')

        # Create a new student record in the database
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            enrollment_date=enrollment_date
        )
        # Return a JSON response with the newly created student's details
        return JsonResponse({'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name})

    # Render the create_student.html template for non-AJAX or GET requests
    return render(request, 'create_student.html')


# View function to update an existing student record. Requires user to be logged in.
@login_required
def update_student(request, student_id):
    # Retrieve the student record or return a 404 error if not found
    student = get_object_or_404(Student, id=student_id)
    # Format the enrollment date for the template
    student.enrollment_date = student.enrollment_date.strftime('%Y-%m-%d')

    # Check if the request method is POST and the request is an AJAX request
    if request.method == 'POST' and is_ajax(request):
        # Update the student record with new data from the POST request
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.enrollment_date = request.POST.get('enrollment_date')
        student.save()

        # Return a JSON response with the updated student's details
        return JsonResponse({'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name})
    # Render the update_student.html template with the student data for non-AJAX or GET requests
    return render(request, 'update_student.html', {'student': student})


# View function to delete a student record. CSRF protection is disabled for this view.
@csrf_exempt
def delete_student(request, student_id):
    # Retrieve the student record or return a 404 error if not found
    student = get_object_or_404(Student, id=student_id)
    student.delete()                      # Delete the student record from the database
    return JsonResponse({'deleted': True})   # Return a JSON response indicating the record was deleted
