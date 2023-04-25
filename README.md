# fsDB
CANCELED: An implementation of basic cli commands using sqlite and python

NEW PROJECT: Hogwarts Wizard Duels

Here's a list of spells with descriptions that need to be placed into a table called 'Spells':<br>
(This list is provided by ChatGPT)
Accio	              Summoning charm used to bring an object to the caster<br>
Aguamenti     	    Creates a stream of water from the wand<br>
Alohomora	          Opens and unlocks doors and windows<br>
Avada Kedavra	      Unforgivable curse that instantly kills the target<br>
Confundus	          Causes confusion in the target<br>
Crucio	            Unforgivable curse that causes intense pain to the target<br>
Expelliarmus	      Disarming charm used to disarm an opponent<br>
Expecto Patronum	  Creates a Patronus, a protective magical charm against Dementors<br>
Imperio	            Unforgivable curse that allows the caster to control the actions of the target<br>
Incendio	          Starts a fire<br>
Levicorpus	        Levitates the target by the ankles<br>
Obliviate	          Erases memories from the target<br>
Protego	            Creates a shield charm that blocks spells<br>
Reducto	            Breaks objects into pieces<br>
Sectumsempra        Causes deep and gory wounds on the target<br>
Stupefy	            Stunning spell used to knock out the target<br>
Apparate	          Teleportation spell that allows the caster to instantly transport themselves to a different location<br>
Bat-Bogey Hex     	Causes the target's bogies to grow wings and attack them<br>
Bombarda	          Creates a small explosion<br>
Colloportus	        Seals a door or other object, making it impossible to open<br>
Confringo	          Causes the target to burst into flames<br>
Diffindo	          Cuts or slashes objects, such as clothing or curtains<br>
Episkey	            Minor healing spell used to heal minor injuries<br>
Evanesco	          Vanishing spell used to make an object disappear<br>
Ferula	            Conjures up a bandage and splint for a broken limb<br>
Finite Incantatem	  Ends the effects of spells and charms<br>
Fidelius	          Hides a secret within the soul of a chosen person, making it impossible for others to discover it<br>
Glisseo	            Causes stairs to flatten into a slide<br>
Impervius         	Waterproofing spell<br>
Invisibility Charm	Renders the caster invisible<br>
Langlock	          Glues the target's tongue to the roof of their mouth<br>
Lumos	              Creates a small light at the end of the wand<br>
Muffliato	          Causes a buzzing noise in the ears of those nearby, making it difficult for them to hear conversations<br>
Petrificus Totalus	Full-body bind that immobilizes the target<br>
Prior               Incantato	Reveals the last spell cast by a wand<br>
Protean             Charm	Allows a group of objects to assume the same form or pattern as a single "master" object<br>
Reparo	            Fixes broken objects<br>
Riddikulus	        Causes the target's greatest fear to become comically absurd<br>
Silencio	          Silences the target, making them unable to speak<br>
Sonorus	            Amplifies the caster's voice<br>
Tarantallegra	      Forces the target to dance uncontrollably<br>
Wingardium Leviosa	Levitates objects, allowing them to be moved through the air<br>

*Note: We need to also add a damage power to the end of each of these spells in another column of the table*<br>

Other rules to be added for dueling:<br>
1.  Year will *increase* the spell's power as follows:<br>
  - year 1 -> x 1.10<br>
  - year 2 -> x 1.25<br>
  - year 3 -> x 1.50<br>
  - year 4 -> x 2.00<br>
2.  However, if wizard 1 in the duel is the house weakness of wizard 2's house, then both wizard's lose any year bonuses...but wizard 1 gets a 1.75 spell power boost.<br>
3.  Use of a random number generator will select the id of a spell that the user will cast for that round. Each duel will be best of three rounds unless two spells are     cast: aparate or avada Kedavra<br>
  - The wizard that casts aparate **LOSES** for running away.<br>
  - The wizard that casts Avada Kedavra **WINS**, but only if they used it *ONCE*.  More than once gets sent to Azkaban.<br>

TABLES to build:
1. Wizards
2. Spells
3. Houses
4. Azkaban
5. Results
