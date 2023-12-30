import click
from simple_term_menu import TerminalMenu
from selosele2_cli.cli.utils import isAuthenticated
import selosele2_cli.cli.menu as menu
import selosele2_cli.cli.auth as auth
import selosele2_cli.cli.list_post as list_post
import selosele2_cli.cli.lang_config as lang_config

@click.command()
def main():
  menu.print_main_title()
  menu.print_select_menu()
  
  menu_exited = False
    
  while not menu_exited:
    
    # 메뉴 선택
    options = menu.print_main()
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    
    # 로그인 or 포스트 목록
    if menu_entry_index == 0:
      
      # 로그인이 되어 있으면 포스트 목록 화면을 출력하고
      if isAuthenticated():
        list_post.main()
      # 안 되어 있으면 로그인 화면을 출력한다.
      else:
        auth.signin()
      break
    
    # 언어설정
    if menu_entry_index == 1:
      lang_config.main()
      break
    
    # 프로그램 종료
    if menu_entry_index == 2:
      menu_exited = True
      auth.signout()
      break

if __name__ == '__main__':
  main()
