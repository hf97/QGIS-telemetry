from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, "server/index.html")

@csrf_exempt
def jsonfile(request):
    if request.method == "POST":
        uploaded_file = request.FILES['telemetry']
        print(uploaded_file.__dict__)
        print(uploaded_file.name)
        print(type(uploaded_file))
        str_text = ''
        for line in uploaded_file:
            str_text = str_text + line.decode()
        print(str_text)
        # name = default_storage.save(uploaded_file.name, uploaded_file)
        # print(name)
        return render(request, "server/index.html")