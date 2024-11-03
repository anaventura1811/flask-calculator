# Tratamentos de erros no python
#  Uso de try e except (funcionamento similar ao do try e catch do JS)


class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422


try:
    print('Estou no bloco try')
    raise HttpUnprocessableEntityError('Estou lançando uma exception')
except Exception as exception:
    print('Estou no tratamento de erro')
    print(exception.name)
    print(exception.status_code)
    print(exception.message)
