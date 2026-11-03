
import pygame
import asyncio
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cricket Champions 4.0")
clock = pygame.time.Clock()

# Colours
WHITE = (255, 255, 255)
GREEN = (35, 115, 55)
LIGHT_GREEN = (55, 145, 70)
DARK = (8, 35, 28)
GOLD = (255, 205, 55)
RED = (210, 45, 45)
BLUE = (35, 85, 190)
SKIN = (235, 175, 125)
BROWN = (130, 80, 40)
PITCH = (190, 155, 110)

title_font = pygame.font.Font(None, 65)
font = pygame.font.Font(None, 35)
small_font = pygame.font.Font(None, 25)
subtitle_font = pygame.font.Font(None, 30)
score_font = pygame.font.Font(None, 42)

# Game settings
score = 0
wickets = 0
balls = 0
high_score = 0
target = 30
match_result = ""

player_x = 450
ball_x = 450
ball_y = 160
ball_speed = 5

ball_state = "delivery"
shot_vx = 0
shot_vy = 0

game_state = "menu"
message = "GET READY!"
message_timer = 0
swing_timer = 0
frame = 0
shot_runs = 0
shot_direction = "STRAIGHT"
particles = []
celebration_timer = 0
celebration_text = ""

# Buttons
left_btn = pygame.Rect(35, 510, 100, 65)
right_btn = pygame.Rect(150, 510, 100, 65)
hit_btn = pygame.Rect(680, 500, 180, 80)
pause_btn = pygame.Rect(790, 20, 75, 45)
play_btn = pygame.Rect(310, 390, 280, 65)

left_shot_btn = pygame.Rect(300, 510, 105, 48)
straight_shot_btn = pygame.Rect(415, 510, 125, 48)
right_shot_btn = pygame.Rect(550, 510, 105, 48)


def draw_text(value, font_obj, color, x, y, center=False):
    image = font_obj.render(str(value), True, color)

    if center:
        screen.blit(image, image.get_rect(center=(x, y)))
    else:
        screen.blit(image, (x, y))


def reset_match():
    global score, wickets, balls, player_x
    global game_state, message, match_result

    score = 0
    wickets = 0
    balls = 0
    player_x = 450
    message = "NEW INNINGS!"
    match_result = ""
    game_state = "playing"
    reset_ball()


def reset_ball():
    global ball_x, ball_y, ball_speed, ball_state

    ball_x = random.randint(405, 495)
    ball_y = 165
    ball_speed = 5 if balls < 6 else 7
    ball_state = "delivery"


def create_celebration(text):
    global particles, celebration_timer, celebration_text

    celebration_text = text
    celebration_timer = 90
    particles = []

    for _ in range(65):
        particles.append({
            "x": random.randint(250, 650),
            "y": random.randint(170, 330),
            "vx": random.uniform(-4, 4),
            "vy": random.uniform(-7, -2),
            "life": random.randint(35, 75),
            "size": random.randint(3, 7),
            "color": random.choice([
                GOLD, WHITE, RED,
                (70, 210, 120), (70, 150, 255)
            ])
        })


def update_celebration():
    global celebration_timer, particles

    if celebration_timer > 0:
        celebration_timer -= 1

    for particle in particles[:]:
        particle["x"] += particle["vx"]
        particle["y"] += particle["vy"]
        particle["vy"] += 0.16
        particle["life"] -= 1

        if particle["life"] <= 0:
            particles.remove(particle)


def draw_celebration():
    for particle in particles:
        pygame.draw.rect(
            screen,
            particle["color"],
            (
                int(particle["x"]),
                int(particle["y"]),
                particle["size"],
                particle["size"]
            ),
            border_radius=2
        )

    if celebration_timer > 0:
        pulse = 1 + abs(math.sin(frame * 0.18)) * 0.12

        banner = title_font.render(
            celebration_text, True, GOLD
        )
        banner = pygame.transform.rotozoom(banner, 0, pulse)

        shadow = title_font.render(
            celebration_text, True, DARK
        )
        shadow = pygame.transform.rotozoom(shadow, 0, pulse)

        screen.blit(shadow, shadow.get_rect(center=(452, 235)))
        screen.blit(banner, banner.get_rect(center=(450, 232)))


