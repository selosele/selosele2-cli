import click
from simple_term_menu import TerminalMenu
import selosele2_cli.cli.menu as menu
import selosele2_cli.cli.signin as signin
import selosele2_cli.cli.config as config
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
    
    # 로그인
    if menu_entry_index == 0:
      signin.main()
      break
    
    # 언어설정
    if menu_entry_index == 1:
      lang_config.main()
      break
    
    # 프로그램 종료
    if menu_entry_index == 2:
      menu_exited = True
      break

if __name__ == '__main__':
  main()
