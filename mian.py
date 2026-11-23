#.............project bot...................
chat_bot: str = 'john'
print(f'hey yoo I\'m {chat_bot}! what is on your mind?')

while True:

    user_input: str = input('you: '). lower()

    if user_input in ['hi','hello','good moring','good after noon','good evening']:
        print(f'{chat_bot}: HI there, how can i help you to day')
    elif user_input in ['bye','see you','goodbye']:
        print(f'{chat_bot}: goodbye, have a nice day')
    elif user_input in ['let\'s two numbers','add','+','could you do some addtion']:
        print(f'{chat_bot}: sure! let add two numbers. enter the two numbers')
        try:
            num1:float = float(input('first number: '))
            num2:float = float(input('second number: '))
            print(f'{chat_bot}: that is actually easy, it {num1+num2}')
        except ValueError:
            print(f'{chat_bot}: I don\'t thnk thas a ')
    elif user_input in ['les\'s subtract two numbers','-','minus','subtract']:
        print(f'{chat_bot}: OK les\'s subtract. please enter the two numbers')
        try:
            num3:float = float(input('first number: '))
            num4:float = float(input('second number: '))
            print(f'{chat_bot}: OK! , is {num3-num4}')
        except ValueError:
            print(f'{chat_bot}: I don\'t thnk thas a ')
    elif user_input in ['multiplay','*',]:
        print(f'{chat_bot}: please enter the two numbers')
        try:
            x:float = float(input('first number'))
            y:float = float(input('second number'))
            print(f'{chat_bot} : sure! {x}*{y} is {x*y}')
        except ValueError:
            print(f'{chat_bot}: Hmmm, i can\'t multiplay that!')
    elif user_input in ['divide','/','lets divid two numbers']:
        print(f'{chat_bot}:sure enter the numbers you want to divide!') 
             
        try:
            a:float = float(input('first number: '))
            b:float = float(input('second number: '))

            print(f'{chat_bot}: ofcoures! it is {a / b}')
        except ZeroDivisionError: 
                print(f'{chat_bot}:  you can not divide a number by zero')
        except ValueError:
                print(f'{chat_bot}: I can not divide this number please try again!!')
    elif user_input in ['thanks','thankyou','thanks for the assiast','thanks for the support']:
        print(f'{chat_bot}:you are very wlecome1q, nice chat bro!')
    elif user_input in ['let\'s talk','wanna talk','you wanna talk','you want to talk','let us talk','talk']:
        print(f'{chat_bot}: feeling lonely! ok let\'s talk, what do you want to talk about')
        print('   about:')
        print('     a : greeting and casual conversation with me')
        print('     b : icebreaker and some questions to test you IQ level')
        print('     c : most popular games')
        print('     d : laptop recomendation')
        print('     e : movie recomendation')
        users = []
        word =[]
        user_input = input( 'you: ')
        match user_input. lower():
            case 'a':
                print(f'{chat_bot}: OK! then greeting it is, HI i\'m chat_bot goes by the name of John, and you?')
                user_name = input('you: ')
                users.append(user_name)
                if user_name in [f'Hi john i\'m {user_name}',f'I\'m {user_name} ',f'{user_name}']:
                    print(f'{chat_bot}: hi {user_name},nice to meet you!')
                else:
                    print(f'{chat_bot}: hi {user_name},nice to meet you!')
            case 'b':
                print(f'{chat_bot}: Ok! here is a simple icebreaker.what is the longest word in english language')
                user_anser = input('you ')
                word.append(user_anser)
                if user_anser == 'smiles' :
                    print(f'{chat_bot}: correct you got it :)') 
                else:
                    print(f'{chat_bot}: it is not {user_anser}, It is smiles :)')
            case 'c':
                print(f'{chat_bot}: so you are in to games. what kind of game do you like??')
                print('shooting , fighting, open world.tell me and i will list them.')
                game = []
                user_input = input('you :')
                match user_input. lower():
                    case 'shooting':
                        print(f'{chat_bot}: OK! Here are the most popular shooting games')
                        print('''                         1. PUBG BATTLEGROUNDS
                                   2. Call of Duty 
                                   3. Blood strike
                                   4. Apex legend
                                   5. combat master''')
                        user_game = input('you: ')
                        game.append(user_game)
                        print(f'nice! you can dowload {user_game} on Steam,but first cheak the reqiuerments')
                    case 'fighting':
                        print(f'{chat_bot}: Sure!')
                        print('''   1. Tekken 8
                        2. street fighter 6
                        3. God Of War
                        4. dragon ball super
                        5. king of fighters ''')
                        user_game = input('you: ')
                        game.append(user_game)
                        print(f'{chat_bot}: Hard to choose huh? you can get {user_game} on steam,but playing those games is not easy')
                    case 'open world':
                        print(f'{chat_bot}: you can live your life in :')
                        print('''   1.red dead redumption 2
                        2. GTA 5/4
                        3. assasin\'s creed:
                        4. whatch dogs
                        5. mine craft''')
                        user_game = input('you: ')
                        game.append(user_game)
                        print(f'{chat_bot}: My recomendation is GTA san andres,but if you want you can download {user_game} on steam')
            case 'd':
                print(f"{chat_bot}: What kind of laptop are you looking for?")
                print("gaming, school, programming, business")
                laptop_type = input("you: ").lower()

                match laptop_type:
                    case "gaming":
                     print(f'{chat_bot}: so you are very into games')
                     print("- ASUS TUF Gaming")
                     print("- Acer Nitro 5")
                     print("- Lenovo Legion 5")

                    case "school":
                     print(f"{chat_bot}: Recommended laptops:")
                     print("- Dell Inspiron")
                     print("- HP Pavilion")
                     print("- Lenovo IdeaPad")

                    case "programming":
                     print(f"{chat_bot}: Recommended laptops:")
                     print("- Lenovo ThinkPad")
                     print("- Dell XPS")
                     print("- MAC BOOK AIR")

                    case "business":
                     print(f"{chat_bot}: Recommended laptops:")
                     print("- Lenovo ThinkPad")
                     print("- HP EliteBook")
                     print("- Dell Latitude")

                    case _:
                     print(f"{chat_bot}: Sorry, I don't have recommendations for that category.")
            case 'e':
                print(f'{chat_bot}: what kind of movie do ypu like?')
                print('action, comedy, sci-fi,horror')

                movie_type = input('you: '). lower()
                match movie_type:
                    case 'action':
                        print(f'{chat_bot}here are so action movies you might like:')
                        print('    1. john wick')
                        print('    2. Mission: impossible')
                        print('    3  ninja turtle')
                    case 'comedy':
                        print(f'{chat_bot}: here are Top 3 comedy movies that will make you laught hard!')
                        print('    1. Home Alone')
                        print('    2. Mr. Bean')
                        print('    3. The Mask')
                    case 'sci-fi':
                        print(f'{chat_bot}: Here are some sfi-fi Movies you might like:')
                        print('    1. Interstellar')
                        print('    2. The Martian')
                        print('    3. Avatar')
                    case 'horror':
                        print(f'{chat_bot}: OK! Here are horror Movies you might like to see')
                        print('    1. The Conjuring')
                        print('    2. Insidious')
                        print('    3. A Quiet Place')
    elif user_input in ['could you make a simple game with python coding','make a simple game code','make a game']:
        print(f'{chat_bot}: sure here is a simple sneake game code')
        print('''
import pygame 
import random
pygame.init()
B = (0, 0, 0)
G = (0, 255, 0)
R = (255, 0, 0)
W = (255, 255, 255)

#screen setting
WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK, BLOCK])


def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])


def game():
    snake = [[100, 100]]
    dx = BLOCK
    dy = 0

    food_x = random.randrange(0, WIDTH, BLOCK)
    food_y = random.randrange(0, HEIGHT, BLOCK)

    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK
                    dy = 0
                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = -BLOCK
                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = BLOCK

        head_x = snake[0][0] + dx
        head_y = snake[0][1] + dy

        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            running = False

        snake.insert(0, [head_x, head_y])

        if head_x == food_x and head_y == food_y:
            score += 1
            food_x = random.randrange(0, WIDTH, BLOCK)
            food_y = random.randrange(0, HEIGHT, BLOCK)
        else:
            snake.pop()

        if snake[0] in snake[1:]:
            running = False

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK, BLOCK])
        draw_snake(snake)
        show_score(score)

        pygame.display.update()
        clock.tick(10)

    print("Game Over! Score:", score)
    pygame.quit()


game()

''')
        print(f'{chat_bot}: you should download a game vesion of coding to make this work like pygame which is used in this code')
    else :
        print(f'{chat_bot}: I didn\' understand that ,please try again ')