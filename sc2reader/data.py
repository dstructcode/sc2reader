# Encoding: UTF-8

abilities = {

    #Zerg Create Unit
    0x032200: 'Birth Queen',
    0x023000: 'Morph to Drone',
    0x023002: 'Morph to Drone (2)',
    0x023001: 'Morph to Zerglings',
    0x003900: 'Morph to Baneling',
    0x027001: 'Morph to Roach',
    0x030c00: 'Morph to Overseer',
    0x023003: 'Morph to Hydralisk',
    0x027002: 'Morph to Infestor',
    0x023004: 'Morph to Mutalisk',
    0x012a00: 'Cancel Morph',
    
    #Zerg Create Building
    0x022610: 'Build Hatchery',
    0x022622: 'Build Extractor',
    0x022613: 'Build Spawning Pool',
    0x026616: 'Build Spine Crawler',
    0x022614: 'Build Evolution Chamber',
    0x026617: 'Build Spore Crawler',
    0x026612: 'Build Baneling Nest',
    0x026615: 'Build Roach Warren',
    0x022615: 'Build Hydralisk Den',
    0x026610: 'Build Infestation Pit',
    0x022616: 'Build Spire',
    0x012e00: 'Cancel Building (Extractor)',
    
    #Zerg Building Upgrades
    0x022900: 'Mutate into Lair',

    #Zerg Unit Abilities
    0x011f20: 'Spawn Larvae',
    0x033310: 'Spawn Creep Tumor (Queen)',
    0x033810: 'Spawn Creep Tumor (Creep Tumor)',
    0x032420: 'Transfusion',
    0x033200: 'Generate Creep',
    0x010f00: 'Spawn Changling',
    0x023400: 'Burrow (Drone)',
    0x023a00: 'Burrow (Zergling)',
    0x023800: 'Burrow (Roach)',
    0x023900: 'Unburrow (Roaches)',
    0x003610: 'Fungal Growth',
    
    #Zerg Unit Research
    0x022d01: 'Evolve Metabolic Boost',
    0x022c03: 'Evolve Burrow',
    0x030f00: 'Evolve Centrifugal Hooks',
    0x011b01: 'Evolve Glial Reconstitution',
    0x011b02: 'Evolve Tunneling Claws',
    0x022e02: 'Evolve Grooved Spines',
    0x022c01: 'Evolve Pneumatized Carapace',
    
    #Zerg Unit Upgrades
    0x022800: 'Evolve Melee Attacks Level 1',
    0x022806: 'Evolve Missile Attacks Level 1',
    0x022807: 'Evolve Missile Attacks Level 2',
    0x022803: 'Evolve Ground Carapace Level 1',
    0x022804: 'Evolve Ground Carapace Level 2',
    0x012b00: 'Cancel Evolution (Evolution Chamber)',
    
    #Protoss Buildings
    0x021910: 'Warp in Nexus',
    0x021911: 'Warp in Pylon',
    0x021914: 'Warp in Forge',
    0x021917: 'Warp in Photon Cannon',
    0x021913: 'Warp in Gateway',
    0x021922: 'Warp in Assimilator',
    0x025916: 'Warp in Cybernetics Core',
    0x021916: 'Warp in Twilight Council',
    0x025912: 'Warp in Templar Archives',
    0x025915: 'Warp in Robotics Facility',
    0x025914: 'Warp in Robotics Bay',
    0x025911: 'Warp in Stargate',
    
    #Protoss Units
    0x021e00: 'Warp in Probe',
    0x021b00: 'Warp in Zealot',
    0x030510: 'Warp in Zealot (warp gate)',
    0x021b01: 'Warp in Stalker',
    0x030511: 'Warp in Stalker (warp gate)',
    0x021b05: 'Warp in Sentry',
    0x030515: 'Warp in Sentry (warp gate)',
    0x030513: 'Warp in High Templar (warp gate)',
    0x021d01: 'Warp in Observer',
    0x021d03: 'Warp in Immortal',
    0x021d02: 'Warp in Colossus',
    0x021c00: 'Warp in Pheonix',
    0x021c04: 'Warp in Void Ray',
    0x012b31: 'Cancel Warp In (Gateway)',
    
    #Protoss Upgrades
    0x022300: 'Upgrade Ground Weapons Level 1',
    0x022301: 'Upgrade Ground Weapons Level 2',
    0x022302: 'Upgrade Ground Weapons Level 3',
    0x022303: 'Upgrade Ground Armor Level 1',
    0x022304: 'Upgrade Ground Armor Level 2',
    0x022305: 'Upgrade Ground Armor Level 3',
    
    #Protoss Research
    0x031b06: 'Research Warp Gate',
    0x031c01: 'Research Blink',
    0x031c00: 'Research Charge',
    0x022504: 'Research Psionic Storm',
    0x022405: 'Research Extended Thermal Lance',
    
    #Protoss Abilities
    0x012420: 'Chrono Boost',
    0x031300: 'Transform to Warp Gate',
    0x030910: 'Blink',
    0x031710: 'Force Field',
    0x003700: 'Guardian Shield',
    0x021f10: 'Psionic Storm',
    0x010b20: 'Graviton Beam',
    
    #Terran Buildings
    0x013011: 'Build Supply Depot',
    0x013013: 'Build Barracks',
    0x013016: 'Build Bunker',
    0x013022: 'Build Refinery',
    0x017012: 'Build Factory',
    0x017013: 'Build Starport',
    0x017015: 'Build Armory',
    0x020200: 'Build Tech Lab (Barracks)',
    0x020400: 'Build Tech Lab (Factory)',
    0x020201: 'Build Reactor (Barracks)',
    0x020211: 'Build Reactor (Barracks) (Liftoff to location)',
    0x020401: 'Build Reactor (Factory)',
    0x031200: 'Orbital Command',
    
    #Terran Units
    0x020a00: 'Train SCV',
    0x020e00: 'Train Marine',
    0x020e03: 'Train Marauder',
    0x020f05: 'Build Hellion',
    0x020f01: 'Build Seige Tank',
    0x020f04: 'Build Thor',
    0x021000: 'Build Medivac',
    
    #Terran Abilities
    0x013200: 'Use Stimpack',
    0x031f00: 'Salvage (Bunker)',
    0x010a20: 'Calldown: MULE',
    0x012120: 'Calldown: Extra Supplies',
    0x013a10: 'Scanner Sweep',
    0x020c00: 'Lower (Supply Depot)',
    0x020d00: 'Raise (Supply Depot)',
    0x020300: 'Liftoff (Barracks)',
    0x020500: 'Liftoff (Factory)',
    0x020b10: 'Land (Barracks)',
    0x020810: 'Land (Factory)',
    0x013e01: 'Unload All (Bunker)',
    
    #Terran Research
    0x021401: 'Research Combat Shield',
    0x021400: 'Research Stimpack',
    
    #Terran Upgrades
    0x021802: 'Upgrade Vehicle Plating Level 1',
    
    #General
    0x370000: 'Right Click Unit (370001) Neutral?',
    0x370001: 'Gather Minerals (370001)',
    0x370003: 'Right Click Unit (370003)',
    0x370002: 'Right Click Unit (370002)',
    0x370004: 'Right Click Unit (370004)',
    0x370005: 'Right Click Unit (370005)',
    0x370006: 'Right Click Unit (370006)',
    0x370007: 'Right Click Unit (370007)',
    0x570000: 'Right Click Unit Again? (570000) Fog of war?',
    0x002400: 'Stop (I think)',
    0x002910: 'Attack (A) (2910)',
    0x002920: 'Attack (A) (2920) (Targetted?)',
    0x002602: 'Hold Position (Zealot?)',
    0x002611: 'Patrol',
    0x012b31: 'Set Rally Point? Or Right Click...',
}

