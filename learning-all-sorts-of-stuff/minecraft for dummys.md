
-----
-- learning how to do somthing in minecraft: (also looking at mineflayer - nodejs module for bots)

(i am an idiot should have looked it up years ago: 'Parent's guide to minecraft' https://www.youtube.com/watch?v=t9eJ6TLtfd8 ... )

Modes: can switch modes
    Creative mode: the monsters can't hurt you
    Survival mode: start with nothing, have to collect and build stuff. Monsters can hurt you. Have earn stuff.
    Adventure mode: can't place/destroy blocks (need tools). 


How to use it
Navigation (just like in vim ;-)
    a d  : left,right
    w s  : up down
    swipe mouse : turn around

    space space  : (in creative mode) - start flying
    shift : gets you down again

Building
    e : bring up the 'inventory window' - the stuff that you can build with.
        
        chose type of block and put them into the 'inventory' (you can build with it)
        
        press number to switch between the selected slot in the inventory (or mouse wheel)


Messages 
    / - bring up the chat window

    # now the bot will get a 'whisper' event. (the bot will get it!)
    /msg BotyBot fly
        
    # public chat on minecraft with say (they don't seem to have that in creative mode without microsoft authentication)
    # this one results in a event for the following
    # bot.on('chat', (username, text) => { } )

    /say BotyBot fly


Coordinates in minecraft
    https://minecraft.fandom.com/wiki/Coordinates#:~:text=The%20y%2Daxis%20indicates%20how,block%20equals%201%20cubic%20meter

    (x,y,z) 
        x,z - coorinates on the plane
            x-axis indicates the player's distance east (positive) or west (negative) - longitude
            z-axis indicates the player's distance south (positive) or north (negative) of the origin point—i.e., the latitude,

        y   - the elevation from surface (

In game:
    F3 (mac fn-F3) : dumps all sort of stuff on the screen (including players coordinates)


