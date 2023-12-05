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
        test = "Python {is an easy to [learn]}, (powerful programming language. It)\
        has efficient high-level [(data structures) and a simple but\
        effective approach to object-oriented programming]. Python's elegant\
        syntax and dynamic typing, together with its {interpreted nature,\
        make it an ideal language (for) scripting and rapid} application\
        development in many areas on most platforms."

        result = requests.post(
            "http://127.0.0.1:5000/rest/check_braces",
            json=test,
        )

        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result.json(),
            {
                "message": "All braces are in place"
            },
        )

    def test_missing_braces(self) -> None:
        """
        Test missing braces
        """
        test = "(abc[def]a[bc[de(f)ab}c"

        result = requests.post(
            "http://127.0.0.1:5000/rest/check_braces",
            json=test,
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(
            result.json(),
            {
                "(": 1, "[": 2, "}": 1
            },
        )
    
if __name__ == '__main__':
    unittest.main()
