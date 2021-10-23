import requests

data = [
    {
        "time":0,
        "menu":"밤식빵①②⑥ 양송이스프①②⑥ 부추스크램블에그①⑤ 통감자버터구이② 닭가슴살샐러드/갈릭 ①⑮ 오이피클 사과 아몬드시리얼/우유"
    },
    {
        "time":1,
        "menu":"쌀밥 오징어무우국⑤⑰ 등뼈김치찜⑤⑥⑨⑩ 봉골레파스타①②⑤⑥ 사과치커리초무침 깍두기⑨ 아이스망고 소떡소떡⑤⑥⑩"
    },
    {
        "time":2,
        "menu":"강황미밥 물만두국①⑤⑥⑩ 시금치계란말이①⑤ 갈릭연어데리야끼구이 김자반⑤ 열무나물무침⑤ 배추김치⑨ 요구르트"
    },
        {
        "time":0,
        "menu":"차조밥 된장찌개⑤⑱ 차돌박이숙주볶음⑤⑯(호주산801002405598) 까르보떡볶이②⑩ 배추나물무침⑤ 갓김치⑨ 단감 불고기후랑크⑤⑩⑮ /머스터드①"
    },
        {
        "time":1,
        "menu":"쌀밥 김치찌개⑤⑩ 불낙전골⑤⑯(호주산801001100129) 참치야채볶음⑤ 오이부추무침⑤ 깍두기⑨ 아이브② 물떡꼬치"
    },
        {
        "time":2,
        "menu":"쌀밥 전복죽⑱ 쇠고기데리야끼볶음⑤⑯(호주산801001100129) 연두부⑤/양념장⑤ 콘샐러드①⑤⑥ 배추김치⑨ 찰보리빵①⑤⑬ 요거링/초코볼②⑤⑥ 바나나/우유②"
    },
        {
        "time":0,
        "menu":"황미밥(학생쌀밥) 닭곰탕⑮ 쇠갈비떡찜⑤⑯ 해물부추전①⑤⑥ 무오이채장아찌무침 매콤츄러스만두 ⑤⑥⑩⑯ 고들빼기김치⑨ 포도 공주님/왕자님쥬스"
    },
        {
        "time":1,
        "menu":"참치새싹비빔밥⑤ 들깨시락국⑤ 버팔로윙오븐구이⑤⑮ 알배추겉절이 총각김치⑨ 바나나우유② 찹쌀고구마치즈볼 ①②⑤⑥"
    },
        {
        "time":2,
        "menu":"쌀밥 맑은소고기국⑤⑯ 베이컨스크램블에그 ①②⑨⑩ 찐두부/볶음김치⑤⑨ 김구이⑤ 바나나 에너지바①②⑤⑥ 아몬드시리얼⑥/우유②"
    },
        {
        "time":0,
        "menu":"속청콩밥⑤ 두부청경새우탕⑤⑨ 피자코든브루 ②⑤⑥⑮ 삼치데리야끼구이⑤ 후르츠마카로니샐러드①②⑤⑥ 배추김치⑨ 초코우유②/시험꾸러미"
    },

]

headers = {'Content-type': 'application/json'}

for x in data:
    a = requests.post("http://127.0.0.1:8000/meals/",headers = headers,json = x)
    print(a.text)