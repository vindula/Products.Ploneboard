#
# Ploneboard transform tests
#

import unittest
from zope.interface.verify import verifyClass, verifyObject
from Products.Ploneboard.tests import PloneboardTestCase
from Products.CMFCore.utils import getToolByName
from Products.Ploneboard.config import PLONEBOARD_TOOL

from Products.CMFPlone.utils import _createObjectByType


class TestTransformRegistration(PloneboardTestCase.PloneboardTestCase):
    """Test transform registration """

    def afterSetUp(self):
        self.board = _createObjectByType('Ploneboard', self.folder, 'board')

    def testDefaultRegistrations(self):
        """Check if the default registrations are present."""
        tool = getToolByName(self.portal, PLONEBOARD_TOOL)
        self.failUnlessEqual(len(tool.getTransforms()), 3)
        self.failUnlessEqual(len(tool.getEnabledTransforms()), 3)

    def testDisabling(self):
        """Try registering and unregistering a transform"""
        tool = getToolByName(self.portal, PLONEBOARD_TOOL)
        tool.enableTransform('safe_html', enabled=False)
        self.failIf('safe_html' in tool.getEnabledTransforms())
        tool.enableTransform('safe_html')
        self.failUnless('safe_html' in tool.getEnabledTransforms())


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTransformRegistration))
    return suite

