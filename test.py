tests = [
        [
            '82;',
            {
                'type': 'Program',
                'body': [
                    {
                        'type': 'ExpressionStatement',
                        'value': {
                            'type': 'NumericalLiteral',
                            'value': 82
                            }
                        }
                    ]
                }
            ],
        [
            '"hello";',
            {
                'type': 'Program',
                'body': [
                    {
                        'type': 'ExpressionStatement',
                        'value': {
                            'type': 'StringLiteral',
                            'value': 'hello' 
                            }
                        }
                    ]
                }
            ],
        [
            '"hello"; 38;',
            {
                'type': 'Program',
                'body': [
                    {
                        'type': 'ExpressionStatement',
                        'value': {
                            'type': 'StringLiteral',
                            'value': 'hello' 
                            }
                        },
                    {
                        'type': 'ExpressionStatement',
                        'value': {
                            'type': 'NumericalLiteral',
                            'value': 38 
                            }
                        }
                    ]
                }
            ]

        ]
