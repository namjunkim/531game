import pygame
import random
import sys
import time

import Background

# 초기화
def intro_game():
    # 배경 음악 로드
    pygame.mixer.music.load('sound/intro.wav')  # 배경 음악 파일명
    pygame.mixer.music.play(-1)  # 음악을 무한 반복 재생

    # 화면 설정
    background = Background.Background(background_music='sound/intro.wav', screen_width=800, screen_height=600)
    background.run_background_music()
    screen = background.set_background_screen()
    pygame.display.set_caption("531 Shooting Game")

    # 한국어 폰트 설정 (프로젝트에 있는 폰트 파일이름으로 지정)
    font_path = 'font/Nanum_Gothic/NanumGothic-Bold.ttf'  # 사용할 한국어 폰트 파일 경로
    font_size = 20
    font = pygame.font.Font(font_path, font_size)

    # 색상
    white = (255, 255, 255)
    black = (0, 0, 0)

    intro_list = [
            "",
            "재배맨은 지구 침공을 위해, 자신의 씨앗을 지구로 보낸다.",
            "오직 531당원들만 이 사실을 알아 차리고, 전세계 정부에 도움을 청한다.",
            "하지만 모든 정부는 531을 묵살한다...",
            "이에 531 총재 이정규는 모든 Java 기술력을 총 동원...",
            "결국 531호를 만들게 된다...",
            "함장 : 이정규 총재, 전략사령관 : 김남준",
            "조타수 : 손한석, 무기조종수 : 김도현, 엔진담당 : 원정중....",
            "지구의 운명을 건 모험이 시작된다...",
            "(Space키를 누르시오...)"
        ]

    cnt = 0
    text_height = 580

    # 메인 루프
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 키 입력
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            cnt += 1
            time.sleep(0.2)
            if(cnt >= len(intro_list)):
                pygame.mixer.music.stop()
                return


        # 화면 지우기
        #screen.fill(black)

        rendered_text = font.render(intro_list[cnt], True, white)
        screen.blit(rendered_text, (10, 50 * cnt + 10))

        pygame.display.flip()
        clock.tick(60)

