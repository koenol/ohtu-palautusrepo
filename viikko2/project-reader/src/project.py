class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_authors(self, authors):
        return "\n".join([f"- {author}" for author in authors])

    def _stringify_dependencies(self, dependencies):
        return "\n".join([f"- {dep}" for dep in dependencies])
        #return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            "\n"
            f"\nAuthors:"
            f"\n{self._stringify_authors(self.authors)}"
            "\n"
            f"\nDependencies:"
            f"\n{self._stringify_dependencies(self.dependencies)}"
            "\n"
            f"\nDevelopment dependencies:"
            f"\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
