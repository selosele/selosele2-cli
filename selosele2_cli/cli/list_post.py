import click
import requests
import selosele2_cli.cli.menu as menu
from selosele2_cli.cli.utils import uri
from selosele2_cli.cli.utils import headers
from selosele2_cli.cli.utils import list_separator
from selosele2_cli.cli.utils import menu_default_options
from simple_term_menu import TerminalMenu
from datetime import datetime

@click.command()
def main():
  posts = []
  menu_exited = False
  
  while not menu_exited:
    
    # 포스트 목록 조회 파라미터
    # pageType: 메인
    params = { 'pageType': 'D01001' }
    
    # 포스트 목록 조회
    response = requests.get(uri('/post'), params=params, headers=headers())
    if response.status_code == 200:
      for i, post in enumerate(response.json()[0]):
        no = str(i+1)
        tmpText = menu.post_tmp_text(post['tmpYn'])
        title = post['title']
        reg_date = datetime.strptime(post['regDate'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d')
        
        posts.append(f'{no} {list_separator()}{tmpText}{title} {list_separator()} {reg_date}')
      
      terminal_menu = TerminalMenu(
        posts,
        title=menu.list_post_title(response.json()[1]),
        **menu_default_options()
      )
      menu_entry_index = terminal_menu.show()
      
      break
    else:
      print(response.json()['message'][0])