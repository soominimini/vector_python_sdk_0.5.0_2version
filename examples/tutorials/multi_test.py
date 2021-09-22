import anki_vector

if __name__ == '__main__':

    with anki_vector.Robot() as robot:
        print() # Will print ControlPriorityLevel.DEFAULT_PRIORITY
        robot.conn.release_control()
        print(robot.conn.behavior_control_level) # Will print None