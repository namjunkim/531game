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

    # 색상
    white = (255, 255, 255)
    black = (0, 0, 0)

    intro = []

    itr_str = ''

    intro_list = [
        "aaaa",
        "bbb",
        "ccc",
        "ddd",
        "eeee",
        "ffff",
        "gggg",
        "hhhh"
    ]

    #intro_list = [
        #    "재배맨은 지구 침공을 위해, 자신의 씨앗을 지구로 보낸다.",
        #    "오직 531당원들만 이 사실을 알아 차리고, 전세계 정부에 도움을 청한다.",
        #    "하지만 모든 정부는 531을 무시한다...",
        #    "이에 531 총재 이정규는 모든 기술력을 총 동원...",
        #    "결국 531호를 만들게 된다...",
        #    "함장 : 이정규 총재, 전략사령관 : 김남준",
        #    "조타수 : 손한석, 무기조종수 : 원정준, 엔진담당 : 원정준....",
        #    "지구의 운명을 건 모험이 시작된다..."
        #]

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
            text_height -= 50
            time.sleep(0.2)
            intro.append(intro_list[cnt])

            if cnt > 0 and cnt < 8:
                for itr in intro:
                    itr_str = itr_str + '\n' + itr + '\n'
            else:
                itr_str = intro_list[0]

            if cnt == 8:
                pygame.quit()
                sys.exit()

        # 화면 지우기
        screen.fill(black)



        intro_font_0 = pygame.font.Font(None, 40)
        intro_text_0 = intro_font_0.render(str(itr_str), True, white)
        intro_rect_0 = intro_text_0.get_rect(center=(background.screen_width / 2, background.screen_height - 580))
        screen.blit(intro_text_0, intro_rect_0)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()