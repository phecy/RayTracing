import unittest
import envtest # modifies path
from raytracing import *


class TestMaterial(unittest.TestCase):
    def testMaterialInvalid(self):
        self.assertRaises(TypeError, Material.n, 5)


class TestMaterialSubclasses(unittest.TestCase):
    def setUp(self) -> None:
        self.materials = Material.__subclasses__()
        self.fails = []

    def tearDown(self):
        self.assertEqual([], self.fails)

    def testMaterialSubclassesTypeError(self):
        for material in self.materials:
            try:
                self.assertRaises(TypeError, material.n, None)
                self.assertRaises(TypeError, material.n, 'test')
            except AssertionError:
                self.fails.append('TypeError for subclass {}'.format(material.__name__))

    def testMaterialSubclassesValueErrors(self):
        for material in self.materials:
            try:
                self.assertRaises(ValueError, material.n, 100)
                self.assertRaises(ValueError, material.n, 0)
                self.assertRaises(ValueError, material.n, -100)
            except AssertionError:
                self.fails.append('ValueError for subclass {}'.format(material.__name__))

    def testMaterialSubclasses(self):
        ''' These are sample values of refractive indexes for each subclass of material for a wavelength of 5 micron.
        In case of a new category of material, make sur to add the sample value to the list. '''
        refractiveIndexes = [1.3965252243506636, 1.5178527121226975, 1.5385861348077337, 1.5612286489801115,
                             1.539610715563772, 1.664053106820355, 1.5948478106562147, 1.6396821789377511,
                             1.5469302146171202, 1.5713583894047798, 1.4716376125966693, 1.459391121152617,
                             1.4251526811342752, 1.5810761652641074, 1.7197092324835102, 1.528065402814606,
                             1.541289278092723, 1.5975207997018837, 1.3404572894914368]

        for material in self.materials:
            n = material.n(5)
            if n not in refractiveIndexes:
                self.fails.append('Wrong value for subclass {}, {} not a valid n value.'.format(material.__name__, str(n)))


if __name__ == '__main__':
    unittest.main()



