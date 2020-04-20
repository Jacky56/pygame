import pygame


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    running = True

    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        #pygame.draw.circle(screen, (0, 0, 255), (100, 100), 50)

        i += 1
        pygame.draw.arc(screen, (0, 0, 255), pygame.Rect(10, 10, 100, 100), i, i+100, 19)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

