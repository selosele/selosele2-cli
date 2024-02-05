#-*- coding: utf-8 -*-

import click
import selosele2_cli.cli.config as config

def print_main_title() -> None:
  r"""
  메인 타이틀을 출력한다.
  """
  click.echo(
    click.style(
      f"""
        ____  _      ____   _____    _____ _      _____  __      ____   ___  
      |  _ \| |    / __ \ / ____|  / ____| |    |_   _| \ \    / /_ | / _ \ 
      | |_) | |   | |  | | |  __  | |    | |      | |    \ \  / / | || | | |
      |  _ <| |   | |  | | | |_ | | |    | |      | |     \ \/ /  | || | | |
      | |_) | |___| |__| | |__| | | |____| |____ _| |_     \  /   | || |_| |
      |____/|______\____/ \_____|  \_____|______|_____|     \/    |_(_)___/ 
      """, fg="blue"
      )
    )
  click.echo("\n")

def choose_menu_text() -> str:
  r"""
  메뉴선택 텍스트를 반환한다.
  """
  if config.lang_code == "ko":
    return "메뉴 선택"
  elif config.lang_code == "en":
    return "Please choose a menu"
  
def footer_menu() -> str:
  r"""
  footer 메뉴를 반환한다.
  """
  if config.lang_code == "ko":
    return "Q: 프로그램 종료 | S: 검색"
  elif config.lang_code == "en":
    return "Q: Quit | S: Search"
  
def main_texts() -> list[str]:
  r"""
  메인 선택메뉴들을 반환한다.
  """
  if config.lang_code == "ko":
    
    # 로그인 상태일 경우
    if config.access_token != "":
      return ["1. 포스트 목록", "2. 언어설정"]
    # 비로그인 상태일 경우
    return ["1. 로그인", "2. 언어설정"]
      
  elif config.lang_code == "en":
    
    # 로그인 상태일 경우
    if config.access_token != "":
      return ["1. Get the posts", "2. Language Settings"]
    # 비로그인 상태일 경우
    return ["1. Sign-in", "2. Language Settings"]

def lang_config_texts() -> list[str]:
  r"""
  언어설정 선택메뉴들을 반환한다.
  """
  if config.lang_code == "ko":
    return ["1. 한국어", "2. 영어"]
  elif config.lang_code == "en":
    return ["1. Korean", "2. English"]

def signin_texts() -> dict[str, str]:
  r"""
  로그인 메뉴의 아이디, 비밀번호 텍스트를 반환한다.
  """
  if config.lang_code == "ko":
    return { "user_id": "아이디", "user_pw": "비밀번호" }
  elif config.lang_code == "en":
    return { "user_id": "ID", "user_pw": "Password" }

def signin_fail_text() -> str:
  r"""
  로그인 실패 메시지를 반환한다.
  """
  if config.lang_code == "ko":
    return "로그인에 실패했습니다."
  elif config.lang_code == "en":
    return "Faild to sign in."
  
def list_post_title(cnt) -> str:
  r"""
  포스트 목록 타이틀을 반환한다.
  """
  if config.lang_code == "ko":
    return f"포스트 목록 : 총 {cnt}개"
  elif config.lang_code == "en":
    return f"Total {cnt} Posts"

def post_tmp_text(tmpYn: str) -> str:
  r"""
  임시저장 포스트임을 알려주는 텍스트를 반환한다.
  """
  if config.lang_code == "ko":
    if tmpYn == "Y":
      return " [임시저장] "
    return ""
  elif config.lang_code == "en":
    if tmpYn == "Y":
      return " [temporary] "
    return ""

def post_reg_date_text() -> str:
  r"""
  포스트의 등록일자 텍스트를 반환한다.
  """
  if config.lang_code == "ko":
    return "등록일자:"
  elif config.lang_code == "en":
    return "Date:"
