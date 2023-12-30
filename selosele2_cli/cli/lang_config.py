import click
from simple_term_menu import TerminalMenu
from selosele2_cli.cli.utils import go_to_main
import selosele2_cli.cli.config as config
import selosele2_cli.cli.menu as menu

@click.command()
def main():
  menu_exited = False
  
  while not menu_exited:
    
    # 메뉴 선택
    options = menu.lang_config_texts()
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    
    # 한국어
    if menu_entry_index == 0:
      config.lang_code = 'ko'
      go_to_main()
    
    # 영어
    if menu_entry_index == 1:
      config.lang_code = 'en'
      go_to_main()