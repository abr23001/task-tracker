from dataclasses import dataclass

@dataclass
class Plan:
    name: str
    description: str
    icon: str
    apps: list[str]

    def __str__(self):
        return f"Plan(name={self.name}, description={self.description}, icon={self.icon}, apps={self.apps})"
    