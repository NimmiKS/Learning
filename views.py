from django.shortcuts import render
from django.views import View
from .models import Student, Teacher, Staff
from django.http import HttpResponse
import csv

class BlockArrayView(View):
    def get(self, request, *args, **kwargs):
        table = request.GET.get('table', 'students')
        if table == 'students':
            data = Student.objects.all().values()
            heading = "Student Details"
        elif table == 'teachers':
            data = Teacher.objects.all().values()
            heading = "Teacher Details"
        elif table == 'staff':
            data = Staff.objects.all().values()
            heading = "Staff Details"
        else:
            data = []
            heading = "No Data Found"
        field_names = data[0].keys() if data else []

        return render(request, 'dashboard.html', {
            'data': data,
            'heading': heading,
            'field_names': field_names
        })
        # context = {
        #     'students': Student.objects.all(),
        #     'teachers': Teacher.objects.all(),
        #     'staff': Staff.objects.all(),
        # }
        # return render(request, 'dashboard.html', context)

class ExportCSVView(View):
    def get(self, request, *args, **kwargs):
        table = request.GET.get('table')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{table}_data.csv"'

        writer = csv.writer(response)

        if table == 'students':
            writer.writerow(['Name', 'Roll Number', 'Department', 'Age'])
            for s in Student.objects.all():
                writer.writerow([s.name, s.roll_number, s.department, s.age])

        elif table == 'teachers':
            writer.writerow(['Name', 'Subject', 'Email'])
            for t in Teacher.objects.all():
                writer.writerow([t.name, t.subject, t.email])

        elif table == 'staff':
            writer.writerow(['Name', 'Position', 'Contact Number'])
            for st in Staff.objects.all():
                writer.writerow([st.name, st.position, st.contact_number])

        else:
            return HttpResponse("Invalid table name.", status=400)

        return response