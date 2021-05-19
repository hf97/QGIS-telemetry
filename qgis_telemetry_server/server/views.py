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
        for filename in request.FILES:
            uploaded_file = request.FILES[filename]
            # print(uploaded_file.__dict__)
            # print(uploaded_file.name)
            # print(type(uploaded_file))
            # TODO meter isto sem iterar o ficheiro
            str_text = ''
            for line in uploaded_file:
                str_text = str_text + line.decode()
            # print(str_text)
            # print(uploaded_file)
            name = default_storage.save('./telemetry/'+uploaded_file.name+".json", uploaded_file)
            # name = default_storage.save(uploaded_file.name+".json", uploaded_file)
            # print(name)
        return render(request, "server/index.html")
