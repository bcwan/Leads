from django.shortcuts import render

# Create your views here.
def index(request):
  # load index.html
  return render(request, 'frontend/index.html')