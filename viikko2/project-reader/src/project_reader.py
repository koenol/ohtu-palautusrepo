from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)
        dep = parsed_toml.get("tool").get("poetry").get("dependencies")
        dev_dep = parsed_toml.get("tool").get("poetry").get("group").get("dev").get("dependencies")
        authors = parsed_toml.get("tool").get("poetry").get("authors")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parsed_toml.get("tool").get("poetry").get("name"), parsed_toml.get("tool").get("poetry").get("description"), dep, dev_dep, parsed_toml.get("tool").get("poetry").get("license"), authors)
