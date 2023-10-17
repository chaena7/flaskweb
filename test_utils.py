from utils import get_movie_info

def test_get_movie_info():
    # 샘플 url
    test_url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=185293"

    # 함수를 호출해서 값을 가져오기
    title, image, description = get_movie_info(test_url)
    print(title)
    print(image)
    print(description)

    assert title == '내일의 기억'