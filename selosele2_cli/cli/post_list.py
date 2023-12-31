import click
import requests
import selosele2_cli.cli.menu as menu
import selosele2_cli.cli.post_view as post_view
from selosele2_cli.cli.utils import uri
from selosele2_cli.cli.utils import headers
from selosele2_cli.cli.utils import list_separator
from selosele2_cli.cli.utils import menu_default_options
from selosele2_cli.cli.utils import set_access_token
from simple_term_menu import TerminalMenu
from datetime import datetime

@click.command()
def main():
  posts = []
  menu_exited = False
  
  while not menu_exited:
    
    # 포스트 목록 조회 파라미터
    # pageType: 메인
    params = { "pageType": "D01001" }
    
    # 포스트 목록 조회
    response = requests.get(uri("/post"), params=params, headers=headers())
    if response.status_code == 200:
      for i, post in enumerate(response.json()[0]):
        # no = str(i+1)
        tmp_text = menu.post_tmp_text(post["tmpYn"])
        title = post["title"]
        reg_date = datetime.strptime(post["regDate"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
        
        posts.append(f"{post['id']} {list_separator()}{tmp_text}{title} {list_separator()} {reg_date}")
      
      terminal_menu = TerminalMenu(
        posts,
        title=menu.list_post_title(response.json()[1]),
        **menu_default_options()
      )
      menu_entry_index = terminal_menu.show()
      post_id = str(posts[menu_entry_index]).split(list_separator())[0].strip()
      click.clear()
      
      # 포스트 상세 조회
      post_view.main([post_id])
      break
    
    # 액세스 토큰 갱신 (공통로직으로 분리 예정)
    # elif response.status_code == 401:
    #   refresh_response = requests.post(uri("/auth/refresh"))
    #   new_access_token = refresh_response.json()["accessToken"]
    #   set_access_token(new_access_token)
    #   session = requests.Session()
    #   session.headers.update({ "Authorization": f"Bearer {new_access_token}" })
    #   response.request.headers["Authorization"] = session.headers["Authorization"]
    #   session.send(response.request, verify=False)
    else:
      print(response.json()["message"][0])