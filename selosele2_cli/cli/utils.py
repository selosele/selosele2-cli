import click

# API BASE URI
API_BASE_URI = 'http://localhost:3000/api'

def uri(url: str) -> str:
  """
  API URI를 반환한다.
  """
  return API_BASE_URI + url

def text(text: str, color: str = '') -> str:
  """
  click.style 텍스트와 색상을 완성하여 반환한다.
  """
  return click.style(text, fg=color)
