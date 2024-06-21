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
    tow['player1_subfaction'] = 'grand army'
    tow['player2_subfaction'] = 'grand army'

    tow.to_csv('tow_processed.csv', index=False)

    subfactions = ['mortuary cult', 'royal host', 'exiles', 'errantry crusade', 'nomadic waagh', 'troll horde']

    temp = tow[tow['player1_list_url'].str.contains("mortuary cult") == True].index.tolist()
    # tow.at[temp.index.astype(int), 'player1_subfaction'] = 'mortuary cult'
    print(temp)

    # for subfaction in subfactions:
    #     tow['player1_subfaction'] = tow['player2_subfaction'].where(tow['player1_list_url'].ne(subfaction),
    #                                                                 subfaction)
        # if tow['player1_list_url'].str.contains(subfaction).any():
        #     tow['player1_subfaction'] = subfaction

    # print(tow.query("player1_faction == 'O&G'")['player1_list_url'].head())
