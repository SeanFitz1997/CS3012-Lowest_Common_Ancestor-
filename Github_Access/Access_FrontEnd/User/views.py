from django.shortcuts import render

def testView(reqest):
    return render(reqest, 'User/userView.html')
