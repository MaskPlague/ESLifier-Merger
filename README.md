# ESLifier (This README may be outdated, when in doubt, refer to the tool tips inside the program)
TBD
  
# For Users
## Files that are patched by ESLifier
<details>
  <summary>Files Patched</summary>
  
  <details>
    <summary>.INI Files</summary>

    Animated Object Swapper
    AutoBody
    Base Object Swapper
    Completionist
    Description Framework
    DtryKeyUtil
    DynDOLOD Rules
    ENB Lights for Effect Shaders
    Experience
    Form List Manipulator
    Item Property Manipulator
    Keyword Item Distributor
    KreatE (only version 1.5+ configs are supported, you may need to launch the game with your weather mod non-compacted to first convert non v1.5+ configs to v1.5 correctly)
    Leveled List Object Swapper
    Light Placer
    Music Type Distributor
    NPCs Use Potions
    Payload Interpreter
    Poise Breaker
    Seasons of Skyrim
    SkyPatcher
    Spell Perk Item Distributor
    TrueHUD
    Valhalla Combat
    Various States of Undress
  </details>

  <details>
    <summary>.JSON Files</summary>

    Achievement Injector
    Alternate Perspective
    CaptiveFollowers
    CoMAP
    Container Distribution Framework
    Creature Framework
    Custom Skills Framework (old format CustomSkill.<name>.config.txt supported)
    Dress Up Lover's NPC Outfit Changer
    dse-display-model
    Dynamic Armor Variants
    Dynamic Inventory Icon Injector
    Dynamic Key Activation Framework NG
    Dynamic String Distributor
    Follower Slavery Mod
    Frost Fall Data
    Generic Synthesis Patcher (GSP)
    Immersive Equipment Display
    Immersive Hair Growth and Styling
    Immersive Interactions
    Inte's Devious Devices - Equip
    Inte's Skyrim - Utility Mod
    Inventory Injector
    Let Your Hair Down
    Magic Fixes and Tweaks SKSE
    M.A.R.A.S.
    MCM Helper
    OBody NG
    Open Animation Replacer
    OStim Standalone
    PapyrusUtil's StorageDataUtil
    Player Equipment Manager
    Race Compatibility SKSE
    Rain Extinguished Fires
    Skyrim Unbound
    SL Config/Expressions/Animations
    SL Scaler
    Sleep In Lingerie
    Smart Harvest Auto NG AutoLoot
    Sound Record Distributor
    Spell Organizer
    Spell Research
    Undaunted
    XEMI Utility
  </details>

  <details>
    <summary>.TOML Files</summary>
      
    Actor Value Generator
    Dynamic Animation Casting
    Loki Poise
    Precision
    True Directional Movement
    YATSM - Yet Another Soul Trap Manager
  </details>

  <details>
    <summary>.YAML Files</summary>

    Precision - Unofficial Locational Damage Framework
    SLP+ Stripping/SOS/Voices
    Sound record distributor
  </details>

  <details>
    <summary>Other Types</summary>
    
      - .pex: Compiled script files
      - _conditions.txt: Dynamic Animation Replacer
      - _srd.: Sound Record Distributor
      - .jslot: Racemenu Presets
      - facegeom's .nif: Texture paths in face mesh files
      - voice, facetint, facegeom: The names of these files are patched
      - .seq: SEQ files

  </details>
</details>

## BSArch.exe
ESLifier includes a modified BSArch.exe (from [TES5Edit](https://github.com/TES5Edit/TES5Edit/tree/master/Tools/BSArchive)) to extract pex, seq, facetint, facegeom, and voice files. The modified .dpr file is included in the repo [here](https://github.com/MaskPlague/ESLifier/blob/main/bsarch/BSArch.dpr).

## User Manual
TBD

# Documentation
## How to Build
Fork this project and install python 3.13 then install these libraries via pip: _PyQt6_, _Regex_, _mmap_, _intervalTree_, _requests_, and _pyinstaller_.
Run "build_ESLifier_EXE.py" either via a terminal opened in the _ESLifier_ directory or via your IDE.



