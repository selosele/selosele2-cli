import click
import selosele2_cli.cli.config as config
from selosele2_cli.cli.utils import isAuthenticated

# 메인 타이틀을 출력한다.
def print_main_title() -> None:
  click.echo(
    click.style(
      f"""
        ____  _      ____   _____    _____ _      _____  __      ____   ___  
      |  _ \| |    / __ \ / ____|  / ____| |    |_   _| \ \    / /_ | / _ \ 
      | |_) | |   | |  | | |  __  | |    | |      | |    \ \  / / | || | | |
      |  _ <| |   | |  | | | |_ | | |    | |      | |     \ \/ /  | || | | |
      | |_) | |___| |__| | |__| | | |____| |____ _| |_     \  /   | || |_| |
      |____/|______\____/ \_____|  \_____|______|_____|     \/    |_(_)___/ 
      """, fg='blue'
      )
    )
  click.echo('\n')

# footer 메뉴를 출력한다.
def print_footer() -> None:
  if config.lang_code == 'ko':
    click.echo(
      f"""
      Q: 프로그램 종료 | W: 로그아웃
      """
    )
  elif config.lang_code == 'en':
    click.echo(
      f"""
      Q: Quit | W: Sign-out
      """
    )

# 메뉴선택 문구를 출력한다.
def print_select_menu() -> None:
  click.echo('=====================================')
  if config.lang_code == 'ko':
    click.echo('메뉴 선택')
  elif config.lang_code == 'en':
    click.echo('Please choose a menu')
  click.echo('=====================================')
  
# 메인 선택메뉴를 출력한다.
def print_main() -> list[str]:
  if config.lang_code == 'ko':
    
    # 로그인 상태일 경우
    if isAuthenticated():
      return ['포스트 목록', '언어설정', '프로그램 종료']
    # 비로그인 상태일 경우
    else:
      return ['로그인', '언어설정', '프로그램 종료']
      
  elif config.lang_code == 'en':
    
    # 로그인 상태일 경우
    if isAuthenticated():
      return ['Get the posts', 'Language Settings', 'Quit']
    # 비로그인 상태일 경우
    else:
      return ['Sign-in', 'Language Settings', 'Quit']

# 언어설정 선택메뉴를 출력한다.
def print_lang_config() -> list[str]:
  if config.lang_code == 'ko':
    return ['한국어', '영어']
  elif config.lang_code == 'en':
    return ['Korean', 'English']

# 로그인 메뉴의 아이디, 비밀번호 텍스트를 출력한다.
def print_signin_text() -> dict[str, str]:
  if config.lang_code == 'ko':
    return { 'user_id': '아이디', 'user_pw': '비밀번호' }
  elif config.lang_code == 'en':
    return { 'user_id': 'ID', 'user_pw': 'Password' }
