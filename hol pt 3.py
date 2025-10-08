import pygame
import mysql.connector
import random
import sys

# -----------------------------
# Database Connection
# -----------------------------
def get_db_connection():
    """Connect safely to the MySQL database."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="your_username",      # 👈 Replace
            password="your_password",  # 👈 Replace
            database="higherlower_db"
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        pygame.quit()
        sys.exit()

def get_random_item(cursor):
    """Fetch a random item (id, name, stat_value)."""
    cursor.execute("SELECT id, name, stat_value FROM items ORDER BY RAND() LIMIT 1;")
    return cursor.fetchone()

def save_score_to_db(name, score):
    """Save player's score to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO scores (player_name, score) VALUES (%s, %s)"
    cursor.execute(query, (name, score))
    conn.commit()
    cursor.close()
    conn.close()

def get_top_scores(limit=5):
    """Get top scores from database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT player_name, score, played_at FROM scores ORDER BY score DESC, played_at ASC LIMIT %s",
        (limit,)
    )
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

# -----------------------------
# Pygame Setup
# -----------------------------
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Higher or Lower (MySQL Edition)")

font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 32)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (180, 180, 180)

clock = pygame.time.Clock()

# -----------------------------
# Utility Functions
# -----------------------------
def draw_text(text, font, color, surface, x, y):
    """Draw centered text."""
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# -----------------------------
# Main Menu
# -----------------------------
def main_menu():
    selected = 0
    options = ["Start Game", "Leaderboard", "Quit"]

    while True:
        screen.fill(WHITE)
        draw_text("Higher or Lower", font, BLACK, screen, 400, 150)

        for i, option in enumerate(options):
            color = GREEN if i == selected else BLACK
            draw_text(option, font, color, screen, 400, 300 + i * 70)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        higher_lower_game()
                    elif selected == 1:
                        show_leaderboard()
                    elif selected == 2:
                        pygame.quit()
                        sys.exit()
        clock.tick(30)

# -----------------------------
# Game Logic
# -----------------------------
def higher_lower_game():
    conn = get_db_connection()
    cursor = conn.cursor()

    score = 0
    running = True

    left_item = get_random_item(cursor)
    right_item = get_random_item(cursor)
    while right_item[0] == left_item[0]:
        right_item = get_random_item(cursor)

    while running:
        screen.fill(WHITE)
        draw_text("Higher or Lower", font, BLACK, screen, 400, 60)
        draw_text(f"Score: {score}", small_font, BLACK, screen, 400, 100)

        draw_text(left_item[1], font, BLACK, screen, 200, 300)
        draw_text("VS", font, BLACK, screen, 400, 300)
        draw_text(right_item[1], font, BLACK, screen, 600, 300)

        draw_text("Press ↑ if Right is Higher", small_font, GREEN, screen, 400, 450)
        draw_text("Press ↓ if Left is Higher", small_font, RED, screen, 400, 500)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:  # Guess right item higher
                    if right_item[2] > left_item[2]:
                        score += 1
                        left_item = right_item
                        right_item = get_random_item(cursor)
                        while right_item[0] == left_item[0]:
                            right_item = get_random_item(cursor)
                    else:
                        name = get_player_name(score)
                        save_score_to_db(name, score)
                        game_over(score, name)
                        running = False

                elif event.key == pygame.K_DOWN:  # Guess left item higher
                    if left_item[2] > right_item[2]:
                        score += 1
                        left_item = right_item
                        right_item = get_random_item(cursor)
                        while right_item[0] == left_item[0]:
                            right_item = get_random_item(cursor)
                    else:
                        name = get_player_name(score)
                        save_score_to_db(name, score)
                        game_over(score, name)
                        running = False
        clock.tick(30)

    cursor.close()
    conn.close()

# -----------------------------
# Player Name Input
# -----------------------------
def get_player_name(score):
    name = ""
    entering = True
    while entering:
        screen.fill(WHITE)
        draw_text("Game Over!", font, RED, screen, 400, 180)
        draw_text(f"Your Score: {score}", font, BLACK, screen, 400, 240)
        draw_text("Enter your name:", small_font, BLACK, screen, 400, 320)
        draw_text(name or "_", font, BLACK, screen, 400, 380)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip():
                    entering = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isprintable() and len(name) < 15:
                    name += event.unicode
    return name.strip()

# -----------------------------
# Game Over Screen
# -----------------------------
def game_over(score, player_name):
    waiting = True
    while waiting:
        screen.fill(WHITE)
        draw_text(f"Thanks, {player_name}!", font, BLACK, screen, 400, 250)
        draw_text(f"Your final score: {score}", small_font, BLACK, screen, 400, 310)
        draw_text("Press ENTER to return to menu", small_font, GRAY, screen, 400, 380)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False
    main_menu()

# -----------------------------
# Leaderboard Screen
# -----------------------------
def show_leaderboard():
    scores = get_top_scores()
    viewing = True
    while viewing:
        screen.fill(WHITE)
        draw_text("Leaderboard", font, BLACK, screen, 400, 100)

        if scores:
            y = 180
            for rank, (name, score, date) in enumerate(scores, start=1):
                draw_text(f"{rank}. {name} - {score} pts", small_font, BLACK, screen, 400, y)
                y += 50
        else:
            draw_text("No scores yet!", small_font, RED, screen, 400, 300)

        draw_text("Press ENTER to return", small_font, GRAY, screen, 400, 520)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                viewing = False
    main_menu()

# -----------------------------
# Run the Game
# -----------------------------
if __name__ == "__main__":
    main_menu()
