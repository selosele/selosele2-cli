import click
import requests
import selosele2_cli.cli.config as config
import selosele2_cli.cli.menu as menu
from selosele2_cli.cli.utils import uri
from selosele2_cli.cli.utils import go_to_main

# 로그인
@click.command()
def signin():
  menu_exited = False
  
  while not menu_exited:
    user_id = click.prompt(menu.signin_texts()['user_id'], type=click.STRING)
    user_pw = click.prompt(menu.signin_texts()['user_pw'], type=click.STRING, hide_input=True)
    data = { 'userId': user_id, 'userPw': user_pw }
    
    # 로그인
    response = requests.post(uri('/auth/signin'), data=data)
    if response.status_code == 201:
      config.access_token = response.json()['accessToken']
      config.refresh_token = response.json()['refreshToken']
      click.clear()
      go_to_main()
    else:
      print(menu.signin_fail_text())

# 로그아웃
def signout():
  config.access_token = ''
  config.refresh_token = ''