from django.shortcuts import render
from django.shortcuts import redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.


def home(request):
    form = EmployeeForm()
    template_name = 'app1/index.html'

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():

            form.save()
        form = EmployeeForm()
    

    data = Employee.objects.all()

    context = {
        'form': form,
        'data': data,
    }

    return render(request, template_name, context)


def delete_record(request, id):
    a = Employee.objects.get(pk=id)
    a.delete()
    return redirect('/')


# update view
def update_record(request, id):
    if request.method == 'POST':
        data = Employee.objects.get(pk=id)
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:

        data = Employee.objects.get(pk=id)
        form = EmployeeForm(instance=data)

    context = {
        'form': form,
        
    }

    return render(request, 'app1/update.html', context)