units = {

    #Terran Buildings
    0x030901: 'Command Center',
    0x030a01: 'Supply Depot (raised)',
    0x021301: 'Supply Depot (lowered)',
    0x004b01: 'Supply Depot (lowered) (2)',
    0x031001: 'Command Center (upgrading to orbital command)',
    0x002801: 'Orbital Command',
    0x000c01: 'Barracks',
    0x010e01: 'Factory',
    0x011301: 'Factory (Flying)',
    0x020701: 'Factory (Flying) (2)',
    0x010f01: 'Starport',
    0x020d01: 'Amory',
    0x000f01: 'Bunker',
    0x001101: 'Tech Lab (Addon)',

    #Terran Units
    0x021101: 'SCV',
    0x011601: 'SCV (Alternate, Building?)',
    0x031001: 'Marine',
    0x031301: 'Marauder',
    0x001501: 'Hellion',
    0x030d01: 'Seige Tank',
    0x001401: 'Thor',
    
    #Zerg
    0x002d01: 'Larvae',
    0x001301: 'Egg',
    0x014101: 'Egg ..',
    0x002301: 'Egg (Cocoon? Individual?)',
    0x040301: 'Egg (fast spawning)',
    0x080301: 'Egg (spawning stuffs..)',
    0x020301: 'Egg (4 at a time?)',
    0x010301: 'Egg (extra)',
    0x008301: 'Egg (extra2)',
    0x012901: 'Creep Tumor',
    0x012001: 'Drone',
    #0x010401: 'Drone (Alternate)',
    0x012101: 'Zergling',
    #0x001501: 'Zergling (Alternate)',
    0x000b01: 'Baneling',
    0x011101: 'Baneling (Alternate)',
    0x022201: 'Roach',
    0x012301: 'Hydralisk',
    0x022301: 'Infestor',
    0x022001: 'Mutalisk',
    0x009001: 'Burrowed Unit (Drone)',
    0x004801: 'Burrowed Unit (Drone) (2)',
    0x002401: 'Burrowed Unit (Drone) (3)',
    0x041001: 'Burrowed Unit (Drone) (4)',
    0x021001: 'Burrowed Unit (Drone) (5)',
    0x002701: 'Burrowed Unit (Zergling)',
    0x002601: 'Burrowed Unit (Roach)',
    0x021201: 'Burrowed Unit (Roach) (2)',
    0x041201: 'Burrowed Unit (Roach) (3)',
    0x010a01: 'Burrowed Unit (Roach) (4)',
    0x011201: 'Unburrowing (Roach)',
    0x040a01: 'Unburrowing (Roach) (2)',
    0x020a01: 'Unburrowing (Roach) (3)',
    0x032501: 'Overseer',
    0x032401: 'Overseer Cocoon',
    0x040201: 'Baneling Cocoon',
    0x020201: 'Baneling Cocoon (2)',
    0x010201: 'Baneling Cocoon (3)',
    0x002201: 'Baneling Cocoon (4)',
    0x011001: 'Baneling Cocoon (5)',
    0x000a01: 'Baneling Cocoon (6)',
    
    0x022601: 'Queen',
    0x012201: 'Overlord',
    
    0x001e01: 'Hatchery',
    0x003e01: 'Extractor',
    0x011c01: 'Extractor (building?)',
    0x011d01: 'Spawning Pool',
    0x031e01: 'Spine Crawler',
    0x011e01: 'Evolution Chamber',
    0x031f01: 'Spore Crawler',
    0x031d01: 'Roach Warren',
    0x021e01: 'Infestation Pit',
    0x011f01: 'Hydralisk Den',
    0x031c01: 'Baneling Nest',
    0x021c01: 'Spire',
    0x002001: 'Lair',
    
    #Protoss
    0x011701: 'Nexus',
    0x021401: 'Pylon',
    0x021501: 'Assimilator',
    0x021701: 'Forge',
    0x021601: 'Gateway',
    0x002901: 'Warp Gate',
    0x011801: 'Cybernetics Core',
    0x031501: 'Twilight Council',
    0x001801: 'Templar Archives',
    0x001b01: 'Robotics Facility',
    0x001a01: 'Robotics Bay',
    0x031701: 'Stargate',
    
    #Protoss Units
    0x001c01: 'Probe',
    #0x041101: 'Probe (Alternate)',
    #0x007001: 'Probe (Alternate)',
    0x011901: 'Zealot',
    0x006e01: 'Alternate Toss (6e01) (Void/Pheonix)',
    0x006c01: 'Alternate Toss (6c01) (Void/Pheonix)',
    0x006901: 'Alternate Toss (6901) (Sentry/Immortal)',
    0x001d01: 'Alternate Toss (1d01) (Colossus)',
    0x006601: 'Alternate Toss (6601) (Stalker)',
    0x006501: 'Alternate Toss (6501) (Zealot)',
    0x006f01: 'Alternate Toss (6f01) (Sentry/Immortal)',
    0x011a01: 'Stalker',
    0x021901: 'Sentry',
    0x011b01: 'High Templar',
    0x031a01: 'Observer',
    0x031b01: 'Immortal',
    0x030501: 'Colossus',
    0x021a01: 'Pheonix',
    0x031801: 'Void Ray',
    
    #General
    0x034201: 'Destructible Rocks',
    0x034301: 'Destructible Rocks (2)',
    0x024101: 'Destructible Debris',
    0x032901: "Xel'Naga Tower",
    0x003d01: 'Mineral Field',
    0x022b01: 'Rich Mineral Field',
}

# These are found in Repack-MPQ/fileset.{locale}#Mods#Core.SC2Mod#{locale}.SC2Data/LocalizedData/Editor/EditorCategoryStrings.txt
# EDSTR_CATEGORY_Race
# EDSTR_PLAYERPROPS_RACE
# question mark means not confirmed data
races = {
    # deDE
    # enUS
    # esES
    # esMX
    # frFR
    # itIT
    
    # koKR
    '프로토스': 'Protoss',
    '테란': 'Terran',
    '저그': 'Zerg',
    
    # plPL
    # ptBR
    # ruRU
    'Протосс': 'Protoss',
    'Терран': 'Terran',
    'Зерг': 'Zerg',
    # zhCN
    # zhTW
    
    # Uncategorized
    '神族': 'Protoss',
    '蟲族': 'Zerg',
    '人類': 'Terran'
}