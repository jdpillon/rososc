from pytouchosc.layout import Layout

import unittest
from StringIO import StringIO
from zipfile import ZipFile
from lxml import etree

homePath = '/Users/mjcarroll/ros/'
layoutPath = 'mcarroll-ros-pkg/rososc/rososc_tutorials/layouts/'
layoutFile = 'ROS-Demo-iPad.touchosc'
layoutBare = 'index.xml'

class LayoutTest_CreateFromExistingZip(unittest.TestCase):
    def setUp(self):
        self.path = homePath + layoutPath + layoutFile
        self.layout = Layout.createFromExisting(self.path)

    def testCreateFromExisting(self):
        self.assertIsInstance(self.layout,Layout,"Not an instance")
        
    def testCreateFromExistingMode(self):
        self.assertEqual(self.layout.mode,"1","Mode isn't iPad")
        
    def testCreateFromExistingOrientation(self):
        self.assertEqual(self.layout.orientation,"vertical","Orientation wrong")
        
    def testCreateFromExistingVersion(self):
        self.assertEqual(self.layout.version,"10")
        
class LayoutTest_CreateFromExistingFile(unittest.TestCase):
    def setUp(self):
        self.path = homePath + layoutPath + layoutBare
        self.f = open(self.path)
        self.layout = Layout.createFromExisting(self.f)

    def testCreateFromExisting(self):
        self.assertIsInstance(self.layout,Layout,"Not an instance")
        
    def testCreateFromExistingMode(self):
        self.assertEqual(self.layout.mode,"1","Mode isn't iPad")
        
    def testCreateFromExistingOrientation(self):
        self.assertEqual(self.layout.orientation,"vertical","Orientation wrong")
        
    def testCreateFromExistingVersion(self):
        self.assertEqual(self.layout.version,"10")
        
class LayoutTest(unittest.TestCase):
    def setUp(self):
        self.path = homePath + layoutPath + layoutFile
        self.layout = Layout.createFromExisting(self.path)
        
    def test_getNumberTabpages(self):
        self.assertEqual(self.layout.getNumberTabpages(),2)
        
    def test_getTabpageNames_base64(self):
        tabpageNames = self.layout.getTabpageNames(encoded=True)
        self.assertEqual(tabpageNames[0],"MQ==")
        self.assertEqual(tabpageNames[1],"VGV4dERlbW8=")
            
    def test_getTabpageNames_plainText(self):
        tabpageNames = self.layout.getTabpageNames()
        self.assertEqual(tabpageNames[0],'1')
        self.assertEqual(tabpageNames[1],'TextDemo')
        
    def test_walkDict(self):
        aDict = {'toggle1': {None: 0.0, 'z': False}}
        testDict = {'/toggle1': 0.0, '/toggle1/z': False}
        newDict = dict(self.layout.walkDict(aDict))
        self.assertEqual(newDict, testDict)
        
    def test_walkDict_withPath(self):
        aDict = {'toggle1': {None: 0.0, 'z': False}}
        testDict = {'/1/toggle1': 0.0, '/1/toggle1/z': False}
        path = '/1'
        newDict = dict(self.layout.walkDict(aDict, path))
        self.assertEqual(newDict, testDict)
        # Check for side effects
        self.assertEqual(path,'/1')
        
    def test_getSendableMessages(self):
        print self.layout.getSendableMessages(self.layout.getTabpageNames()[0])
        
    def test_getReceivableMessages(self):
        print self.layout.getReceivableMessages(self.layout.getTabpageNames()[0])
        