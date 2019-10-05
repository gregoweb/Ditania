# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    $ mind_color = renpy.random.choice(['black','white'])
    "What's just happened everything's %(mind_color)s in my head"
    "I can't remember anything, who am I ? At less im feeling like a "
    menu:
        "girl":
            jump girl
        "boy":
            jump boy
        "cloud":
            jump cloud
    label girl:
        $ player_genre = "girl"
        jump genreSelected
    label boy:
        $ player_genre = "boy"
        jump genreSelected
    label cloud:
        $ player_genre = "cloud"
    
    label genreSelected:

    $ player_name = renpy.input("What's my name ?")
    $ player_name = player_name.strip()
    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name="Akira"
    e "Pleased to meet you young %(player_genre)s, %(player_name)s!"

    # This ends the game.

    return
