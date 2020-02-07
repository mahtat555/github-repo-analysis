"""GitHub module

This module enables you to manage list the languages used by the 100
trending public repositories on GitHub.
"""

import requests
from operator import itemgetter


from backend.models import get_data_json, set_data_json


# URL of list all public repositories on GitHub
URL_REPOS = "https://api.github.com/repositories"


# Lists languages for the specified repository
def languages(repos) -> list:
    """This function returns a lists of languages for the
    specified repository.

    """
    rep = requests.get(repos['url'] + '/languages')
    if rep.status_code != 200:
        return None
    return list(rep.json())


# List of  100 trending public repositories on GitHub in json format
def json_repos() -> list:
    """This funtion returns a list of  100 trending public repository
    on GitHub in json format.

    """
    list_repos = requests.get(URL_REPOS)

    if list_repos.status_code != 200:
        return None

    return list_repos.json()


# List of  100 trending public repos on GitHub and languages used
def repositories() -> list:
    """This funtion returns a list of 100 trending Github public
    repositories and the  languages they use.

    Return the `list` of `dict`.

    """
    # List of  repositories on GitHub in json format
    json = json_repos()

    # If GitHub-API rate limit exceeded
    if not json:
        # used data stored in `data.json`
        return get_data_json()

    list_repos = []
    for repos in json:
        dict = {}
        dict['repository'] = {
            'html_url': repos['html_url'],
            'url': repos['url']
        }
        # If GitHub-API rate limit exceeded
        lang = languages(repos)
        if isinstance(lang, list):
            dict['languages'] = lang
        else:
            return get_data_json()
        list_repos.append(dict)

    # Store the list of repositories in `data.json`
    if list_repos != get_data_json():
        set_data_json(list_repos)

    return list_repos


# This function returns a repository specified by `id`
def repository(id :int) -> dict:
    """This function returns a repository specified by `id`.

    Parameters :
        id :int - the repository number, is integer between 0 and 99.
    """
    # List of  repositories on GitHub in json format
    json = json_repos()

    # if GitHub-API rate limit exceeded
    if not json:
        # used data stored in `data.json`
        list_repos = get_data_json()
        try:
            return list_repos[id]
        except:
            return None

    # repository specified by `id`
    try:
        # 'id' is integer between 0 and 99
        repos = json[id]
    except:
        return None

    dict = {}
    # repository info
    dict['repository'] = {
        'html_url': repos['html_url'],
        'url': repos['url']
    }
    # Lists languages for `repos`
    dict['languages'] = languages(repos)

    return dict


# Number of repositories using a language
def number_repos(language=None):
    """This function returns the number of repositories using a language.

    """
    # List of repositories and the languages they use
    list_repos = repositories()

    if not list_repos:
        return None

    # for a given language
    if language:
        # `language` is string
        if not isinstance(language, str):
            return None

        nb_repos = 0
        # browse the list of repositories
        for repos in list_repos:
            # Test if `language` is in list of languages used by `repos`
            if language.lower() in map(str.lower, repos['languages']):
                nb_repos += 1

        # if the `language` not found
        if not nb_repos:
            return None

        return {
            "language": language,
            "nb_repos": nb_repos
        }

    # for all languages
    list_number_repos = {}
    # browse the list of repositories
    for repos in list_repos:
        # browse the list of languages used by `repos`
        for language in repos['languages']:
            try:
                list_number_repos[language] += 1
            except:
                list_number_repos[language] = 1

    # sort results by order descending
    list_number_repos = sort(list_number_repos)

    return [
        {'language': language, 'nb_repos': nb_repos}
        for language, nb_repos in list_number_repos.items()
    ]


# List of repositories using a language
def list_repos(language=None):
    """This function returns the list of repositories using a language.

    """
    # List of repositories and the languages they use
    list_repos = repositories()

    if not list_repos:
        return None

    # for a given language
    if language:
        # `language` is string
        if not isinstance(language, str):
            return None

        list_repos_lang = []
        # browse the list of repositories
        for repos in list_repos:
            # Test if `language` is in list of languages used by `repos`
            if language.lower() in map(str.lower, repos['languages']):
                list_repos_lang.append(repos['repository'])

        # if the `language` not found
        if not list_repos_lang:
            return None

        return {
            "language": language,
            "repositories": list_repos_lang
        }

    # for all languages
    list_lang_list_repos = {}
    # browse the list of repositories
    for repos in list_repos:
        # browse the list of languages used by `repos`
        for language in repos['languages']:
            try:
                list_lang_list_repos[language].append(repos['repository'])
            except:
                list_lang_list_repos[language] = [repos['repository']]

    # sort results by order descending
    list_lang_list_repos = sort(
        list_lang_list_repos,
        lambda tuple: len(tuple[1])
    )

    return [
        {'language': language, 'repositories': list_repos}
        for language, list_repos in list_lang_list_repos.items()
    ]


# Framework popularity over the 100 repos
def popularity(language=None, plot=False):
    """This function returns Framework popularity over the 100 repos
    """
    # List of repositories and the languages they use
    list_repos = repositories()

    if not list_repos:
        return None

    # for a given language
    if language:
        # `language` is string
        if not isinstance(language, str):
            return None

        nb_repos, sum_number_repos = 0, 0
        # browse the list of repositories
        for repos in list_repos:
            # sum (number of `repos` using a language) for all language
            sum_number_repos += len(repos['languages'])

            # Test if `language` is in list of languages used by `repos`
            if language.lower() in map(str.lower, repos['languages']):
                nb_repos += 1

        # if the `language` not found
        if not nb_repos:
            return None

        rate = nb_repos / sum_number_repos * 100

        if plot:
            return (
                [language, 'Others languages'],
                [
                    {'name': language, 'y': rate},
                    {'name': 'Others languages', 'y': 100 - rate}
                ]
            )

        return {
            "language": language,
            "popularity": rate
        }

    # for all languages
    list_nb_repos = {}
    # browse the list of repositories
    for repos in list_repos:
        # browse the list of languages used by `repos`
        for language in repos['languages']:
            try:
                list_nb_repos[language] += 1
            except:
                list_nb_repos[language] = 1

    # sum (number of `repos` using a language) for all language
    sum_number_repos = sum(list_nb_repos.values())

    if plot:
        return (
            list(list_nb_repos.keys()),
            [{'name': k, 'y': list_nb_repos[k]} for k in list_nb_repos]
        )

    # sort results by order descending
    list_nb_repos = sort(list_nb_repos)

    return [{
            'language': language,
            'popularity': nb_repos / sum_number_repos * 100
        }
        for language, nb_repos in list_nb_repos.items()
    ]


# Sort descending a dictionary by value
def sort(d :dict, key=itemgetter(1)) -> dict:
    """ Sort descending a dictionary by value """
    return dict(
        sorted(d.items(), key=key, reverse=True)
    )
