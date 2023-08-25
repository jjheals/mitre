from Classes import *
import pandas as pd


''' Actors_From_CSVs(actor_csv_path, alias_csv_path) -> list[Actor] - create a list of Actor objects from the given CSVs 
        :param actor_csv_path:str path to the csv containing the 'actor' instances 
            Columns for the csv must be ["actor_id", "primary_alias", "actor_region", "actor_class", "actor_priority"]
        :param alias_csv_path:str path to the csv containing the 'alias' instances
            Columns for the csv must be ["actor_id", "source", "alias"]
        :return a list of Actor objects 
'''
def Actors_From_CSVs(actor_csv_path:str, alias_csv_path:str) -> list[Actor]:
    all_actors:list[Actor] = [] # List of all actors to return 
    
    try: 
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
    except Exception as e:
        print("ERROR: There was an error creating the actors from the CSVs.")
        print(e)
        return []