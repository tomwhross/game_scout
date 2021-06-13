from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Render index
    """

    return render(
        request,
        "xbox/index.html",
    )
