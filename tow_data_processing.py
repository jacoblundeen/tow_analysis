import pandas as pd
import numpy as np

if __name__ == "__main__":
    tow = pd.read_excel('tow.xlsx')

    tow.columns = map(str.lower, tow.columns)
    tow.columns = tow.columns.str.replace(' ', '_')
    tow.columns = tow.columns.str.replace('?', '')
    faction_replace = {'Warriors of Chaos': 'w_chaos', 'Tomb Kings of Khemri': 'tomb_kings',
                       'Kingdom of Bretonnia': 'bretonnia', 'Ogre Kingdoms': 'ogres', 'Wood Elf Realms': 'wood_elves',
                       'Dwarfen Mountain Holds': 'dwarves', 'Orc and Goblin Tribes': 'o_and_g',
                       'Empire of Man': 'empire',
                       'Beastmen Brayherds': 'beastmen', 'High Elf Realms': 'high_elves', 'Daemons of Chaos': 'd_chaos',
                       'Vampire Counts': 'vampire_counts', 'Dark Elves': 'dark_elves', 'Chaos Dwarfs': 'chaos_dwarves',
                       'Skaven': 'skaven', 'Lizardmen': 'lizardmen'}
    result_replace = {1: 0.5, 2: 1}
    tow.replace({'player1_faction': faction_replace}, inplace=True)
    tow.replace({'player2_faction': faction_replace}, inplace=True)
    tow.replace({'player1_result': result_replace}, inplace=True)
    tow.replace({'player2_result': result_replace}, inplace=True)
    tow['player1_list_url'] = tow['player1_list_url'].str.lower()
    tow['player2_list_url'] = tow['player2_list_url'].str.lower()
    tow['player1_subfaction'] = 'grand_army'
    tow['player2_subfaction'] = 'grand_army'

    subfactions = ['mortuary cult', 'royal host', 'exiles', 'errantry crusade', 'nomadic waagh', 'troll horde']
    subf_proper = ['mortuary_cult', 'royal_host', 'exiles', 'errantry_crusade', 'nomadic_waagh', 'troll_horde']

    for subfaction, subf in zip(subfactions, subf_proper):
        player1_indices = tow[tow['player1_list_url'].str.contains(subfaction) == True].index.tolist()
        player2_indices = tow[tow['player2_list_url'].str.contains(subfaction) == True].index.tolist()
        tow.loc[player1_indices, 'player1_subfaction'] = subf
        tow.loc[player2_indices, 'player2_subfaction'] = subf

    tow = tow.query("`mirror_match` == 'N' & full_data == 'Y'")

    player1_db = tow[['player1_faction', 'player1_subfaction', 'player2_faction', 'player2_subfaction',
                      'player1_result', 'points', 'rounds', 'ruleset', 'players']].rename(
        columns={"player1_faction": "player_faction", "player2_faction": "opponent_faction",
                 "player1_result": "result", "player1_subfaction": "player_subfaction",
                 "player2_subfaction": "opponent_subfaction"})
    player2_db = tow[
        ['player2_faction', 'player2_subfaction', 'player1_faction', 'player1_subfaction', 'player2_result', 'points',
         'rounds', 'ruleset', 'players']].rename(
        columns={"player2_faction": "player_faction", "player1_faction": "opponent_faction",
                 "player2_result": "result", "player2_subfaction": "player_subfaction",
                 "player1_subfaction": "opponent_subfaction"})
    tow_db = pd.concat([player1_db, player2_db], ignore_index=True)
    tow_db['result'].replace('', np.nan, inplace=True)
    tow_db.dropna(subset=['result'], inplace=True)

    tow_db.to_csv('tow_processed.csv', index=False)
