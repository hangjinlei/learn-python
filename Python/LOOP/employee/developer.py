from employee import Employee


class Developer(Employee):
    def __init__(self, first: str, last: str, pay: int, prog_lang: str):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
