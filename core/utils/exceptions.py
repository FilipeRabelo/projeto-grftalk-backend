from rest_framework.exceptions import APIException  # classe base de exceção do rest_framework

class ValidationError(Exception):
  status_code = 400
  default_detail = 'Parâmetros inválidos para a requisição'
  default_code = 'validation_error'