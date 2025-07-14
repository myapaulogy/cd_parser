from enum import Enum
import re

spec = [
        # Comments
        #[r'\/\/.*', None],
        # Whitespace
        [r'\s', None],

        [r'\d+(\.\d*)?', 'NUMERICAL'],
        [r'^\w+', 'IDENTIFIER'],

        [r'=', '='],

        [r"^;", ';'],
        # End of Expression

        # coordinate expression
        [r"^\(", '('],
        [r"^,", ','],
        [r"^\)", ')'],
        ]

class Token:
    def __init__(self, token_type: str, token_value) -> None:
        self.type = token_type
        self.value = token_value

class Tokenizer:
    def __init__(self, string) -> None:
        self.string: str = string
        self.cursor = 0


    def is_eof(self) -> bool:
        return self.cursor == len(self.string)


    def has_more_tokens(self) -> bool:
        return self.cursor < len(self.string)


    def get_next_token(self) -> Token | None:
        if not self.has_more_tokens():
            return

        string_slice = self.string[self.cursor:]
        for (reg, token_type) in spec:
            token_value = self.match(reg, string_slice)

            if not token_value:
                continue

            if not token_type:
                return self.get_next_token()

            return Token(token_type, token_value)

        raise TypeError(f'index({self.cursor}) unexpected value found: {string_slice}')


    def match(self, reg, string) -> str | None:
        matched = re.match(reg, string)
        if not matched:
            return

        self.cursor += len(matched[0])
        return matched[0]


