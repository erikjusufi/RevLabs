import requests
import json
import unittest
from task import app

class TestJoinNamesPost(unittest.TestCase):
    app = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = app.test_client()
    
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_basic_use_case(self) -> None:
        """
        Usual test case
        """
        test = {
            "first_names": [["Adam", "1234"], ["John", "4321"]],
            "last_names": [["Anderson", "4321"], ["Smith", "1234"]],
        }

        result = requests.post(
            "http://127.0.0.1:5000/rest/join_names",
            json=test,
        )

        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result.json(),
            {
                "full_names": [["Adam", "Smith", "1234"], ["John", "Anderson", "4321"]],
                "unpaired": [],
            },
        )

    def test_unpaired(self) -> None:
        """
        Test unpaired
        """
        test = {
            "first_names": [["Adam", "1234"], ["John", "4321"], ["Erik", "9999"]],
            "last_names": [["Anderson", "4321"], ["Smith", "1234"]],
        }

        result=  requests.post(
            "http://127.0.0.1:5000/rest/join_names",
            json=test,
        )

        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result.json(),
            {
                "full_names": [["Adam", "Smith", "1234"], ["John", "Anderson", "4321"]],
                "unpaired": [["Erik", "9999"]],
            },
        )

if __name__ == '__main__':
    unittest.main()
