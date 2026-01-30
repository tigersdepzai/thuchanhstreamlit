def handle_player_hit():
    global score

    for fruit in fruit_list:
        fruit_x = fruit[0]
        fruit_y = fruit[1]

        if check_collision(player_x, player_y, fruit_x, fruit_y):
            score += 1
            fruit[0] = random.randint(0, screen_width - fruit_size)
            fruit[1] = random.randint(-screen_height, 0)


while game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    move_fruits()
    handle_player_hit()

    if lives <= 0:
        game_running = False

    draw_game_screen()

    font = pygame.font.Font(None, 34)
    display_text = font.render("Score: " + str(score) + "    Lives: " + str(lives), True, COLOR_GREEN)
    screen.blit(display_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
