classDiagram
    PrisonBox <.. Board
    BeginBox <.. Board
    class Board {
        +BeginBox &begin
        +PrisonBox &prison
    }
    Board "1" -- "40" Box
    Box .. Box
    class Box {
        +String name
        +Box &prev
        +Box &last
        +virutal do_action()
    }

    Board "1" -- "2-8" Player
    Player .. Box
    class Player {
        +String type
        +Box REFcurrent
        +Integer money
    }

    Board "1" -- "2" Dice
    class Dice {
        +int max
        +throw_dice()
    }

    Box <|--  "1" BeginBox
    class BeginBox {

    }

    Box <|--  "1" PrisonBox
    class PrisonBox {

    }

    StreetBox ..> Player
    Box <|--  "?" StreetBox
    class StreetBox {
        +String streetName
        +Integer houseCount
        +Integer hotelCount
        +Integer maxHouses = 4
        +Integer maxHotels = 1
        +Player &owner
    }

    Box <|--  "?" YhteismaaSattuma
    class YhteismaaSattuma {
        +queue cards
        +takeCard()
    }

    Box <|--  "?" AsemaLaitos
    class AsemaLaitos {

    }
