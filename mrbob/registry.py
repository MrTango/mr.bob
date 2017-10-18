import pkg_resources


class TemplateRegistry(object):

    def __init__(self):
        self.templates = {
            'plone_addon': 'bobtemplates.plone:addon',
        }
        self.sub_templates = {}
        for entry_point in pkg_resources.iter_entry_points('mrbob_templates'):
            self.templates[entry_point.name] = entry_point.load()

    def list_templates(self):
        return self.templates.keys()
