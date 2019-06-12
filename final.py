# coded in utf-8
import random
import io


def Main():
    cont = 1
    while cont == 1:
        cont = game()


def game():
    print(
        "You awaken in a haze, unaware of where you are you cast about and find a mirror. you look into the mirror. \n \
    what do you see? push 1 for warrior, 2 for mage, 3 for rogue"
    )

    character_select = int(input())
    if character_select == 1:
        character = player(20, 6, "warrior")
    elif character_select == 2:
        character = player(1, 1, "mage")
    else:
        character = player(13, 13, "rogue")
    print("Welcome young" + character.name + " your adventure begins now")
    print(
        "you start your journey in a haze, walking through the depth of a forrest until you come to a fork. to one side \n \
         you hear screaming, yet down the other fork you sense a serinity, it appears safe. press 1 to go toward the screaming, any other key to take the other path"
    )
    user_input = int(input())
    if user_input == 1:
        print(
            "you march towards the screams, your path is set, \n \
            you come around a bend to see a massive rat snarling at you, you dont see the source of scream - but the rat charges you "
        )
        rat = characters(5, 5, "rat")
        print(
            "you see the beast approaching, press 1 to FIGHT, any other key to run away- this will end your adventure"
        )
        user_input = int(input())
        if user_input == 1:
            result = combat(character, rat)
            if result != 2:
                return result
            print(
                "YOU ARE VICTORIUS! \n \
                a small figure appraoaches you, the head of a ant - and the body of a monkey.\n \
                the creature lets loose a whoop!the creature tells you that there is a treasure for your reward just down the road "
            )
        else:
            character.run_away()
        print(
            "you stumble your way in the diretion of the supposed loot, as you round the bend you see a massive chest, presumbly full of treasure.\n \
                you notice there are many small creatures surrounding the loot, they apear to be worshiping it, \n \
                what do you wish to do?, press 1 to take the loot,  or any other key to walk away and find adventure in another area."
        )
        user_choice = int(input())
        if user_choice == 1:
            print(
                "the pygmy like creatures charge you, there are dozens of them, swarmin you at ankle height"
            )
            pygmy = characters(10, 3, "pygmy")
            if (combat(character, pygmy)) == 0:
                return 0
            print(
                "dozens of small little creatures lay littered on the ground, you approach the chest and steal its content \n \
            a fistful of rubies is now yours, and you continue down the path"
            )

        print(
            'with your head held high you continue down the path, you see, eronate door, you approach\n \
            upon the door is ancient writing below it says " is this a palidrome? if you answer wrong- magic will kill you" enter [Y/N]'
        )
        puzzle_number = 12321
        print(str(puzzle_number))
        user_input = input()
        if user_input == "Y" and is_palindrome(puzzle_number):
            pass
        else:
            death(character)
        print(
            "the door opens, a strong musky wind overcomes you as you hear a distant roar, do you continue? push 1 to continue any other key to end your adventure"
        )
        user_input = int(input())
        if user_input == 1:
            print(
                "you charge down the tunnel toward the roar, and are confronted with a massive red dragon, do you want to engage? \n \
                press 1 to fight the dragon for the hoard, any other key to run away- RUN AWAY YOU WILL DIE-probably"
            )
            user_input = int(input())
            if user_input == 1:
                dragon = characters(100, 15, "dragon")
                result = combat(character, dragon)
                if result != 2:
                    death(character)
                else:
                    final_ending()

            else:
                character.run_away()

        else:
            happy_ending()
    # 1st split path
    return 2


def dice_roll(max_value):
    return random.randint(1, max_value)


class characters:
    def violence(self, target):
        roll = dice_roll(self.damage)
        if roll == 1:
            print(self.name + "suffers a critical failure!")
            return death(self)
        elif roll == self.damage:
            print(self.name + " strikes a critical sucess!")
            return death(target)
        else:
            print(self.name + " hits " + target.name + " for " + str(roll))
            target.health -= roll

    def __init__(self, health=20, damage=6, name="default"):
        self.health = health
        self.damage = damage
        self.name = name


def damage_taken():
    damage_taken = [
        "You take a mighty blow from the enemy, you stagger back from the pain",
        "The enemy strikes a fierce blow to you, you gasp from the pain",
        "You see the whites of your enemies eyes as he approaches- weapon raised high for  vigorous strike, you shrink back from the pain from the blow \n \
         the enemy tackles you, you drop to the ground and your head hits the rock",
        "The enemy lets out a fierce below as they aim a strike at your body, you take the blow squarly to the chest",
    ]
    return damage_taken[random.randint(1, len(damage_taken) - 1)]


def damage_given():
    damage_given = [
        "You let out a massive scream as you raise your weapon to strike!, you land a mighty blow and the enemy staggers back/n",
        "you let out a cry of passion as you charge the enemy, your weapon forcing the enemy to their knees in pain, you see the fear in their eyes/n",
        "you jump up in the air doing a crazy spinny attack, the barbarian whirlwind you call it, you clip the enemy and he lets our a cry of pain/n",
        "your blow lands squary on your enemy, your scream of passion lends strength to your strike",
    ]
    return damage_given[random.randint(1, len(damage_given) - 1)]


