from pydoc import describe
from utils import to_number

class Trend:
    def __init__(self, name, description, category, search_volume, growth):
        self.name = name
        self.description = description
        self.category = category
        self.search_volume = to_number(search_volume) if search_volume else None
        self.growth = growth if len(growth.split()) == 1 else growth.split()[1]

    def __repr__(self):
        return f'Trend({self.name})'

    def __str__(self):
        str = '\n+------------------------+'
        str += f'\nName: {self.name}'
        str += f'\nDesc: {self.description}'
        str += f'\nCategory: {self.category}'
        str += f'\nVolume: {self.search_volume}'
        str += f'\nGrowth: {self.growth}'

        return str
    
    def get_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'volume': self.search_volume,
            'growth': self.growth
        }

