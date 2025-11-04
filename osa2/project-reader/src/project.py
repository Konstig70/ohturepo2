class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, lisenssi, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = lisenssi

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        auth = "\n".join(f'- {author}' for author in self.authors)
        depd = "\n".join(f"- {dep}" for dep in self.dependencies)
        devdep = "\n".join(f"- {dep}" for dep in self.dev_dependencies) 
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '_'}"
            f"\n"
            f"Authors:"
            f"\n{auth}"
            f"\n"
            f"\nDependencies:"
            f"\n{depd}"
            f"\nDevelopment dependencies:"        
            f"\n{devdep}"
        )
