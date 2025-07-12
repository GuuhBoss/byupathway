print("My 1st friend enjoyed the game, said it was fun and engaging!")
print("My 2nd friend also liked, and said it was a great adventure!")

print("""
🌲 Welcome to The Enchanted Forest Mystery! 🌲
==================================================
You are a brave adventurer who has stumbled upon a mysterious glowing path
leading deep into an ancient forest. Strange sounds echo from within, and
you notice three distinct paths branching ahead of you...

As you approach the fork in the path, you see:
- A BRIGHT path glowing with golden light
- A DARK path shrouded in purple mist
- A NARROW path winding between ancient oak trees
""")
print()

# First level choice
while True:
    first_choice = input("Which path do you choose? (BRIGHT/DARK/NARROW): ").upper()
    if first_choice == "BRIGHT" or first_choice == "DARK" or first_choice == "NARROW":
        break
    print("Please choose a valid path: BRIGHT, DARK, or NARROW.")

if first_choice == "BRIGHT":
    print("""
    🌟 You walk down the bright golden path...
    The light grows stronger as you progress, and suddenly you find yourself
    in a beautiful clearing where a majestic unicorn stands by a crystal pond.
    The unicorn speaks: 'Brave traveler, I can grant you a gift, but choose wisely!'
    
    The unicorn offers you three magical items:
    - A SWORD that glows with inner fire
    - A SHIELD that reflects all magic
    - A POTION that grants temporary flight
    """)
    print()

    while True:
        second_choice = input("What do you choose? (SWORD/SHIELD/POTION): ").upper()
        if second_choice == "SWORD" or second_choice == "SHIELD" or second_choice == "POTION":
            break
        print("Please choose a valid item: SWORD, SHIELD, or POTION.")

    if second_choice == "SWORD":
        print("""
        ⚔️ You take the glowing sword...
        As you grasp it, the blade erupts in flames! Suddenly, a dragon emerges
        from behind the trees, drawn by the sword's power.
        'That blade was stolen from me long ago!' the dragon roars.
        
        The dragon blocks your path. You must:
        - FIGHT the dragon with your new sword
        - NEGOTIATE and offer to return the sword
        """)
        print()

        while True:
            third_choice = input("What do you do? (FIGHT/NEGOTIATE): ").upper()
            if third_choice == "FIGHT" or third_choice == "NEGOTIATE":
                break
            print("Please choose a valid action: FIGHT or NEGOTIATE.")

        if third_choice == "FIGHT":
            print("""
            🔥 You raise the flaming sword and charge!
            The battle is fierce, but the sword's power overwhelms the dragon.
            As the dragon falls, it transforms into a wise old wizard.
            'You have proven your courage,' he says, 'The forest's treasure is yours!'
            You discover a chest of gold and magical artifacts. Victory!
            """)
        elif third_choice == "NEGOTIATE":
            print("""
            🤝 You lower the sword and speak calmly to the dragon.
            'I did not know this blade was yours. I return it willingly.'
            The dragon's eyes soften. 'Your wisdom impresses me, young one.'
            The dragon grants you safe passage and shares ancient forest secrets.
            You leave with knowledge more valuable than gold!
            """)

    elif second_choice == "SHIELD":
        print("""
        🛡️ You take the magical shield...
        The shield feels warm in your hands. Suddenly, evil spirits emerge
        from the forest shadows, their dark magic crackling toward you!
        The shield glows and deflects their attacks easily.
        
        The spirits circle you menacingly. You can:
        - ADVANCE boldly toward the spirits
        - RETREAT while the shield protects you
        """)
        print()

        while True:
            third_choice = input("What do you do? (ADVANCE/RETREAT): ").upper()
            if third_choice == "ADVANCE" or third_choice == "RETREAT":
                break
            print("Please choose a valid action: ADVANCE or RETREAT.")

        if third_choice == "ADVANCE":
            print("""
            👻 You march forward with confidence!
            The spirits' attacks grow weaker against your shield.
            As you reach them, they suddenly transform into grateful forest spirits!
            'You have freed us from our curse!' they exclaim.
            They reward you with a magical compass that always points to treasure!
            """)
        elif third_choice == "RETREAT":
            print("""
            🏃 You back away carefully, shield raised.
            The spirits cannot harm you, and you escape safely.
            You find a hidden cave filled with ancient books of wisdom.
            The knowledge you gain makes you the wisest adventurer in the land!
            """)

    elif second_choice == "POTION":
        print("""
        🧪 You drink the flight potion...
        Wings of pure energy sprout from your back! You soar above the trees
        and spot a magnificent castle in the distance, but also notice
        a group of lost travelers trapped in a maze below.
        
        With your limited flight time, you must choose:
        - CASTLE: Fly to the mysterious castle
        - RESCUE: Dive down to help the lost travelers
        """)
        print()

        while True:
            third_choice = input("What do you do? (CASTLE/RESCUE): ").upper()
            if third_choice == "CASTLE" or third_choice == "RESCUE":
                break
            print("Please choose a valid action: CASTLE or RESCUE.")

        if third_choice == "CASTLE":
            print("""
            🏰 You soar toward the castle!
            Inside, you meet a lonely princess who has been waiting centuries
            for someone brave enough to reach her tower.
            She rewards your courage with a crown of starlight that grants
            eternal youth and happiness!
            """)
        elif third_choice == "RESCUE":
            print("""
            🚁 You swoop down to help the travelers!
            Using your aerial view, you guide them out of the maze.
            The grateful travelers reveal they are actually merchant princes!
            They grant you a share of their trading empire and lifelong friendship!
            """)

