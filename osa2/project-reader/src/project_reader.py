from urllib import request
from project import Project
import tomllib  

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = tomllib.loads(content)
        lisenssi = data["tool"]["poetry"]["license"]
        authors = data["tool"]["poetry"]["authors"]
        return Project(data["tool"]["poetry"]["name"], data["tool"]["poetry"]["description"], data["tool"]["poetry"]["dependencies"], data["tool"]["poetry"]["group"]["dev"]["dependencies"], lisenssi, authors)
