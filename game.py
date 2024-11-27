import pygame
import random
import sys
import time
import Emeny
import Player

# 초기화
pygame.init()

# 배경 음악 로드
pygame.mixer.music.load('sound/back_sound_1.wav')  # 배경 음악 파일명
pygame.mixer.music.play(-1)  # 음악을 무한 반복 재생

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Shooting Game")

# 색상 및 속도
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 5
bullet_speed = 10
enemy_speed = 2

# 플레이어 이미지 로드
player = Player.Player(player_img_path = 'image/531_plane.png', player_score = 10,
                       player_height = 40, player_length = 40, player_power = 0,
                       player_bullet_per_amount = 0, player_bullet_img_path = '',
                       player_bullet = '')
player_img = player.make_player_img()
player_rect = player.make_player_rect(player_img)
player_rect.topleft = (screen_width // 2, screen_height - 70)  # 플레이어 초기 위치

# 적 이미지 로드
enemy_chaebae = Emeny.Enemy(enemy_img_path = 'image/enemy.png', enemy_score = 10,
                    enemy_height = 40, enemy_length = 40, enemy_power = 0,
                    enemy_bullet_per_amount = 0, enemy_bullet_img_path = '',
                    enemy_bullet = '')
enemy_img = enemy_chaebae.make_enemy_img()
enemy_rect = enemy_chaebae.make_enemy_rect(enemy_img)


# 총알 및 적 리스트
bullets = []
enemies = []

#점수
score = 0

#생존여부
alive = True

# 새로운 적 생성 시간
enemy_spawn_time = 2000  # 2초
last_enemy_spawn = pygame.time.get_ticks()

elapsed_time_seconds = 0

# 메인 루프
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0 and alive:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < screen_width and alive:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.right > 0 and alive:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.right < screen_height and alive:
        player_rect.y += player_speed
    if keys[pygame.K_SPACE] and alive:
        bullet = pygame.Rect(player_rect.centerx - 5, player_rect.top - 10, 3, 3)
        pygame.mixer.Sound('sound/shoot.wav').play()
        bullets.append(bullet)

    # 적 생성
    if pygame.time.get_ticks() - last_enemy_spawn > enemy_spawn_time:
        enemy_x = random.randint(0, screen_width - 50)
        enemy_rect = pygame.Rect(enemy_x, 0, 40, 40)
        enemies.append(enemy_rect)
        last_enemy_spawn = pygame.time.get_ticks()

    # 총알 이동
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # 적 이동
    for enemy_rect in enemies[:]:
        enemy_rect.y += enemy_speed
        if enemy_rect.top > screen_height:
            enemies.remove(enemy_rect)

    # 충돌 체크
    for bullet in bullets[:]:
        for enemy_rect in enemies[:]:
            if bullet.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemies.remove(enemy_rect)
                score =  score + enemy_chaebae.enemy_score
                break

    # 적 충돌
    for enemy_rect in enemies[:]:
        if enemy_rect.colliderect(player_rect):
            pygame.mixer.music.stop()
            alive = False
            pygame.mixer.Sound('sound/dead_sound.wav').play()
            time.sleep(3.8)
            pygame.quit()


    # 화면 그리기
    screen.fill(black)

    # 경과 시간 가져오기 (밀리초 단위)
    elapsed_time_ms = pygame.time.get_ticks()

    # 밀리초를 초로 변환

    if alive:
        elapsed_time_seconds = elapsed_time_ms / 1000.0

    font = pygame.font.Font(None, 23)
    text = font.render(f"Elapsed Time: {elapsed_time_seconds:.2f} sec", True, white)
    text_rect = text.get_rect(center=(screen_width - 90, screen_height - 580))
    screen.blit(text, text_rect)

    score_font = pygame.font.Font(None, 40)
    score_text = score_font.render(str(score), True, white)
    score_rect = score_text.get_rect(center=(screen_width - 750, screen_height - 580))
    screen.blit(score_text, score_rect)

    for bullet in bullets:
        pygame.draw.rect(screen, white, bullet)
    for enemy_rect in enemies:
        screen.blit(enemy_img, enemy_rect)


    screen.blit(player_img, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()