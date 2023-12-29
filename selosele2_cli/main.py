import click
from simple_term_menu import TerminalMenu
import selosele2_cli.cli.utils as utils
import selosele2_cli.cli.menu as menu
import selosele2_cli.cli.signin as signin
import selosele2_cli.cli.blog_config as blog_config

@click.command()
def main():
  menu_exited = False
    
  while not menu_exited:
    menu.print_main_title()
    
    click.echo('=====================================')
    click.echo('메뉴 선택')
    click.echo('=====================================')
  
    # 메뉴 선택
    options = ['로그인', '환경설정', '프로그램 종료']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    
    # 로그인
    if menu_entry_index == 0:
      signin.main()
    
    # 환경설정
    if menu_entry_index == 1:
      blog_config.main()
    
    # 프로그램 종료
    if menu_entry_index == 2:
      menu_exited = True

if __name__ == '__main__':
  main()
