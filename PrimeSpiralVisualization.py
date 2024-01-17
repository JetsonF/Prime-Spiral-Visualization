# In terminal, "pip install pygame"
import pygame
import sys

# Initialize
pygame.init()

# Set up display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spiral Visualization of Prime Numbers (Clockwise and Outward, 0 at Center)")

# Define colors
color_bckgrnd = (29, 43, 83)
color_nonprime = (126, 37, 83)
color_prime = (255, 0, 77)
color_zero = (0, 0, 0)

# Determine if a number is a prime
def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return False
    elif number % 2 == 0:
        return False
    else:

        # Check for factors up to the square root of the number
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
    return True

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Color background
    screen.fill(color_bckgrnd)

    # Define squares
    side = 4
    center_x = (width/2) - (side/2)
    center_y = (height/2) - (side/2)
    pos_x = center_x
    pos_y = center_y

    # Define Current Number, the number representing each square
    Current_Number = 0

    # Draw squares
    pygame.draw.rect(screen, color_zero, (center_x, center_y, side, side))

    # Defines how many side lengths the spiral iterates for
    iterations = 201

    # Actually run the code
    for n in range(iterations):
        if ((n+1)%2==1):
            # moves box left
            for m in range (n+1):
                pos_x -= side
                Current_Number += 1
                if (is_prime(Current_Number)):
                    pygame.draw.rect(screen, color_prime, (pos_x, pos_y, side, side))
                else:
                    pygame.draw.rect(screen, color_nonprime, (pos_x, pos_y, side, side))
            # moves box up
            for m in range (n+1): 
                pos_y -= side
                Current_Number += 1
                if (is_prime(Current_Number)):
                    pygame.draw.rect(screen, color_prime, (pos_x, pos_y, side, side))
                else:
                    pygame.draw.rect(screen, color_nonprime, (pos_x, pos_y, side, side))
                
        else: 
            # moves box right
            for m in range (n+1):
                pos_x += side
                Current_Number += 1
                if (is_prime(Current_Number)):
                    pygame.draw.rect(screen, color_prime, (pos_x, pos_y, side, side))
                else:
                    pygame.draw.rect(screen, color_nonprime, (pos_x, pos_y, side, side))
            # moves box down
            for m in range (n+1): 
                pos_y += side
                Current_Number += 1
                if (is_prime(Current_Number)):
                    pygame.draw.rect(screen, color_prime, (pos_x, pos_y, side, side))
                else:
                    pygame.draw.rect(screen, color_nonprime, (pos_x, pos_y, side, side))

    # Update display
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()