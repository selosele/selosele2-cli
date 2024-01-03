import click
import selosele2_cli.cli.menu as menu
import selosele2_cli.cli.auth as auth
import selosele2_cli.cli.post_list as post_list
import selosele2_cli.cli.lang_config as lang_config
import selosele2_cli.cli.config as config
from simple_term_menu import TerminalMenu
from selosele2_cli.cli.utils import isAuthenticated
from selosele2_cli.cli.utils import menu_default_options

@click.command()
def main():
  if not config.main_title_printed:
    menu.print_main_title()
    config.main_title_printed = True
    
  # 메뉴 선택
  terminal_menu = TerminalMenu(
    menu.main_texts(),
    title=menu.choose_menu_text(),
    **menu_default_options()
  )
  menu_index = terminal_menu.show()
  
  # 로그인 or 포스트 목록
  if menu_index == 0:
    
    # 로그인이 되어 있으면 포스트 목록 화면을 출력하고
    if isAuthenticated():
      post_list.main()
    # 안 되어 있으면 로그인 화면을 출력한다.
    else:
      auth.signin()
  
  # 언어설정
  if menu_index == 1:
    lang_config.main()

if __name__ == "__main__":
  main()
