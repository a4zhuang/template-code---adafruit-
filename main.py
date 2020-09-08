def LED_loop():
    global remaining_button_presses, continue_game
    while remaining_button_presses > 0:
        for index in range(10):
            light.set_pixel_color(index, 0xff0000)
            pause(randint(25, 150))
            if input.button_a.is_pressed():
                if index == 2:
                    print("Button A correct push!")
                    music.power_up.play()
                    light.show_animation(light.rainbow_animation, 1000)
                    light.set_all(0xffffff)
                    remaining_button_presses += 1
                else:
                    print("Button A incorrect push!")
                    music.power_down.play()
                    light.set_all(0xffffff)
                    pause(1000)
                remaining_button_presses += -1
                break
            light.set_pixel_color(index, 0xffffff)
        continue_game = False
def show_result(correct_presses: number):
    console.log_value("Your Score", correct_presses)
    for index_2 in range(10):
        if 0 > 0:
            light.set_pixel_color(index_2, 0x00ff00)
            correct_presses += -1
    pause(5000)
    light.set_all(0xffffff)
correct_presses = 0
continue_game = False
remaining_button_presses = 0
remaining_button_presses = 10
correct_button_presses = 0
continue_game = True

def on_forever():
    global correct_button_presses, remaining_button_presses, continue_game
    if continue_game == True:
        LED_loop()
    else:
        show_result(correct_presses)
        correct_button_presses = 0
        remaining_button_presses = 10
        continue_game = True
forever(on_forever)
