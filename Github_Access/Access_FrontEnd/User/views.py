from django.shortcuts import render
from django.views.generic import TemplateView
from github import Github
from .forms import UserForm

class userView(TemplateView):
    template_name = 'User/userView.html'
    form_class = UserForm

    def get(self, request):
        context = {
            'form' : self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid:
            print(form.data['usersName'])

        return render(request, self.template_name)

