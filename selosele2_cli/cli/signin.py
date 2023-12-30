import click
import requests
from selosele2_cli.cli.utils import uri

menu_exited = False

@click.command()
def main():
  while not menu_exited:
    user_id = click.prompt("아이디", type=str)
    user_pw = click.prompt("비밀번호", type=str, hide_input=True)
    data = { 'userId': user_id, 'userPw': user_pw }
    
    # 로그인
    response = requests.post(uri('/auth/signin'), data=data)
    if response.status_code == 201:
      # 로그인 성공 시, 액세스 토큰이랑 리프레시 토큰이 출력됨
      # TODO: 토큰 저장 및 메인 화면 출력
      print(response.json())
      break
    else:
      print(response.json()['message'][0])
