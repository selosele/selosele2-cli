import click
import requests
import selosele2_cli.cli.menu as menu
from selosele2_cli.cli.utils import uri
from selosele2_cli.cli.utils import headers
from datetime import datetime
from bs4 import BeautifulSoup

@click.group()
def cli():
  pass

@cli.command()
@click.argument("post_id", type=list[str])
def main(post_id: list[str]):
  menu_exited = False
  
  while not menu_exited:
  
    # 포스트 상세 조회
    response = requests.get(uri(f"/post/{''.join(post_id)}"), headers=headers())
    post = response.json()
    reg_date = datetime.strptime(post["regDate"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
    soup = BeautifulSoup(post["cont"], "html.parser")
    
    click.echo('\n\n\n\n\n\n')
    click.echo(post["title"])
    click.echo("======================================================================")
    click.echo(f"{menu.post_reg_date_text()} {reg_date}")
    click.echo("======================================================================")
    click.echo(soup.text)
    break
  