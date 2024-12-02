import pygame
import sys
import game
import intro

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Menu")

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)

# 폰트 설정
font = pygame.font.Font(None, 40)

# 버튼 정의
def draw_button(text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # 버튼 색상 변화 및 클릭 이벤트 처리
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=((x + (w / 2)), (y + (h / 2))))
    screen.blit(text_surface, text_rect)

# 버튼 클릭 시 실행될 함수
def start_game():
    print("Game Starting...")
    game.run_game()
    # 이후 게임 로직 실행 코드 위치

def open_settings():
    print("Settings Opened")
    intro.intro_game()
    # 이후 설정 화면 코드 위치

def quit_game():
    pygame.quit()
    sys.exit()

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 메뉴 화면 그리기
    screen.fill(grey)  # 배경색 설정
    draw_button("Start", 350, 200, 100, 50, white, (200, 200, 200), start_game)
    draw_button("Intro", 350, 300, 100, 50, white, (200, 200, 200), open_settings)
    draw_button("Quit", 350, 400, 100, 50, white, (200, 200, 200), quit_game)

    pygame.display.flip()  # 화면 업데이트
    pygame.time.Clock().tick(60)  # FPS 설정

pygame.quit()
sys.exit()