# -*- coding: utf-8 -*-

import click
import requests
import selosele2_cli.cli.menu as menu
import selosele2_cli.cli.post_list as post_list
from selosele2_cli.cli.utils import uri
from selosele2_cli.cli.utils import headers
from selosele2_cli.cli.utils import menu_default_options
from simple_term_menu import TerminalMenu
from datetime import datetime

@click.group()
def cli():
  pass

@cli.command()
@click.argument("post_id", type=list[str])
def main(post_id: list[str]):
  
  # 포스트 상세 조회
  response = requests.get(uri(f"/post/{''.join(post_id)}"), headers=headers())
  post = response.json()
  reg_date = datetime.strptime(post["regDate"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
  
  click.echo('\n\n\n\n\n\n')
  click.echo(click.style(post["title"], bg="blue", fg="white"))
  click.echo("======================================================================")
  click.echo(f"{menu.post_reg_date_text()} {reg_date}")
  click.echo("======================================================================")
  click.echo(post["rawText"])
  
  # 메뉴 선택
  terminal_menu = TerminalMenu(
    ["목록으로 돌아가기"],
    title="",
    **menu_default_options()
  )
  menu_index = terminal_menu.show()
  
  # 목록으로 돌아가기
  if menu_index == 0:
    post_list.main()
  