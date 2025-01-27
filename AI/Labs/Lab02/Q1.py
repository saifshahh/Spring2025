import random

class Environment:

    def __init__(self):
        self.components = [random.choice([0, 1]) for _ in range(9)]

    def percept(self, position):
        return "Safe" if self.components[position] == 1 else "Vulnerable"

    def display(self):
        print("System Initial State:")
        for i in range(len(self.components)):
            status = self.percept(i)
            print(f"Component {chr(65 + i)}: {status}")
            
    def update_component(self, component, status):
        self.components[component] = status

class SecurityAgent:
    
    def __init__(self, environment):
        self.environment = environment
        self.to_patch = []

    def Scan(self):
        self.to_patch = []  
        print("\nSystem Scan:")
        for i in range(len(self.environment.components)):
            if self.environment.percept(i) == 'Vulnerable':
                print(f"Warning: Component {chr(65 + i)} is vulnerable.")
                self.to_patch.append(i)
            else:
                print(f"Success: Component {chr(65 + i)} is safe.")

    def Patch(self):
        print("\nPatching Vulnerabilities:")
        for i in self.to_patch:
            self.environment.update_component(i, 1)
            print(f"Component {chr(65 + i)} has been patched and is now safe.")

    def Display(self):
        print("\nFinal Status:")
        for i in range(len(self.environment.components)):
            status = self.environment.percept(i)
            print(f"Component {chr(65 + i)}: {status}")


if __name__ == "__main__":
    
    environment = Environment()
    environment.display()

    agent = SecurityAgent(environment)
    agent.Scan()

    agent.Patch()

    agent.Display()

