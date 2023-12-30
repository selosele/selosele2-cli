import click
import selosele2_cli.main as _main
import selosele2_cli.cli.menu as menu
import selosele2_cli.cli.config as config

# API BASE URI
API_BASE_URI = 'http://localhost:3000/api'

def uri(url: str) -> str:
  r"""
  API URI를 반환한다.
  """
  return API_BASE_URI + url

def headers() -> dict[str, str]:
  r"""
  API 호출에 필요한 header를 반환한다.
  """
  return { 'Authorization': f'Bearer {config.access_token}' }

def isAuthenticated() -> bool:
  r"""
  로그인이 되어 있으면 True를, 안 되어 있으면 False를 반환한다.
  """
  return config.access_token != ''

def go_to_main() -> None:
  r"""
  메인 화면으로 돌아간다.
  """
  _main.main()

def text(text: str, color: str = '') -> str:
  r"""
  click.style 텍스트와 색상을 완성하여 반환한다.
  """
  return click.style(text, fg=color)

def list_separator() -> str:
  r"""
  목록 출력 시, 항목 간의 구분자를 반환한다.
  
  :| (파이프)가 아니라 ㅣ (한글)이라는 점에 유의한다.
  :파이프 사용 시, simple-term-menu 패키지에서 파이프로 인해 데이터 출력에 문제가 있음.
  """
  return 'ㅣ'

def menu_default_options():
  r"""
  메뉴 기본 설정 값을 반환한다.
  """
  return {
    'show_search_hint': True,
    'show_search_hint_text': menu.footer_menu(),
    'search_key': 's',
    'search_highlight_style': ['fg_black', 'standout', 'bold']
  }
