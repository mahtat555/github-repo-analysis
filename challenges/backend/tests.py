"""Unit testing for our `backend` application

The Tests :
    1  Test the `repository()` function.
    2. Test the `list_repos()` function.
    3. Test the `number_repos()` function.
    4. Test the `popularity()` function.
    5. Test the `plot()` function.

"""

from django.test import TestCase
from django.urls import reverse


# 1. Test the repository() function
class RepositoryTestCase(TestCase):
    """Unit testing for the repository() function

    """

    def setUp(self):
        # id valid - integer between 0 and 99
        self.id_valid = '10'
        # id not valid - integer greater than 99
        self.id_not_valid = '111'

    def test_repository_repos_200(self):
        """Test if the status code is 200 if the given language valid
        """
        response = self.client.get(
            reverse(
                'api:repository',
                args = (self.id_valid,)
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_repository_repos_404(self):
        """Test if the status code is 404 if the given language not found
        """
        response = self.client.get(
            reverse(
                'api:repository',
                args = (self.id_not_valid,)
            )
        )
        self.assertEqual(response.status_code, 404)



# 2. Test the list_repos() function
class ListTestCase(TestCase):
    """Unit testing for the list_repos() function

    """

    def setUp(self):
        # language exists
        self.language_exists = "Python"
        # Language not found
        self.language_not_found = "PyRuCpJa"

    def test_list_repos_200(self):
        """Test if the status code is 200 if the given language valid
        """
        response = self.client.get(
            reverse('api:list_repos'),
            {'language': self.language_exists}
        )
        self.assertEqual(response.status_code, 200)

    def test_list_repos_404(self):
        """Test if the status code is 404 if the given language not found
        """
        response = self.client.get(
            reverse('api:list_repos'),
            {'language': self.language_not_found}
        )
        self.assertEqual(response.status_code, 404)

# 3. Test the number_repos function
class NumberTestCase(TestCase):
    """Unit testing for the number_repos() function

    """

    def setUp(self):
        # language exists
        self.language_exists = "Python"
        # Language not found
        self.language_not_found = "PyRuCpJa"

    def test_number_repos_200(self):
        """Test if the status code is 200 if the given language valid
        """
        response = self.client.get(
            reverse('api:number_repos'),
            {'language': self.language_exists}
        )
        self.assertEqual(response.status_code, 200)

    def test_number_repos_404(self):
        """Test if the status code is 404 if the given language not found
        """
        response = self.client.get(
            reverse('api:number_repos'),
            {'language': self.language_not_found}
        )
        self.assertEqual(response.status_code, 404)

# 4. Test the popularity() function.
class PopularityTestCase(TestCase):
    """Unit testing for the popularity() function

    """

    def setUp(self):
        # language exists
        self.language_exists = "Python"
        # Language not found
        self.language_not_found = "PyRuCpJa"

    def test_popularity_repos_200(self):
        """Test if the status code is 200 if the given language valid
        """
        response = self.client.get(
            reverse('api:popularity'),
            {'language': self.language_exists}
        )
        self.assertEqual(response.status_code, 200)

    def test_popularity_repos_404(self):
        """Test if the status code is 404 if the given language not found
        """
        response = self.client.get(
            reverse('api:popularity'),
            {'language': self.language_not_found}
        )
        self.assertEqual(response.status_code, 404)

# 5. Test the plot() function.
class PlotTestCase(TestCase):
    """Unit testing for the plot() function

    """

    def setUp(self):
        # language exists
        self.language_exists = "Python"
        # Language not found
        self.language_not_found = "PyRuCpJa"

    def test_plot_repos_200(self):
        """Test if the status code is 200 if the given language valid
        """
        response = self.client.get(
            reverse('api:plot'),
            {'language': self.language_exists}
        )
        self.assertEqual(response.status_code, 200)

    def test_plot_repos_404(self):
        """Test if the status code is 404 if the given language not found
        """
        response = self.client.get(
            reverse('api:plot'),
            {'language': self.language_not_found}
        )
        self.assertEqual(response.status_code, 404)