elif first_choice == "DARK":
    print("""
    🌙 You brave the dark, misty path...
    The purple mist swirls around you as you walk deeper into shadow.
    You hear whispers in the darkness, and three glowing eyes appear before you.
    A mysterious voice speaks: 'Answer my riddle, or face the consequences!'
    
    The voice asks: 'What grows stronger when shared, lighter when divided,
    and disappears when hoarded?'
    Three glowing orbs appear with possible answers:
    - KNOWLEDGE (blue orb)
    - LOVE (red orb)
    - MAGIC (green orb)
    """)
    print()

    while True:
        second_choice = input("Which answer do you choose? (KNOWLEDGE/LOVE/MAGIC): ").upper()
        if second_choice == "KNOWLEDGE" or second_choice == "LOVE" or second_choice == "MAGIC":
            break
        print("Please choose a valid answer: KNOWLEDGE, LOVE, or MAGIC.")

    if second_choice == "KNOWLEDGE":
        print("""
        📚 You touch the blue orb...
        'Correct!' the voice booms. 'Knowledge shared grows stronger!'
        The mist clears, revealing a vast library built into the trees.
        An ancient librarian approaches with a glowing book.
        
        The librarian offers you a choice:
        - READ the book of future events
        - WRITE your own story in the book of destiny
        """)
        print()

        while True:
            third_choice = input("What do you do? (READ/WRITE): ").upper()
            if third_choice == "READ" or third_choice == "WRITE":
                break
            print("Please choose a valid action: READ or WRITE.")

        if third_choice == "READ":
            print("""
            🔮 You open the book and see visions of the future!
            You learn about coming dangers and opportunities.
            Armed with this knowledge, you become a great leader who
            guides your people through difficult times to prosperity!
            """)
        elif third_choice == "WRITE":
            print("""
            ✍️ You pick up the magical quill and write your own fate!
            Your words reshape reality itself around you.
            You become the author of your own legend, with power to
            help others write their stories too!
            """)

    elif second_choice == "LOVE":
        print("""
        ❤️ You touch the red orb...
        'A beautiful answer,' the voice whispers warmly.
        The darkness transforms into a garden where separated lovers
        from different fairy tale stories are trapped by an evil spell.
        
        To break the spell, you must:
        - UNITE one pair of lovers with a magic key
        - SACRIFICE your own chance at love to free them all
        """)
        print()

        while True:
            third_choice = input("What do you choose? (UNITE/SACRIFICE): ").upper()
            if third_choice == "UNITE" or third_choice == "SACRIFICE":
                break
            print("Please choose a valid action: UNITE or SACRIFICE.")

        if third_choice == "UNITE":
            print("""
            💕 You use the magic key to unite one couple!
            Their joy breaks part of the spell, and they grant you
            a blessing of true love. You will find your soulmate
            and live happily ever after!
            """)
        elif third_choice == "SACRIFICE":
            print("""
            💖 You sacrifice your own chance at love for others!
            Your selfless act breaks the entire spell!
            All the lovers are freed, and they grant you something greater:
            the love and friendship of everyone you meet!
            """)

    elif second_choice == "MAGIC":
        print("""
        🌟 You touch the green orb...
        'An interesting choice,' the voice muses, 'but not quite right.'
        The mist thickens, and you find yourself in a swamp where
        a friendly witch offers to teach you real magic as consolation.
        
        The witch offers to teach you:
        - HEALING magic to help others
        - TRANSFORMATION magic to change yourself
        """)
        print()

        while True:
            third_choice = input("What do you choose? (HEALING/TRANSFORMATION): ").upper()
            if third_choice == "HEALING" or third_choice == "TRANSFORMATION":
                break
            print("Please choose a valid action: HEALING or TRANSFORMATION.")

        if third_choice == "HEALING":
            print("""
            🌿 You learn the arts of healing!
            You become a renowned healer, traveling the land
            and curing ailments wherever you go.
            Your compassion makes you beloved by all!
            """)
        elif third_choice == "TRANSFORMATION":
            print("""
            🦋 You learn transformation magic!
            You can now change into any animal or person.
            You use this power to help others by becoming
            whatever they need most in their darkest hour!
            """)

