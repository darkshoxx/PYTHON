import os
import time
import keyboard


def cls():
    os.system('cls')


speed = 0.5  # seconds per cycle
update_resolution = 20  # number of button checks per sleep cycle


# Function not used anymore

# def fill_binary(bin_str):
#    num = len(bin_str)
#    print(num)
#    if num < 8:
#        buffer = (8 - num) * '0'
#        return buffer + bin_str
#    else:
#        return bin_str[(num - 8):]


def engine(fastness, resolution):  # increase update resolution if game doesn't take inputs

    start_byte = '00000001'
    cursor_list = ['^<------', '>^<-----', '->^<----', '-->^<---',
                   '--->^<--', '---->^<-', '----->^<', '------>^']  # Cursor style is picked
    # from this list
    cursor_start_index = 7
    cursor_index = cursor_start_index
    byte = start_byte[:]
    # Flags that check if a button has been pressed
    space_pressed = False
    left_key_pressed = False
    right_key_pressed = False
    # Running the game consists of 1. act on buttons, 2. test for game over
    # 3. Updating bit & Cursor 4. test buttons
    while True:
        # 1 Act on button presses 'space', 'left', 'right'
        if space_pressed:
            # Kill the Bit that is there
            if byte[cursor_index] == '1':
                new_string = ''
                new_string += byte[:cursor_index]
                new_string += '0'
                new_string += byte[(cursor_index + 1):]
                byte = new_string[:]
                space_pressed = False
            # Create a bit where there was none
            else:
                new_string = ''
                new_string += byte[:cursor_index]
                new_string += '1'
                new_string += byte[(cursor_index + 1):]
                byte = new_string[:]
                space_pressed = False
        # Move Cursor left/right
        if left_key_pressed:
            if cursor_index != 0:
                cursor_index -= 1
        if right_key_pressed:
            if cursor_index != 7:
                cursor_index += 1
        # 2. Is the game over?
        if byte == '00000000':
            print("A WINNER IS YOU")
            return None
        if byte == '11111111':
            print("LOL YOU DIE")
            return None
        # 3. Updating Cursor, rolling over the bit(s)
        cursor = cursor_list[cursor_index]
        left_key_pressed = False
        right_key_pressed = False
        if byte[0] == '1':
            byte = byte[1:8] + '1'
        else:
            byte = byte[1:8] + '0'
        print(f"{byte}\n{cursor}")
        # 4. Checking for Keyboard inputs. Won't be accepted DURING sleep, so chuck up sleep into
        # Update intervals of given resolution.
        for i in range(0, resolution):
            if keyboard.is_pressed(' '):  # if key ' ' is pressed
                space_pressed = True
            if keyboard.is_pressed('left arrow'):  # if key '->' is pressed
                left_key_pressed = True
            if keyboard.is_pressed('right arrow'):  # if key '<-' is pressed
                right_key_pressed = True
            time.sleep(fastness / resolution)
        # Clear screen, so print is always in the same lines.
        cls()


engine(speed, update_resolution)
