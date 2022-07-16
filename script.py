import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://namu.wiki" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["yellow", "orange"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "박영민")
write("description", "경운중 출신, 퉤에엣")
write("button", "꺼무위키")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생일": "071227",
  "좋아하는 것": "재밌는 게임",
  "싫어하는 것": "컴파일 에러",
  "꿈": "게임 만들기"
}
information(informations)
