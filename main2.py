import math

from logic import *

sack = Sack(6_404_180)
items = [
    Item(1, "Axe", 32_252, 68_674),
    Item(2, "Bronze coin", 225_790, 471_010),
    Item(3, "Crown", 468_164, 944_620),
    Item(4, "Diamond statue", 489_494, 962_094),
    Item(5, "Emerald belt", 35_384, 78_344),
    Item(6, "Fossil", 265_590, 579_152),
    Item(7, "Gold coin", 497_911, 902_698),
    Item(8, "Helmet", 800_493, 1_686_515),
    Item(9, "Ink", 823_576, 1_688_691),
    Item(10, "Jewel box", 552_202, 1_056_157),
    Item(11, "Knife", 323_618, 677_562),
    Item(12, "Long sword", 382_846, 833_132),
    Item(13, "Mask", 44_676, 99_192),
    Item(14, "Necklace", 169_738, 376_418),
    Item(15, "Opal badge", 610_876, 1_253_986),
    Item(16, "Pearls", 854_190, 1_853_562),
    Item(17, "Quiver", 671_123, 1_320_297),
    Item(18, "Ruby ring", 698_180, 1_301_637),
    Item(19, "Silver bracelet", 446_517, 859_835),
    Item(20, "Timepiece", 909_620, 1_677_534),
    Item(21, "Uniform", 904_818, 1_910_501),
    Item(22, "Venom potion", 730_061, 1_528_646),
    Item(23, "Wool scarf", 931_932, 1_827_477),
    Item(24, "Crossbow", 952_360, 2_068_204),
    Item(25, "Yesteryear book", 926_023, 1_746_556),
    Item(26, "Zinc cup", 978_724, 2_100_851),
]

solution = run_ga(items, 1000, 5, sack.max_weight)
print(solution)
