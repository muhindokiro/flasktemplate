import unittest
from app.models import Pitch

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Pitch('blog category','my blog')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


if __name__ == '__main__':
    unittest.main()