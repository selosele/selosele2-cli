import click
import requests
import selosele2_cli.cli.menu as menu
from selosele2_cli.cli.utils import uri
from selosele2_cli.cli.utils import headers
from selosele2_cli.cli.utils import list_separator
from simple_term_menu import TerminalMenu
from datetime import datetime

@click.command()
def main():
  menu_exited = False
  post_list = []
  
  while not menu_exited:
    
    # 포스트 목록 조회 파라미터
    # pageType: 메인
    params = { 'pageType': 'D01001' }
    
    # 포스트 목록 조회
    response = requests.get(uri('/post'), params=params, headers=headers())
    if response.status_code == 200:
      posts = response.json()
      for i, post in enumerate(posts[0]):
        # reg_date = datetime.strftime(str(post['regDate']), '%Y-%m-%dT%H:%M:%S.%fZ')
        # reg_date_f = reg_date.strftime('%Y-%m-%d')
        post_list.append(f"{str(i+1)} {list_separator()}{menu.post_tmp_text(post['tmpYn'])}{post['title']} {list_separator()} {str(post['regDate'])}")
      
      options = post_list
      terminal_menu = TerminalMenu(
        options,
        title=menu.list_post_title()
      )
      menu_entry_index = terminal_menu.show()
      
      break
    else:
      print(response.json()['message'][0])