elif first_choice == "NARROW":
    print("""
    🌳 You squeeze through the narrow path between ancient oaks...
    The trees seem to whisper secrets as you pass. You emerge into
    a clearing where three woodland creatures await: a wise owl,
    a playful fox, and a gentle deer.
    
    Each creature offers to guide you further:
    - OWL: 'I know the path to ancient wisdom'
    - FOX: 'I know the path to great adventure'
    - DEER: 'I know the path to inner peace'
    """)
    print()

    while True:
        second_choice = input("Which guide do you choose? (OWL/FOX/DEER): ").upper()
        if second_choice == "OWL" or second_choice == "FOX" or second_choice == "DEER":
            break
        print("Please choose a valid animal: OWL, FOX, or DEER.")

    if second_choice == "OWL":
        print("""
        🦉 You follow the wise owl...
        The owl leads you to a great oak tree with a door in its trunk.
        Inside, you find a council of ancient spirits debating
        the fate of the forest. They invite you to cast the deciding vote.
        
        The debate is about:
        - PRESERVE the forest exactly as it is
        - EVOLVE and allow controlled change
        """)
        print()

        while True:
            third_choice = input("How do you vote? (PRESERVE/EVOLVE): ").upper()
            if third_choice == "PRESERVE" or third_choice == "EVOLVE":
                break
            print("Please choose a valid action: PRESERVE or EVOLVE.")

        if third_choice == "PRESERVE":
            print("""
            🌲 You vote to preserve the forest!
            The spirits are pleased with your respect for tradition.
            They name you Guardian of the Ancient Ways.
            You gain the power to protect all natural places!
            """)
        elif third_choice == "EVOLVE":
            print("""
            🌱 You vote for careful evolution!
            The spirits appreciate your wisdom and balance.
            They name you the Bridge Between Worlds.
            You can help others find harmony between old and new!
            """)

    elif second_choice == "FOX":
        print("""
        🦊 You follow the playful fox...
        The fox leads you through a series of natural puzzles and tricks.
        You arrive at a clearing where a treasure chest sits,
        but it's guarded by three riddles carved in stone.
        
        The fox grins: 'You can try to solve all three riddles,
        or use cunning to find another way!'
        - RIDDLES: Attempt to solve all three riddles
        - CUNNING: Look for a clever alternative
        """)
        print()

        while True:
            third_choice = input("What do you do? (RIDDLES/CUNNING): ").upper()
            if third_choice == "RIDDLES" or third_choice == "CUNNING":
                break
            print("Please choose a valid action: RIDDLES or CUNNING.")

        if third_choice == "RIDDLES":
            print("""
            🧩 You tackle the riddles head-on!
            Your logical thinking and persistence pay off.
            You solve all three riddles and claim the treasure:
            A bag of gold and a crown of cleverness that makes
            you the wisest puzzle-solver in the realm!
            """)
        elif third_choice == "CUNNING":
            print("""
            🎭 You look for another way...
            You notice the chest isn't actually locked!
            The fox laughs: 'Sometimes the simplest solution is best!'
            Inside you find a mirror that shows people's true nature.
            You become a great judge of character!
            """)

    elif second_choice == "DEER":
        print("""
        🦌 You follow the gentle deer...
        The deer leads you to a peaceful meadow with a crystal stream.
        You feel all your worries melt away. The deer speaks softly:
        'True peace comes from within, but how will you share it?'
        
        The deer offers you a choice:
        - MEDITATE here and gain inner wisdom
        - RETURN to the world to spread peace
        """)
        print()

        while True:
            third_choice = input("What do you choose? (MEDITATE/RETURN): ").upper()
            if third_choice == "MEDITATE" or third_choice == "RETURN":
                break
            print("Please choose a valid action: MEDITATE or RETURN.")

        if third_choice == "MEDITATE":
            print("""
            🧘 You sit in peaceful meditation...
            You achieve perfect inner balance and understanding.
            You become a spiritual guide, helping others find
            their own path to peace and enlightenment!
            """)
        elif third_choice == "RETURN":
            print("""
            🕊️ You choose to return and spread peace!
            The deer blesses you with a gentle spirit.
            Wherever you go, you bring calm to conflicts
            and harmony to troubled hearts!
            """)

print("""
==================================================
Thank you for playing The Enchanted Forest Mystery!
🌟 Your adventure has come to an end! 🌟
""")