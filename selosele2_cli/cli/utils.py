import click
import selosele2_cli.main as _main
import selosele2_cli.cli.config as config

# API BASE URI
API_BASE_URI = 'http://localhost:3000/api'

def uri(url: str) -> str:
  """
  API URI를 반환한다.
  """
  return API_BASE_URI + url

def isAuthenticated() -> bool:
  """
  로그인이 되어 있으면 True를, 안 되어 있으면 False를 반환한다.
  """
  return config.access_token != ''

def go_to_main() -> None:
  """"
  메인 화면으로 돌아간다.
  """
  _main.main()

def text(text: str, color: str = '') -> str:
  """
  click.style 텍스트와 색상을 완성하여 반환한다.
  """
  return click.style(text, fg=color)
