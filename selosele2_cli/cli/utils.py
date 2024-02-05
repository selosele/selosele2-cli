# -*- coding: utf-8 -*-

import selosele2_cli.cli.config as config

# API BASE URI
#API_BASE_URI = "http://localhost:3000/api"
API_BASE_URI = "https://blog.selosele.com/api"

def uri(url: str) -> str:
  r"""
  API URI를 반환한다.
  """
  return API_BASE_URI + url

def headers() -> dict[str, str]:
  r"""
  API 호출에 필요한 header를 반환한다.
  """
  return { "Authorization": f"Bearer {config.access_token}" }

def set_access_token(access_token: str) -> None:
  r"""
  액세스 토큰을 설정한다.
  """
  config.access_token = access_token
  
def set_refresh_token(refresh_token: str) -> None:
  r"""
  리프레시 토큰을 설정한다.
  """
  config.refresh_token = refresh_token

def go_to_main() -> None:
  r"""
  메인 화면으로 돌아간다.
  """
  import selosele2_cli.main as _main
  _main.main()

def list_separator() -> str:
  r"""
  목록 출력 시, 항목 간의 구분자를 반환한다.
  
  :| (파이프)가 아니라 ㅣ (한글)이라는 점에 유의한다.
  :파이프 사용 시, simple-term-menu 패키지에서 파이프로 인해 데이터 출력에 문제가 있음.
  """
  return "ㅣ"

def menu_default_options() -> dict[str, any]:
  r"""
  메뉴 기본 설정 값을 반환한다.
  """
  import selosele2_cli.cli.menu as menu
  return {
    "show_search_hint": True,
    "show_search_hint_text": menu.footer_menu(),
    "search_key": "s",
    "search_highlight_style": ["bg_yellow", "fg_black", "bold"]
  }
