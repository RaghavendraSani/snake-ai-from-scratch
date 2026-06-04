class RuleAgent:
    def get_action(self, state):
        food_left = state[4]
        food_right = state[5]
        food_up = state[6]
        food_down = state[7]

        if food_right:
            return 1
        elif food_left:
            return 0
        elif food_up:
            return 2
        elif food_down:
            return 3

        return 1