# class art:
# inside test file

# class config:
# save/load


# class puzzle:
# will see a number, user selects true or false if the number is a palindrone.
def is_palindrome(number):

    if isinstance(number, int):
        number = abs(number)
    try:
        int(number)
    except ValueError:
        raise ValueError
    number = str(number)
    if len(number) <= 1:
        return True
    if number[0] == number[-1]:
        return is_palindrome(number[1:-1])
    return False


class player(characters):
    def __init__(self, health, damage, name):
        super().__init__(health, damage, name)
        self.max_health = health

    def run_away(self):
        print(
            "You realize you are a utter coward and the beat before you frightens you \n \
            you turn your back, and run with everything you have, you feel your pants wet \n \
            from were you peed yourself in fear, you find a safe spot to hide and cry"
        )
        death(self)


def death(actor):
    actor.health == 0
    if type(actor) == player:
        LOSS_LIST = [
            "YYYYYYY       YYYYYYY     OOOOOOOOO     UUUUUUUU     UUUUUUUU     LLLLLLLLLLL                  OOOOOOOOO        SSSSSSSSSSSSSSS EEEEEEEEEEEEEEEEEEEEEE",
            "Y:::::Y       Y:::::Y   OO:::::::::OO   U::::::U     U::::::U     L:::::::::L                OO:::::::::OO    SS:::::::::::::::SE::::::::::::::::::::E",
            "Y:::::Y       Y:::::Y OO:::::::::::::OO U::::::U     U::::::U     L:::::::::L              OO:::::::::::::OO S:::::SSSSSS::::::SE::::::::::::::::::::E",
            "Y::::::Y     Y::::::YO:::::::OOO:::::::OUU:::::U     U:::::UU     LL:::::::LL             O:::::::OOO:::::::OS:::::S     SSSSSSSEE::::::EEEEEEEEE::::E",
            "YYY:::::Y   Y:::::YYYO::::::O   O::::::O U:::::U     U:::::U        L:::::L               O::::::O   O::::::OS:::::S              E:::::E       EEEEEE",
            "  Y:::::Y Y:::::Y   O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::OS:::::S              E:::::E             ",
            "   Y:::::Y:::::Y    O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O S::::SSSS           E::::::EEEEEEEEEE   ",
            "    Y:::::::::Y     O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O  SS::::::SSSSS      E:::::::::::::::E   ",
            "      Y:::::::Y      O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O    SSS::::::::SS    E:::::::::::::::E   ",
            "       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O       SSSSSS::::S   E::::::EEEEEEEEEE   ",
            "       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U        L:::::L               O:::::O     O:::::O            S:::::S  E:::::E             ",
            "       Y:::::Y       O::::::O   O::::::O U::::::U   U::::::U        L:::::L         LLLLLLO::::::O   O::::::O            S:::::S  E:::::E       EEEEEE",
            "        Y:::::Y       O:::::::OOO:::::::O U:::::::UUU:::::::U      LL:::::::LLLLLLLLL:::::LO:::::::OOO:::::::OSSSSSSS     S:::::SEE::::::EEEEEEEE:::::E",
            "     YYYY:::::YYYY     OO:::::::::::::OO   UU:::::::::::::UU       L::::::::::::::::::::::L OO:::::::::::::OO S::::::SSSSSS:::::SE::::::::::::::::::::E",
            "     Y:::::::::::Y       OO:::::::::OO       UU:::::::::UU         L::::::::::::::::::::::L   OO:::::::::OO   S:::::::::::::::SS E::::::::::::::::::::E",
            "      YYYYYYYYYYYYY         OOOOOOOOO           UUUUUUUUU           LLLLLLLLLLLLLLLLLLLLLLLL     OOOOOOOOO      SSSSSSSSSSSSSSS   EEEEEEEEEEEEEEEEEEEEEE",
        ]
        print(
            "You see the angels of valhalla comeing for your soul, yet they give you a chance to start again, would you like to try again? \
        press 1 to try your restart the game, press any other key to quite"
        )
        file = io.open("yousuck.txt", "w", encoding="utf-8")
        for line in LOSS_LIST:
            file.write(line + "\n")
        file.close()
        user_choice = int(input())
        if user_choice == 1:
            return 1
        else:
            return 0
    return 2


def combat(mainchar, enemy):
    while enemy.health > 0 and mainchar.health > 0:
        print(mainchar.name + ": " + str(mainchar.health))
        print(enemy.name + ": " + str(enemy.health))
        mainchar.violence(enemy)
        print(damage_given())
        if enemy.health <= 0 or mainchar.health <= 0:
            break
        enemy.violence(mainchar)
        print(damage_taken())
    if mainchar.health >= 0:
        mainchar.health = mainchar.max_health
        return death(enemy)
    return death(mainchar)


def happy_ending():
    print("Congratulations you have survived your journey, now you may rest")
    return 2


def final_ending():
    print(
        "the dragon falls, you are the mightest of heroes. the dragon hoard is now yours, as is his magic. THE END"
    )
    return 2


Main()
