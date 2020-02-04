from django.test import TestCase, Client

class BlogTestCase(TestCase):

# @beforeのようなメソッド
    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('/')

        # status code => 200 OK
        # status code => 300 Redirect
        # status code => 404 Not Found
        self.assertEqual(200, res.status_code)

    def test_fail_access(self):
        res = self.c.get('/unknown')
        print(res.status_code)
        self.assertEqual(404, res.status_code)
