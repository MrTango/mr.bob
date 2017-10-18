import pkg_resources


class TemplateRegistry(object):

    def __init__(self):
        self.templates = {}
        self.subtemplates = {}
        for entry_point in pkg_resources.iter_entry_points('mrbob_templates'):
            self.templates[entry_point.name] = entry_point.load()
        for entry_point in pkg_resources.iter_entry_points(
                'mrbob_subtemplates'):
            self.subtemplates[entry_point.name] = entry_point.load()

    def list_templates(self):
        return self.templates.keys()

    def list_subtemplates(self):
        return self.subtemplates.keys()
