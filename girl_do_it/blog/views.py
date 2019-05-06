from django.shortcuts import render

# Create your views here.
def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur le blog Girls do it !</h1>
    """)