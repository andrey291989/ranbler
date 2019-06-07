import unittest
import ram

class TestCap(unittest.TestCase):
    # cписок групп в которых нужно узнать сколько подписчиком в ней
    id = ['rambler', 'ramblermail', 'horoscopesrambler', 'championat',
          'championat.auto', 'championat_cybersport', 'livejournal', 'afisha']
    # Токен для подключения к API (и тут тоже егонужно ввести :) )
    toc =

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        id = TestCap.id
        toc = TestCap.toc

        result = ram.namder(id, toc)
        self.assertEqual(type(result), list)

    def test_2(self):
        id = TestCap.id
        toc = TestCap.toc

        result = ram.namder(id, toc)
        self.assertEqual(type(result[0]), tuple )

if __name__ == '__main__':
    unittest.main()