from django.shortcuts import render
from django.views.generic.list import ListView
from college.models import Notice,Profile,Branch,Question
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.edit import UpdateView,CreateView
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from rest_framework import viewsets
# from college.serializer import BranchSerializer,NoticeSerializer

@method_decorator(login_required,name="dispatch") 
class NoticeListview(ListView):
    model = Notice
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        if self.request.user.is_superuser:
            return Notice.objects.filter(Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")
        else:
            return Notice.objects.filter(Q(branch = self.request.user.profile.branch) | Q(branch__isnull=True)).filter(Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")


@method_decorator(login_required,name="dispatch")  
class Noticedetailview(DetailView):
    model = Notice    


@method_decorator(login_required,name="dispatch")  
class ProfileUpdateview(UpdateView):
    model = Profile
    fields =["branch","sem","mark_10","mark_11","mark_12","mark_aggr","roll_no","phone_no","my_img","my_resume","skills"]
    
    
@method_decorator(login_required,name="dispatch")  
class QuestionCreateview(CreateView):
    model = Question
    fields =["subject","question"]
    
    def form_valid(self,form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())        
    
    
@method_decorator(login_required,name="dispatch")
class Mylist(TemplateView):
    template_name = "college/mylist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notices"] = Notice.objects.order_by("-id")
        context["question"] = Question.objects.order_by("-id")
        return context
    
    
# class BranchViewSet(viewsets.ModelViewSet):
#     queryset = Branch.objects.all()
#     serializer_class = BranchSerializer
    
# class NoticeViewSet(viewsets.ModelViewSet):
#     queryset = Notice.objects.all()
#     serializer_class = NoticeSerializer