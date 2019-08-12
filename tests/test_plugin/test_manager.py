import unittest, mock
from slackminion.plugin import PluginManager

class TestPluginManager(unittest.TestCase):

    def setUp(self):
        self.bot = mock.Mock()
        self.object = PluginManager(self.bot)

    def test_on_unload(self):
        fake_plugin = mock.Mock()
        self.object.plugins = [fake_plugin]
        self.object.unload_all()
        fake_plugin.on_unload.assert_called()
