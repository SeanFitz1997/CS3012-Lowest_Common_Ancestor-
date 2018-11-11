from django.shortcuts import render
from django.views.generic import TemplateView

class userView(TemplateView):

    def get(self, request):
        return render(request, 'User/userView.html')
