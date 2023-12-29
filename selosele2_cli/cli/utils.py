import click

# API BASE URI
API_BASE_URI = 'http://localhost:3000/api'

def text(text: str, color: str = '') -> str:
  """
  click.style 텍스트와 색상을 완성하여 반환한다.
  """
  return click.style(text, fg=color)
