import unittest
from app import auth

err_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1aWJhbmsuYXp1cmV3ZWJzaXRlcy5jb20iLCJleHAiOjE1ODAxMDIyODAsInN1YiI6IjEyMzQ1Njc4OTAifQ.uqVY6fh_QPM-ZOMWIWObdi1b6VvARJovYO2dF38sfa4'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1aWJhbmsuYXp1cmV3ZWJzaXRlcy5jb20iLCJleHAiOjE1ODAxMDIyODAsInN1YiI6IjEyMzQ1Njc4OTAifQ.MJX5gZuBlYCkzhu6Itz32wv6-l1SzshE88UyEBvIM40'
user_id = '1234567890'
exp = 1580102280

class TestAuth(unittest.TestCase):

    def test_encode(self):
        t = auth.generate_token(user_id, exp=exp)
        self.assertEqual(token,t.decode('utf-8'))


    def test_decode(self):
        t = auth.decode_token(token)
        self.assertIn('iss', t)
        self.assertEqual(t['iss'], 'uibank.azurewebsites.com')
        self.assertIn('exp', t)
        self.assertEqual(t['exp'], exp)
        self.assertIn('sub', t)
        self.assertEqual(t['sub'], user_id)
        pass

    def test_decode_raise(self):
        with self.assertRaises(Exception):
            auth.decode_token(err_token)

if __name__ == '__main__':
    import unittest
    unittest.main()
