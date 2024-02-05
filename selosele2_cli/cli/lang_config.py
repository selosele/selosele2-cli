#-*- coding: utf-8 -*-"

import click
import selosele2_cli.cli.config as config
import selosele2_cli.cli.menu as menu
from simple_term_menu import TerminalMenu
from selosele2_cli.cli.utils import go_to_main
from selosele2_cli.cli.utils import menu_default_options

@click.command()
def main():
  
  # 메뉴 선택
  terminal_menu = TerminalMenu(
    menu.lang_config_texts(),
    title=menu.choose_menu_text(),
    **menu_default_options()
  )
  menu_index = terminal_menu.show()
  
  # 한국어
  if menu_index == 0:
    config.lang_code = "ko"
    go_to_main()
  
  # 영어
  if menu_index == 1:
    config.lang_code = "en"
    go_to_main()