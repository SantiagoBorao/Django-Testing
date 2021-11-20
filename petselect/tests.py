from django.test import TestCase
from .models import Pet
# Create your tests here.
class PetModelTests(TestCase):
    def setUp(self):
        #  pet creation in the model
        Pet.object.create(name= 'chihuahua', hair='short', size='small')
        Pet.object.create(name= 'Scottish Terrier', hair= 'medium', size='large')
    

    def test_dog_hair_length(self):
        #test store/retireval of hair length
        chi = Pet.object.get(name= 'chihuahua')
        scot = Pet.objects.get(name= 'Scottish Terrier')
        self.assertEqual(chi.hair, 'short')
        self.assertEqual(scot.hair, 'medium')