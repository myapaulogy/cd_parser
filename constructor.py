"""
Critical Dimension Map string 
constructor used to build the 
CD map from the AST parser
"""
class CriticalDimensionMapCSV:
    def chech_key(self, key: str, d: dict):
        if key not in d:
            raise KeyError(f'missing {key} in {d.keys()}')


    def program(self, program_dict: dict) -> str:
        self.chech_key('body', program_dict)
        return self.statements(program_dict['body'])


    def statements(self, statements_dict: dict) -> str:
        expressions = []
        for meta in statements_dict['meta_data']:
            expressions.append(self.assignment_expression(meta))

        for coordinate in statements_dict['coordinates']:
            expressions.append(self.coordinate_expression(coordinate))

        return '\n'.join(expressions)


    def assignment_expression(self, assignment: dict):
        self.chech_key('left', assignment)
        self.chech_key('operator', assignment)
        self.chech_key('right', assignment)

        return f'{assignment["left"]} {assignment["operator"]} {assignment["right"]};'


    def coordinate_expression(self, coordinates: list):
        if len(coordinates) != 3:
            raise KeyError(f'missing coordinates values')

        return f'( {coordinates[0]}, {coordinates[1]} ) {coordinates[2]}'


    def string_literal(self, string):
        return string


class Constructor:
    def __init__(self, dictionary: dict) -> None:
        self.dictionary: dict = dictionary

    def to_csv(self):
        return CriticalDimensionMapCSV().program(self.dictionary)
