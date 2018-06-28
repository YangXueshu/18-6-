from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import ListView,View,CreateView,UpdateView,DeleteView
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.urls import reverse,reverse_lazy
from django.shortcuts import render, redirect
from .models import Students,S_CURRICULUM,Sign
from django.contrib import messages
from .begin import detection
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from urllib.parse import unquote
from PIL import Image
import base64
import datetime
# Create your views here.



def home(request):
    return render(request, 'homepage.html')




def studentDetail(request, id):
    Student = Students.objects.get(id=id)
    template = get_template('detail.html')
    context = {'Students': Student}

    return HttpResponse(template.render(context, request))

# class StudentList(ListView):
#     model = Students
#     template_name = 'list.html'
def studentTest(request, id):
    Student = Students.objects.get(id=id)
    template = get_template('test.html')
    context = {'Students': Student}
    context['left_x'],context['left_y'],context['bottom_x'],context['bottom_y']=detection('/home/lenovo/darkflow/detection'+Student.s_photo.url)
    return HttpResponse(template.render(context, request))


@csrf_exempt
def pred(request):
    i = 0
    if request.POST:
        img = open('./school/static/pi.png', 'wb')
        img.write(base64.b64decode(request.POST['img'][22:]))
        img.close()
    if request.method == 'GET':
        w = detection('/home/lenovo/darkflow/detection/school/static/pi.png')
        students = Students.objects.all()
        for s in students:
            a = s.s_photo.url.split('/')
            b = a[-1].split('.')
            if unquote(b[0], encoding="utf-8") == str(w):
                person = Sign.objects.create(name=s.name,time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return render(request, 'pred.html',{'img':'/static/pi.png','name':w})


class StudentList(ListView):
    model = Students
    template_name = 'list.html'

    def get_queryset(self):
        name = self.request.GET.get('name')
        queryset = super(StudentList, self).get_queryset()
        if name:
            queryset = Students.objects.filter(name__icontains=name)
        return queryset

class Index(View):

    def get(self, request):
        return render(request, 'backstage/index.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user or user.is_superuser:
            login(request, user)
            return redirect(reverse('student_list'))
        messages.error(request, 'username or password is incorrect！')
        return redirect(reverse('index'))

class CreateProject(CreateView):
    model = S_CURRICULUM
    template_name = 'backstage/create_project.html'
    fields = ['name', 'week_day', 'time_begin', 'time_end']
    def get_success_url(self):
        messages.success(self.request, 'Create Success!')
        return resolve_url('create_project')

class CreateStudent(CreateView):
    model = Students
    template_name = 'backstage/create_student.html'
    fields = ['name', 's_class', 's_id', 's_grade','s_photo','s_curriculum']

    def get_success_url(self):
        messages.success(self.request, 'Create Success!')
        return resolve_url('create_student')

class UpdateStudent(UpdateView):
    model = Students
    template_name = 'backstage/create_student.html'
    fields = ['name', 's_class', 's_id', 's_grade','s_photo','s_curriculum']
    def get_success_url(self):
        messages.success(self.request, 'Create Success!')
        return resolve_url('update_student', pk=self.kwargs['pk'])
class UpdateProject(UpdateView):
    model = S_CURRICULUM
    template_name = 'backstage/create_project.html'
    fields = ['name', 'week_day', 'time_begin', 'time_end']
    def get_success_url(self):
        messages.success(self.request, 'Create Success!')
        return resolve_url('update_project', pk=self.kwargs['pk'])

class DeleteStudent(DeleteView):
    model = Students
    template_name = 'backstage/delete_student.html'
    success_url = reverse_lazy('student_list')

class DeleteProject(DeleteView):
    model = S_CURRICULUM
    template_name = 'backstage/delete_student.html'
    success_url = reverse_lazy('student_list')