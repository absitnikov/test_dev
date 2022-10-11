import unittest
import functions


class TestSecretaryProgram(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('Start to test')

    def test_get_doc_owner_name(self):
        self.assertEqual(functions.get_doc_owner_name('11-2'), 'Геннадий Покемонов')

    def test_add_new_doc(self):
        self.assertEqual(functions.add_new_doc('11-3', 'pass', 'Иванов Иван', 2), 2)

    def test_delete_doc(self):
        self.assertTrue(functions.delete_doc('11-3'))

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(functions.get_all_doc_owners_names(), set)

    @classmethod
    def tearDown(self):
        print('End of the test')


if __name__ == '__main__':
    unittest.main()
