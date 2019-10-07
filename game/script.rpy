# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Emperess")
define s = Character("Sarah")

# The game starts here.

label start:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    $ mind_color = renpy.random.choice(['black','white'])
    "What's just happened everything's %(mind_color)s in my head"
    play music "dunes.mp3" fadeout 1.0 fadein 1.0
    "I can't remember anything"
    "I'm feeling cold, let's open my eyes"
    scene bgdunes
    "It's look's like a desert here the place will soon been hot"
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
    "Well I am a proud %(player_genre)s ! Let's look around"
    scene bgburningship
    play music "fear.mp3" fadeout 1.0 fadein 1.0
    "Wow a spaceship is burning ! Could it be my Spaceship ?"
    "But wait someone's comming"
    play music "havefun.mp3" fadeout 1.0 fadein 1.0
    "it's look's like a girl and she is alone, what i am gonna do ?"
    menu:
        "Making love to her, she will thanks me for that":
            jump rapeGirl
        "Trying to ask for help":
            jump helpme
    label rapeGirl:
        #path RebelBoy
        # Jail in world ruled by girls
        # Escaped by RebelBoys
        # Destroy palace of Girlpower with your repaired ship
        "As soon as you get behind the girl to try to remove her clothes,"
        play music "fear.mp3" fadeout 1.0 fadein 1.0
        "The girl scream loudly and a squad of 6 girls in armor come at the speed of light with a landspeeder"
        "You don't have time to escape and soon the girls controll you"
        label prisoner:
        "Girls in armor tie you with metal chains and put a blindfold on your eyes"
        scene black
        "[Girl guard]" "You will be put in jail xeno %(player_genre)s!"
        "[Girl guard]" "Let's go Girls"
        play music "dunes.mp3" fadeout 1.0 fadein 1.0
        "After a short drive of maybe 2km the speeder brutally stop"
        "[Man voice]" "You are surrounded, Get out of the speeder !"
        "[Man voice]" "Let the %(player_genre)s free and we won't shot at you anymore !"
        "[Girl guard]" "We are outnumbered Let's go Girls, Let's run for our lives"
        "[Girl guard]" "There's no point to die, for this prissoner we will revenge later"
        "[Man voice]" "Ok GUYS take this poor oppressed %(player_genre)s to our secret rebel base"
        "After a long drive of maybe 3 hours, you've been put in a room a man free you from chains and blindfold"
        scene bgdunes
        "[Man]" "Hello %(player_genre)s! I am Balrog the chief of Rebelboyz. What's your name ? "
        $ player_name = renpy.input("What's my name ?")
        $ player_name = player_name.strip()
        #  If the player can't be bothered to choose a name, then we
        #  choose a suitable one for them:
        if player_name == "":
            $ player_name="Akira"
        "[Balrog]" "Welcome here %(player_name)s you are on planete Ditania in our secret Rebelboyz base"
        "[Balrog]" "We see you eject from a spaceship, and I think we can help you"
        "[Balrog]" "We were looking at you with our binocular and we see your unconventionnal way to rule the girls"
        "[Balrog]" "We could repair your spaceship, if you accept to help us in our rebelion against girl power"
        "[Balrog]" "We want you to shoot the palace of Girlpower with your spaceship"
        "[Balrog]" "This will garantee our chances to rules Ditania. Will you do that ?"
        menu:
            "Yes":
                jump endRebelBoysWin
            "No":
                "[Balrog]" "As you wish we will put you back to the palace of the girl power where you remain to be"
                jump endSlave
    label helpme:
        #path Powered Girl
        # Go to palace of Girlpower
        # convince to put all mens in jail to control their uncontralable nature
        # final fight against rebels with your repaired ship

        #path harmony
        # Go to palace of Girlpower
        # Convince to live in harmony with RebelBoys 
        # To thanks for restoration of peace Boys and Girlz repair your ship 
        scene bgdunes
        play music "dunes.mp3" fadeout 1.0 fadein 1.0
        "[Girl]" "Hello beautiful %(player_genre)s, my name is Sarah What's your name ?"

        $ player_name = renpy.input("What's my name ?")
        $ player_name = player_name.strip()
        #  If the player can't be bothered to choose a name, then we
        #  choose a suitable one for them:
        if player_name == "":
            $ player_name="Akira"
        s "I am pleased to meet you %(player_name)s"
        s "I see you are looking for help, I'll take you to the palace of Girlpower"
        scene pgpower
        s "Holy revered Empress of Girl Power. I bring back to you a %(player_genre)s named %(player_name)s looking for our help"
        e "Hi little %(player_genre)s, what kind of help do you need ?"
        menu:
            "Holy revered Empress, Could I be your slave for the rest of my insignificant life ?":
                jump endSlave
            "Could you help me repair my ship ?":
                e "Yes we might consider helping you but we can't waste ressources during the stupid men's rebelion that we are facing."
                e "What do you offer in exchange ?"
                "[player_name]" "Let me think..."
                "[player_name]" "Well I can offer you my"
                menu:
                    "Help to kill the men's Rebellion":
                        jump endGirlsWin
                    "Help to resolve the crisis peacefully by drafting egalitarian law for women, men and all small clouds":
                        jump endHarmony
                    "Help to find the true pleasure deep inside your intimity":
                        e "How dare you ! Guards take this insolant thing out of my sight"
                        jump prisoner

    label endRebelBoysWin:
        scene pgpxplode1
        "As soon as your brother in arm repaired your spaceship you flight toward the palace of Girl power "
        "and you shoot 2 proton torpedo to get your revenge against the humilliations you suffer from girls of Ditania"
        scene pgpxplode2
        play music "havefun.mp3" fadeout 1.0 fadein 1.0
        "Congratulation %(player_name)s you've destroyed the palace of Girlpower"
        "Mens will finnally be totally free here in Ditania !"
        jump end
    label endGirlsWin:
        scene pgpower
        play music "havefun.mp3" fadeout 1.0 fadein 1.0
        "Congratulation %(player_name)s you've finnaly killed this insignificant men's rebellion"
        "Girl power will rule Ditania forewer !"
        jump end
    label endHarmony:
        scene harmony
        play music "havefun.mp3" fadeout 1.0 fadein 1.0
        "Congratulation %(player_name)s you help the inhabitants of Ditania to live together in equality, peace and harmony"
        jump end
    
    label endSlave:
        scene pgpower
        play music "fear.mp3" fadeout 1.0 fadein 1.0
        "You've been imprisoned for life and treated like a slave by girls of Ditania"
    label end:
        "THE END"
        "Thanks fo playing %(player_name)s, try again to see diferents ends"

    # This ends the game.

    return
