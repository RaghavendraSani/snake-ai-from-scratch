class RuleAgent:
    def get_action(self, state):
        danger_left = state[0]
        danger_right = state[1]
        danger_up = state[2]
        danger_down = state[3]

        food_left = state[4]
        food_right = state[5]
        food_up = state[6]
        food_down = state[7]

        if food_right and not danger_right:
            return 1
        elif food_left and not danger_left:
            return 0
        elif food_up  and not danger_up:
            return 2
        elif food_down and not danger_down  :
            return 3

        return 1