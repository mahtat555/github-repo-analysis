"""
"""

from os import path
from markdown import markdown
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse


from backend import github


TYPE = ('pie', 'column', 'line', 'bar', 'scatter')
README_HELP = path.join(
    path.dirname(path.dirname(path.dirname(__file__))),
    "README.md"
)
INDEX_MD = path.join(
    path.dirname(__file__),
    "templates/backend/index.md"
)

# Index page
def index(request):
    """ Index page

    URL:
        http://127.0.0.1:8000/api/  `or`
        http://127.0.0.1:8000/api/index

    """
    with open(INDEX_MD, 'r') as file:
        readme_md = file.read()

    html = markdown(
        readme_md,
        output_format='html5',
        extensions=['extra', 'smarty']
    )

    return render(
        request, "backend/index.html", {'html': html}
    )


# Help page
def help(request):
    """ Help page

    URL:
        http://127.0.0.1:8000/api/help

    """
    with open(README_HELP, 'r') as file:
        readme_md = file.read()

    html = markdown(
        readme_md,
        output_format='html5',
        extensions=['extra', 'smarty']
    )

    return render(
        request, "backend/index.html", {'html': html}
    )


# List of  100 trending public repos on GitHub and languages used
def repositories(request):
    """This funtion returns a list of 100 trending Github public
    repositories and the  languages they use in JSON format.

    URL:
        http://127.0.0.1:8000/api/repositories/

    """
    data = github.repositories()

    if data:
        return JsonResponse(data, safe=False)

    return error_404(request)



# Lists languages for the specified repository.
def repository(request, id :int):
    """This function returns a repository specified by
    `id` in JSON format.

    URL:
        http://127.0.0.1:8000/api/repository/<id>/
    """
    try:
        id = int(id)
        data = github.repository(id)
    except:
        return error_404(request)

    if data:
        return JsonResponse(data)

    return error_404(request)

# Number of repos using a language
def number_repos(request):
    """This function returns the number of repositories using a
    language in JSON format.

    URL:
        http://127.0.0.1:8000/api/number/?language=<language>/

    """
    try:
        language = request.GET.get('language')
        data = github.number_repos(language=language)
    except:
        return error_404(request)

    if data:
        return JsonResponse(data, safe=False)

    return error_404(request)


# The list of repos using a language
def list_repos(request):
    """This function returns the list of repositories using a
    language in JSON format.

    URL:
        http://127.0.0.1:8000/api/list/?language=<language>/

    """
    try:
        language = request.GET.get('language')
        data = github.list_repos(language=language)
    except:
        return error_404(request)

    if data:
        return JsonResponse(data, safe=False)

    return error_404(request)


# Frameworks popularity over the 100 repos
def popularity(request):
    """This function returns the Framework popularity over
    the 100 repos in JSON format.

    URL:
        http://127.0.0.1:8000/api/popularity/?language=<language>/

    """
    try:
        language = request.GET.get('language')
        data = github.popularity(language=language)
    except:
        return error_404(request)

    if data:
        return JsonResponse(data, safe=False)

    return error_404(request)


# A simple plotting utility for interpreting results
def plot(request):
    """A simple plotting utility for interpreting results.

    URL:
        http://127.0.0.1:8000/api/popularity/plot/?language=\
        <language>&type=<type>/

    """
    type = request.GET.get('type')
    if type not in TYPE:
        type = "column"

    language = request.GET.get('language')
    if language:
        type = "pie"

    # Frameworks popularity over the 100 repos
    try:
        languages, popularity = github.popularity(
            language=language, plot=True
        )
    except:
        return error_404(request)

    data = {
        'type': type,
        "languages": languages,
        "popularity": popularity,
    }
    return render( request, 'backend/plot.html', data)


# Error message `404 Page Not Found`
# The page_not_found() view is overridden by error_404()
def error_404(request, exception=None):
    """ Return a 404 error. Overloaded The HTTP 404, 404 Not Found,
    404, Page Not Found.

    """
    return JsonResponse({
            "message": "Not Found",
            "help_url": "http://127.0.0.1:8000/api/help"
        },
        status=404
    )
