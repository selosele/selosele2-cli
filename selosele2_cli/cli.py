import click
from simple_term_menu import TerminalMenu
import selosele2_cli.utils as utils

@click.command()
def main():
  menu_exited = False
    
  while not menu_exited:
    click.echo(click.style('블로그 CLI 클라이언트', bold=True) + click.style(' v1.0', fg='yellow'))
    click.echo('\n')
    
    click.echo('=====================================')
    click.echo('메뉴 선택')
    click.echo('=====================================')
  
    # 메뉴 선택
    options = ['로그인', '환경설정', '프로그램 종료']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    
    # 프로그램 종료
    if options[menu_entry_index] == '프로그램 종료':
      menu_exited = True

if __name__ == '__main__':
  main()
