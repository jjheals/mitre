from Classes import *
import pandas as pd

def Actors_From_CSVs(actor_csv_path:str, alias_csv_path:str) -> list[Actor]:
    all_actors:list[Actor] = [] # List of all actors to return 
    
    # Get the dataframe for actors from the CSV
    actor_df:pd.DataFrame = pd.read_csv(actor_csv_path, header=0, index_col=False)
    actor_df.set_index('actor_id')
    
    # Get the dataframe for aliases from the CSV
    alias_df:pd.DataFrame = pd.read_csv(alias_csv_path, header=0, index_col=False)
    alias_df.set_index('actor_id')

    # Iterate over actor_df and pull the matches from alias_df
    for r in [row[1] for row in actor_df.iterrows()]: 
        thisActor:Actor = Actor(r[0], r[1], r[2], r[3])
        thisActor.actor_priority = r['actor_priority']
        thisActor.aliases = alias_df.loc[alias_df['actor_id'] == r[0], ['source', 'alias']].set_index('source')['alias'].to_dict()
        all_actors.append(thisActor)
        
    for a in all_actors: print(a.toString() + "\n")
    return all_actors