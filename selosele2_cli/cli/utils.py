import click
import selosele2_cli.main as _main
import selosele2_cli.cli.config as config

# API BASE URI
API_BASE_URI = 'http://localhost:3000/api'

# API URI를 반환한다.
def uri(url: str) -> str:
  return API_BASE_URI + url

# API 호출에 필요한 header를 반환한다.
def headers() -> dict[str, str]:
  return { 'Authorization': f'Bearer {config.access_token}' }

# 로그인이 되어 있으면 True를, 안 되어 있으면 False를 반환한다.
def isAuthenticated() -> bool:
  return config.access_token != ''

# 로그아웃을 한다.
def logout() -> None:
  config.access_token = ''
  config.refresh_token = ''

# 메인 화면으로 돌아간다.
def go_to_main() -> None:
  _main.main()

# click.style 텍스트와 색상을 완성하여 반환한다.
def text(text: str, color: str = '') -> str:
  return click.style(text, fg=color)

# 목록 출력 시, 항목 간의 구분자를 반환한다.
# 주의: | (파이프)가 아니라 ㅣ (한글)
# 파이프 사용 시, simple-term-menu 패키지에서 파이프 이슈로 인해서 데이터 출력에 문제가 있음
def list_separator() -> str:
  return 'ㅣ'
