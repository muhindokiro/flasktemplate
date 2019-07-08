import unittest
from app.models import Blog

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog('blog category','my blog')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))


if __name__ == '__main__':
    unittest.main()