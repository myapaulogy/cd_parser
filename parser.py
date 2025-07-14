import tokenizer

"""
Abstract Syntax Tree pattern
"""
class AbstractSyntaxTree:
    def program(self, body):
        return {
                'type': 'Program',
                'body': body
                }

    def statements(self, meta_data, coordinates):
        return {
                'type': 'Statements',
                'meta_data': meta_data,
                'coordinates': coordinates
                }

    def assignment_expression(self, left, right):
        return {
                "type": "AssignmentExpression",
                "operator": '=',
                "left": left,
                "right": right 
                }

    def coordinate_expression(self, x, y, z):
        return {
                "type": "CoordinateExpression",
                "x": x, 
                "y": y,
                "z": z
                }

    def string_literal(self, string):
        return {
                'type': 'StringLiteral',
                'value': string 
                }

"""
python friendly logical Tree
"""
class PythonLogicalTree:
    def program(self, body):
        return {
                'type': 'Program',
                'body': body
                }

    def statements(self, meta_data, coordinates):
        return {
                'meta_data': meta_data,
                'coordinates': coordinates
                }

    def assignment_expression(self, left, right):
        return {
                "type": "AssignmentExpression",
                "operator": '=',
                "left": left,
                "right": right 
                }

    def coordinate_expression(self, x, y, z):
        return [x, y, z]

    def string_literal(self, string):
        return string


#pattern = AbstractSyntaxTree()
pattern = PythonLogicalTree()

'''
Class used to Parse Critical Dimensions Map

meta_data: stores the parameters of the map { dx_y=2031; }
coordinates: stores the CD of the map       { ( 0, 0 ) 0 }
'''
class Parser:
    def __init__(self, string: str) -> None:
        self.string = string
        self.tokenizer = tokenizer.Tokenizer(string)
        
        self.lookahead = self.tokenizer.get_next_token()


    '''
    Entry to parse CD Map
    '''
    def parse(self):
        return self.program()


    '''
    program
        : statments
        ;
    '''
    def program(self):
        return pattern.program(self.statements())


    '''
    Returns statement lists of meta data and of coordinates

    statements
        : meta_data
        | coordinates
        ;
    '''
    def statements(self): 
        meta_data: list = [] 
        coordinates: list = [] 

        while self.lookahead is not None:

            if not self.lookahead:
                raise SyntaxError('Literal: unexpected literal production')

            if self.lookahead.type == '(':
                coordinates.append(self.coordinate_expression())

            elif self.lookahead.type == 'IDENTIFIER':
                meta_data.append(self.assignment_expression())

            else:
                raise SyntaxError(
                        f'Unexpected token ({self.lookahead.type}): {self.lookahead.value} at char ({self.tokenizer.cursor})'
                        )

        return pattern.statements(meta_data, coordinates)


    '''
    evaluation of expression for meta data

    ExpressionStatement
        : IDENTIFIER '=' NUMERICAL ';'
    '''
    def assignment_expression(self):
        left = self.string_literal()
        self.consume('=')
        right = self.numerical_literal()
        self.consume(';')
        return pattern.assignment_expression(left, right)


    '''
    evaluation of expression for coordinate 

    ExpressionStatement
        : '(' NUMERICAL ',' NUMERICAL ')' NUMERICAL
    '''
    def coordinate_expression(self):
        self.consume('(')
        x = self.numerical_literal()
        self.consume(',')
        y = self.numerical_literal()
        self.consume(')')
        z = self.numerical_literal()
        
        return pattern.coordinate_expression(x, y, z)



    '''
    StringLiteral
        : IDENTIFIRE
    '''
    def string_literal(self):
        token = self.consume('IDENTIFIER')
        return pattern.string_literal(token.value)


    '''
    NumericalLiteral
        : IDENTIFIRE
    '''
    def numerical_literal(self):
        token = self.consume('NUMERICAL')
        return pattern.string_literal(token.value)


    '''
    retrive/validate/advance tokenizer 
    '''
    def consume(self, token_type: str) -> tokenizer.Token:
        token = self.lookahead

        if not token:
            raise SyntaxError(
                    f'Unexpected end of input, expected {token_type}'
                    )

        if token.type != token_type:
            raise SyntaxError(
                    f'Unexpected token: {token.value}, expected: {token_type} at char ({self.tokenizer.cursor})'
                    )
        
        self.lookahead = self.tokenizer.get_next_token()

        return token


