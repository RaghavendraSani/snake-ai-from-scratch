import pygame
import random

class SnakeGame:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 600, 400
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake AI")

        self.clock = pygame.time.Clock()

        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50]]
        self.snake_size = 10

        self.direction = "RIGHT"

        self.food_pos = [random.randrange(0, self.WIDTH, 10),
                         random.randrange(0, self.HEIGHT, 10)]

        self.food_size = 10
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 20)

    def run (self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            action = 1
            state, food, reward, done = self.step(action)
            state = self.get_state()

            if done:
                self.reset()

            # drawing:

            # screen
            self.screen.fill((0, 0, 0))

            # snake body
            for block in self.snake_body:
                pygame.draw.rect(self.screen, (0, 255, 0),
                                 (block[0], block[1], self.snake_size, self.snake_size))

            # food
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (self.food_pos[0], self.food_pos[1], self.food_size, self.food_size))

            # score
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            # update
            pygame.display.update()

            self.clock.tick(10)

        pygame.quit()

    def step(self, action):
        reward = -1
        done = False

        #set direction
        if action == 0:
            self.direction = "LEFT"
        elif action == 1:
            self.direction = "RIGHT"
        elif action == 2:
            self.direction = "UP"
        elif action == 3:
            self.direction = "DOWN"

        #move
        if self.direction == "RIGHT" and self.direction != "LEFT":
            self.snake_pos[0] += 10
        elif self.direction == "LEFT" and self.direction != "RIGHT":
            self.snake_pos[0] -= 10
        elif self.direction == "UP" and self.direction != "DOWN":
            self.snake_pos[1] -=10
        elif self.direction == "DOWN" and self.direction != "UP":
            self.snake_pos[1] += 10

        #body update
        self.snake_body.insert(0, list(self.snake_pos))
        self.snake_body.pop()

        #food collision
        if self.snake_pos == self.food_pos:
            self.snake_body.append(list(self.snake_body[-1]))
            self.food_pos = [random.randrange(0, self.WIDTH, 10),
                             random.randrange(0, self.HEIGHT, 10)]
            self.score += 1
            reward = 10

        #wall collision
        if (self.snake_pos[0] <0 or
                self.snake_pos[0] >= self.WIDTH or
                self.snake_pos[1] < 0 or
                self.snake_pos[1] >= self.HEIGHT):
            reward = -10
            done = True

        #self collision
        for block in self.snake_body[1:]:
            if block == self.snake_pos:
                reward = -10
                done = True

        return self.snake_pos, self.food_pos, reward, done


    def reset(self):
        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50]]
        self.direction = "RIGHT"

        self.food_pos = [random.randrange(0, self.WIDTH, 10),
                         random.randrange(0, self.HEIGHT, 10)]
        self.score = 0

    def get_state(self):
        left_pos = [self.snake_pos[0] - 10, self.snake_pos[1]]
        right_pos = [self.snake_pos[0] + 10, self.snake_pos[1]]
        up_pos = [self.snake_pos[0], self.snake_pos[1] - 10]
        down_pos = [self.snake_pos[0], self.snake_pos[1] + 10]

        danger_left = (left_pos[0] < 0 or left_pos in self.snake_body)
        danger_right = (right_pos[0] >= self.WIDTH or right_pos in self.snake_body)
        danger_up = (up_pos[1] < 0 or up_pos in self.snake_body)
        danger_down = (down_pos[1] >= self.HEIGHT or down_pos in self.snake_body)

        food_left = self.food_pos[0] < self.snake_pos[0]
        food_right = self.food_pos[0] > self.snake_pos[0]
        food_up =self.food_pos[1] < self.snake_pos[1]
        food_down = self.food_pos[1] > self.snake_pos[1]

        return [danger_left, danger_right, danger_up, danger_down, food_left, food_right, food_up, food_down]












