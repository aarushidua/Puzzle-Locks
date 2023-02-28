# Puzzle-Solver

Storyline: 
Adventurer Lin has struggled through a maze of twisty little passages, all alike, to reach the bottom of a colossal cave hidden deep in the mountains.
At this point, only three locked doors stand between Lin and the Well of Wisdom.
Your aim in this project is to help Lin solve the puzzles that will unlock these doors and then, perhaps, to help Lin escape.

Puzzle 1:
The first lock consists of a panel filled with sparkling gems. Beside the panel is a row of buttons, one corresponding to each type of gem. To unlock the door, Lin must press the button corresponding to the most common type of gem in the panel. Note that, if there is a tie between the most common type of gem (ie, there are equal numbers), then more than one button will need to be pressed.

The code: 
- Determines what gems are the most common and need to be pressed
- Takes a list of gems and returns the most common in alphabetical order

Puzzle 2:
The second lock consists of a "T"-shaped groove in the door. The left branch of the T is labelled source, the right branch is labelled destination, and the bottom branch is labelled store. Several gems are mounted in the left branch (the source) such that they can be slid along the groove toward the right or bottom branches. Each of the gems is numbered consecutively beginning from one. No numbers are skipped, nor are any numbers duplicated; however, some of the gems are out of order. Gems cannot be slid over the top of other gems.

To unlock the door, Lin must slide the gems onto the destination branch in increasing numerical order. The store branch can be used to help reorder the gems (see below for a step by step example). After some experimentation, Lin notes that any gem which is slid into the destination or store branches can no longer slide back toward the source branch.

Visualisation:

(source)             (destination)
   |-3-4-5-2-1-+-----------|
               |
               |
               |
               :
            (store)
            
The code:
 - Takes a list of integer gem numbers as input (number in position 0 is the last gem to be moved)
 - Returns a tuple consisting of a boolean value specifying whether the door can be unlocked or not, and an integer corresponding to the largest number of gems that are required to be located on the store branch at any one point in time
 - If cannot be solved returns (False, -1)

Puzzle 3:

The third lock consists of a stone with a set of irregular holes carved out of it. Lin realises that an oddly-shaped gem found elsewhere in the cave that might fit this lock.

Your task is to write a function third_lock(key, stone) that determines whether the "key" gem will fit the pattern of holes in the "stone" lock. If the key is smaller than the stone, then the key can be moved to any location relative to the stone, so long as it doesn't extend beyond the edge of the stone in any direction. The key can also be rotated to any of four possible orientations: (N)orth (with the top of the key facing up), (E)ast (with the key rotated 90 degree clockwise such that the top faces to the right), (S)outh (with the key rotated 180 degrees clockwise such that the top faces downwards), or (W)est (with the key rotated 270 degrees clockwise such that the top faces to the left). The key can only be moved or rotated, it cannot be flipped over.

If a key will fit a stone in multiple orientations and/or locations then return the combination closest to the top, the left and 0 degree rotation.

The code:
- Take two nested lists describing the shape of the key (which parts are "raised") and the shape of the stone (which parts contain "holes" that raised parts of the key fit within) as input
- Returns a tuple specifying the location (in terms of row-index and column-index) and orientation of the key if it will fit, or None if the key will not fit for any location or orientation

Visualisation example:
**
*.

key1 = [['*', '*'], ['*', '.']]

...
.#.
...

stone1 = [['.', '.', '.'], ['.', '#', '.'], ['.', '.', '.']]

#Files

The files consist of solutions for all three puzzles and separate files for their sample test cases