def draw_stadium():
    screen.fill((7, 22, 38))
    pygame.draw.rect(screen, (22, 48, 65), (0, 55, WIDTH, 75))

    # Stadium crowd
    for row in range(3):
        y = 65 + row * 19

        for x in range(25, 880, 22):
            colors = [
                (210, 75, 65),
                (235, 190, 65),
                (65, 145, 210),
                (220, 220, 210)
            ]

            color = colors[(x // 22 + row) % 4]
            pygame.draw.circle(screen, color, (x, y), 4)

    # Floodlights
    for x in (75, 825):
        pygame.draw.line(
            screen, (170, 185, 195),
            (x, 30), (x, 100), 5
        )

        pygame.draw.rect(
            screen, (235, 235, 205),
            (x - 25, 20, 50, 12),
            border_radius=4
        )

        pygame.draw.circle(
            screen, (255, 245, 190),
            (x, 27), 28, 1
        )

    # Ground
    pygame.draw.ellipse(
        screen, (30, 105, 57),
        (20, 105, 860, 390)
    )

    pygame.draw.ellipse(
        screen, (65, 145, 75),
        (35, 125, 830, 350), 2
    )

    for y in range(150, 460, 65):
        pygame.draw.arc(
            screen, (48, 128, 65),
            (35, y - 25, 830, 90),
            0, math.pi, 3
        )

    # Boundary and pitch
    pygame.draw.ellipse(
        screen, GOLD,
        (20, 105, 860, 390), 4
    )

    pygame.draw.rect(
        screen, PITCH,
        (325, 125, 250, 330),
        border_radius=8
    )

    pygame.draw.rect(
        screen, (215, 185, 145),
        (335, 135, 230, 310),
        2, border_radius=6
    )

    pygame.draw.line(
        screen, WHITE,
        (340, 180), (560, 180), 3
    )

    pygame.draw.line(
        screen, WHITE,
        (340, 425), (560, 425), 3
    )

    # Wickets
    for x in (420, 450, 480):
        pygame.draw.rect(
            screen, WHITE,
            (x, 435, 7, 40),
            border_radius=2
        )

    pygame.draw.line(
        screen, WHITE,
        (400, 435), (500, 435), 3
    )


def draw_fielder(x, y):
    bounce = math.sin(frame * 0.07 + x) * 3
    cy = int(y + bounce)

    # Legs
    pygame.draw.line(
        screen, (25, 35, 45),
        (x - 4, cy + 27), (x - 10, cy + 43), 6
    )

    pygame.draw.line(
        screen, (25, 35, 45),
        (x + 4, cy + 27), (x + 10, cy + 43), 6
    )

    # Jersey
    pygame.draw.rect(
        screen, (25, 75, 165),
        (x - 11, cy + 8, 22, 23),
        border_radius=5
    )

    # Arms
    pygame.draw.line(
        screen, SKIN,
        (x - 9, cy + 13), (x - 19, cy + 28), 5
    )

    pygame.draw.line(
        screen, SKIN,
        (x + 9, cy + 13), (x + 19, cy + 28), 5
    )

    # Head and cap
    pygame.draw.circle(screen, SKIN, (int(x), cy), 10)

    pygame.draw.arc(
        screen, (20, 35, 70),
        (x - 11, cy - 10, 22, 16),
        math.pi, 2 * math.pi, 5
    )


def draw_bowler():
    movement = math.sin(frame * 0.16) * 7

    # Legs
    pygame.draw.line(
        screen, WHITE,
        (440, 185), (431, 211 + movement), 9
    )

    pygame.draw.line(
        screen, WHITE,
        (460, 185), (470, 210 - movement), 9
    )

    # Shoes
    pygame.draw.ellipse(
        screen, (25, 30, 35),
        (418, 205 + movement, 20, 8)
    )

    pygame.draw.ellipse(
        screen, (25, 30, 35),
        (462, 205 - movement, 20, 8)
    )

    # Shirt
    pygame.draw.rect(
        screen, RED,
        (433, 148, 34, 42),
        border_radius=7
    )

    pygame.draw.line(
        screen, GOLD,
        (450, 151), (450, 186), 3
    )

    # Arms
    pygame.draw.line(
        screen, SKIN,
        (438, 158), (419, 174 + movement), 8
    )

    pygame.draw.line(
        screen, SKIN,
        (462, 158), (481, 139 - movement), 8
    )

    pygame.draw.circle(
        screen, SKIN,
        (419, int(174 + movement)), 5
    )

    pygame.draw.circle(
        screen, SKIN,
        (481, int(139 - movement)), 5
    )

    # Head and cap
    pygame.draw.circle(screen, SKIN, (450, 133), 15)

    pygame.draw.arc(
        screen, (35, 25, 20),
        (436, 119, 28, 20),
        math.pi, 2 * math.pi, 7
    )

    pygame.draw.arc(
        screen, GOLD,
        (435, 118, 30, 15),
        math.pi, 2 * math.pi, 3
    )


def draw_batsman():
    # Shadow
    pygame.draw.ellipse(
        screen, (95, 75, 55),
        (player_x - 30, 430, 62, 12)
    )

    # Pads
    pygame.draw.rect(
        screen, (235, 235, 225),
        (player_x - 19, 402, 15, 31),
        border_radius=5
    )

    pygame.draw.rect(
        screen, (235, 235, 225),
        (player_x + 4, 402, 15, 31),
        border_radius=5
    )

    # Shoes
    pygame.draw.line(
        screen, (30, 35, 45),
        (player_x - 12, 432),
        (player_x - 23, 437), 7
    )

    pygame.draw.line(
        screen, (30, 35, 45),
        (player_x + 12, 432),
        (player_x + 23, 437), 7
    )

    # Jersey
    pygame.draw.rect(
        screen, (20, 80, 185),
        (player_x - 23, 357, 46, 52),
        border_radius=9
    )

    pygame.draw.line(
        screen, GOLD,
        (player_x, 362), (player_x, 402), 3
    )

    pygame.draw.rect(
        screen, (25, 55, 115),
        (player_x - 22, 395, 44, 13),
        border_radius=4
    )

    # Arms
    pygame.draw.line(
        screen, SKIN,
        (player_x - 17, 370),
        (player_x + 9, 382), 9
    )

    pygame.draw.line(
        screen, SKIN,
        (player_x + 12, 370),
        (player_x + 23, 383), 8
    )

    pygame.draw.circle(
        screen, WHITE,
        (int(player_x + 10), 383), 7
    )

    pygame.draw.circle(
        screen, WHITE,
        (int(player_x + 24), 384), 6
    )

    # Neck and face
    pygame.draw.rect(
        screen, SKIN,
        (player_x - 6, 345, 12, 15)
    )

    pygame.draw.circle(
        screen, SKIN,
        (int(player_x), 337), 17
    )

    # Helmet
    pygame.draw.arc(
        screen, (20, 35, 65),
        (player_x - 19, 317, 38, 34),
        math.pi, 2 * math.pi
    )

    pygame.draw.line(
        screen, (20, 35, 65),
        (player_x + 4, 334),
        (player_x + 24, 342), 3
    )

    pygame.draw.circle(
        screen, (30, 30, 30),
        (int(player_x + 7), 336), 2
    )

    # Bat swing
    if swing_timer > 0:
        angle = -1.15 + (8 - swing_timer) * 0.30
    else:
        angle = 0.65

    end_x = player_x + math.cos(angle) * 72
    end_y = 380 + math.sin(angle) * 72

    pygame.draw.line(
        screen, (65, 42, 25),
        (player_x + 17, 378),
        (player_x + 25, 389), 6
    )

    pygame.draw.line(
        screen, (190, 125, 55),
        (player_x + 23, 386),
        (end_x, end_y), 15
    )

    pygame.draw.line(
        screen, (225, 175, 95),
        (player_x + 23, 386),
        (end_x, end_y), 3
    )


def draw_ball():
    # Ball trail
    pygame.draw.line(
        screen, (255, 170, 170),
        (int(ball_x), int(ball_y - 25)),
        (int(ball_x), int(ball_y - 10)), 4
    )

    pygame.draw.circle(
        screen, RED,
        (int(ball_x), int(ball_y)), 11
    )

    pygame.draw.circle(
        screen, WHITE,
        (int(ball_x), int(ball_y)), 11, 2
    )


def draw_scoreboard():
    pygame.draw.rect(
        screen, (5, 22, 30),
        (18, 9, 864, 72),
        border_radius=14
    )

    pygame.draw.rect(
        screen, (65, 105, 85),
        (18, 9, 864, 72),
        2, border_radius=14
    )

    draw_text("CRICKET CHAMPIONS", small_font, GOLD, 35, 18)
    draw_text(score, score_font, WHITE, 360, 25)
    draw_text("RUNS", small_font, (180, 205, 190), 360, 58)

    draw_text(
        f"{wickets}/3",
        score_font, WHITE, 510, 25
    )

    draw_text(
        "WICKETS",
        small_font, (180, 205, 190), 510, 58
    )

    draw_text(
        f"{balls // 6}.{balls % 6}",
        score_font, WHITE, 665, 25
    )

    draw_text(
        "OVERS",
        small_font, (180, 205, 190), 665, 58
    )

    pygame.draw.rect(
        screen, (40, 65, 55),
        pause_btn, border_radius=8
    )

    draw_text(
        "II", font, WHITE,
        pause_btn.centerx, pause_btn.centery, True
    )


def draw_button(rect, label, color):
    pygame.draw.rect(
        screen, (15, 25, 25),
        rect.move(0, 5), border_radius=13
    )

    pygame.draw.rect(
        screen, color,
        rect, border_radius=13
    )

    pygame.draw.rect(
        screen, WHITE,
        rect, 2, border_radius=13
    )

    draw_text(
        label, font, WHITE,
        rect.centerx, rect.centery, True
    )


def draw_game():
    draw_stadium()

    # Fielders
    draw_fielder(115, 250)
    draw_fielder(780, 250)
    draw_fielder(150, 400)
    draw_fielder(750, 400)

    draw_bowler()
    draw_batsman()
    draw_ball()
    draw_scoreboard()

    # Movement and hit buttons
    draw_button(left_btn, "<", (45, 90, 150))
    draw_button(right_btn, ">", (45, 90, 150))
    draw_button(hit_btn, "HIT!", (175, 45, 45))

    # Shot direction buttons
    direction_buttons = [
        (left_shot_btn, "LEFT", "LEFT"),
        (straight_shot_btn, "STRAIGHT", "STRAIGHT"),
        (right_shot_btn, "RIGHT", "RIGHT")
    ]

    for rect, label, direction in direction_buttons:
        color = GOLD if shot_direction == direction else (45, 75, 85)

        pygame.draw.rect(
            screen, color, rect,
            border_radius=9
        )

        pygame.draw.rect(
            screen, WHITE, rect, 2,
            border_radius=9
        )

        text_color = DARK if shot_direction == direction else WHITE

        draw_text(
            label, small_font, text_color,
            rect.centerx, rect.centery, True
        )

    draw_text(
        f"TARGET: {target} RUNS",
        small_font, GOLD, 450, 485, True
    )

    draw_text(
        message, font, GOLD, 450, 570, True
    )

    draw_celebration()


def hit_ball():
    global score, ball_state, shot_vx, shot_vy
    global swing_timer, message, shot_runs

    timing = abs(ball_y - 385) + abs(ball_x - player_x) * 0.65

    if timing < 20:
        shot_runs = 6
    elif timing < 35:
        shot_runs = 4
    elif timing < 45:
        shot_runs = 3
    elif timing < 55:
        shot_runs = 2
    elif timing < 70:
        shot_runs = 1
    else:
        shot_runs = 0

    score += shot_runs
    ball_state = "shot"

    # Shot direction
    if shot_direction == "LEFT":
        shot_vx = -random.randint(7, 10)

    elif shot_direction == "RIGHT":
        shot_vx = random.randint(7, 10)

    else:
        shot_vx = random.choice([-2, -1, 1, 2])

    shot_vy = -random.randint(8, 12)

    swing_timer = 8

    if shot_runs == 6:
        message = "SIX! AMAZING SHOT!"
        create_celebration("SIX!!!")

    elif shot_runs == 4:
        message = "FOUR! BOUNDARY!"
        create_celebration("FOUR!!!")

    elif shot_runs == 0:
        message = "DOT BALL!"

    else:
        message = f"{shot_runs} RUNS!"


def finish_match():
    global game_state, high_score, match_result

    if score > high_score:
        high_score = score

    match_result = "YOU WIN!" if score >= target else "YOU LOSE!"
    game_state = "gameover"


def miss_ball():
    global wickets, balls, message

    wickets += 1
    balls += 1

    message = "BOWLED! WICKET!"

    if wickets >= 3 or balls >= 12 or score >= target:
        finish_match()
    else:
        reset_ball()


def handle_hit():
    if (
        game_state == "playing"
        and ball_state == "delivery"
        and 320 <= ball_y <= 420
        and abs(ball_x - player_x) < 100
    ):
        hit_ball()


def handle_touch(x, y):
    global player_x, game_state, shot_direction

    if game_state == "menu":
        reset_match()
        return

    if game_state == "gameover":
        reset_match()
        return

    if game_state == "paused":
        if pause_btn.collidepoint(x, y):
            game_state = "playing"
        return

    if pause_btn.collidepoint(x, y):
        game_state = "paused"

    elif left_btn.collidepoint(x, y):
        player_x -= 35

    elif right_btn.collidepoint(x, y):
        player_x += 35

    elif left_shot_btn.collidepoint(x, y):
        shot_direction = "LEFT"

    elif straight_shot_btn.collidepoint(x, y):
        shot_direction = "STRAIGHT"

    elif right_shot_btn.collidepoint(x, y):
        shot_direction = "RIGHT"

    elif hit_btn.collidepoint(x, y):
        handle_hit()

    player_x = max(355, min(545, player_x))


async def main():
    global frame, ball_x, ball_y, ball_state
    global shot_vx, shot_vy, balls
    global player_x, swing_timer, game_state, shot_direction

    running = True

    while running:
        frame += 1
        update_celebration()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_SPACE:

                    if game_state in ("menu", "gameover"):
                        reset_match()

                    elif game_state == "paused":
                        game_state = "playing"

                    else:
                        handle_hit()

                if game_state == "playing":

                    if event.key == pygame.K_1:
                        shot_direction = "LEFT"

                    elif event.key == pygame.K_2:
                        shot_direction = "STRAIGHT"

                    elif event.key == pygame.K_3:
                        shot_direction = "RIGHT"

                if event.key == pygame.K_p:

                    if game_state == "playing":
                        game_state = "paused"

                    elif game_state == "paused":
                        game_state = "playing"

            if event.type == pygame.MOUSEBUTTONDOWN:

                if game_state == "menu" and play_btn.collidepoint(event.pos):
                    reset_match()

                else:
                    handle_touch(*event.pos)

            if event.type == pygame.FINGERDOWN:

                x = int(event.x * WIDTH)
                y = int(event.y * HEIGHT)

                if game_state == "menu":
                    reset_match()

                else:
                    handle_touch(x, y)

        keys = pygame.key.get_pressed()

        if game_state == "playing":

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_x -= 5

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player_x += 5

            player_x = max(355, min(545, player_x))

            if swing_timer > 0:
                swing_timer -= 1

            if ball_state == "delivery":

                ball_y += ball_speed
                ball_x += math.sin(frame * 0.12) * 2

                if ball_y > 440:
                    miss_ball()

            elif ball_state == "shot":

                ball_x += shot_vx
                ball_y += shot_vy
                shot_vy += 0.25

                if (
                    ball_y < 95
                    or ball_x < 20
                    or ball_x > 880
                ):
                    balls += 1

                    if score >= target or balls >= 12:
                        finish_match()

                    else:
                        reset_ball()

        # Draw screens
        if game_state == "menu":

            draw_stadium()

            panel = pygame.Surface(
                (700, 330),
                pygame.SRCALPHA
            )

            panel.fill((4, 20, 28, 225))
            screen.blit(panel, (100, 145))

            pygame.draw.rect(
                screen, GOLD,
                (100, 145, 700, 330),
                3, border_radius=28
            )

            draw_text(
                "WELCOME TO",
                subtitle_font, WHITE,
                450, 205, True
            )

            draw_text(
                "CRICKET CHAMPIONS",
                title_font, GOLD,
                450, 260, True
            )

            draw_text(
                "2 OVER BATTING CHALLENGE",
                font, WHITE,
                450, 315, True
            )

            draw_text(
                "Score 30 runs to win the match!",
                small_font, (210, 225, 215),
                450, 350, True
            )

            mouse_pos = pygame.mouse.get_pos()

            play_color = (
                (225, 175, 45)
                if play_btn.collidepoint(mouse_pos)
                else (185, 125, 25)
            )

            pygame.draw.rect(
                screen, (15, 25, 25),
                play_btn.move(0, 6),
                border_radius=16
            )

            pygame.draw.rect(
                screen, play_color,
                play_btn,
                border_radius=16
            )

            pygame.draw.rect(
                screen, WHITE,
                play_btn, 2,
                border_radius=16
            )

            draw_text(
                "PLAY MATCH",
                font, WHITE,
                play_btn.centerx,
                play_btn.centery, True
            )

            draw_text(
                "Move: A / D     Aim: 1 / 2 / 3     Hit: SPACE",
                small_font, WHITE,
                450, 485, True
            )

        elif game_state == "playing":
            draw_game()

        elif game_state == "paused":

            draw_game()

            pygame.draw.rect(
                screen, DARK,
                (250, 220, 400, 150),
                border_radius=20
            )

            draw_text(
                "PAUSED",
                title_font, GOLD,
                450, 270, True
            )

            draw_text(
                "PRESS SPACE OR P TO RESUME",
                small_font, WHITE,
                450, 325, True
            )

        elif game_state == "gameover":

            draw_stadium()

            pygame.draw.rect(
                screen, DARK,
                (170, 155, 560, 300),
                border_radius=25
            )

            draw_text(
                "MATCH OVER",
                title_font, GOLD,
                450, 195, True
            )

            result_color = (
                (80, 230, 120)
                if match_result == "YOU WIN!"
                else RED
            )

            draw_text(
                match_result,
                font, result_color,
                450, 245, True
            )

            draw_text(
                f"FINAL SCORE: {score}",
                font, WHITE,
                450, 290, True
            )

            draw_text(
                f"WICKETS: {wickets}     OVERS: {balls // 6}.{balls % 6}",
                font, WHITE,
                450, 335, True
            )

            draw_text(
                f"BEST SCORE: {high_score}",
                font, GOLD,
                450, 380, True
            )

            draw_text(
                "PRESS SPACE OR TAP TO PLAY AGAIN",
                small_font, WHITE,
                450, 425, True
            )

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
"""  """