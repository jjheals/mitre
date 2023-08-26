import pandas as pd
from enum import Enum 

# -------------------------------------------------------------------------- #
# CLASSES FOR DATABASE OBJECTS

class Actor: 
    
    actor_id:str
    primary_alias:str
    actor_region:str
    actor_class:str
    actor_priority:int 
    aliases:dict[str,str]
    
    def __init__(self, id:str, prim_alias:str, region:str, a_class:str): 
        self.actor_id = id
        self.primary_alias = prim_alias
        self.actor_region = region
        self.actor_class = a_class
        self.actor_priority = -1
        self.aliases = {}
    
    
    ''' toString() -> str - Return this Actor as a meaningful string 
        :return str representation of this actor
    '''
    def toString(self) -> str: 
        s = f"ACTOR (id = {self.actor_id}, primary_alias = {self.primary_alias}):\n\tactor_class: {self.actor_class}\n\tactor_region: {self.actor_region}\n\tactor_priority: {self.actor_priority}\n\taliases:"
        
        for k in self.aliases.keys(): s += f"\n\t\t{k} - {self.aliases[k]}"
        return s
    
# -------------------------------------------------------------------------- #
# CLASSES FOR MITRE ATT&CK FRAMEWORK

import mitreattack.attackToExcel.attackToExcel as attackToExcel
import mitreattack.attackToExcel.stixToDf as stixToDf

class MitreDomains:
    ICS = "ics-attack"
    ENTERPRISE = "enterprise-attack"
    MOBILE = "mobile-attack"
    
class Mitre:
    
    domain:str 
    attack_data:object
    attack_dfs_dict:dict
    tactics_df:pd.DataFrame
    techniques_df:pd.DataFrame
    
    def __init__(self, domain:str): 
        self.domain = domain
        try: self.attack_data = attackToExcel.get_stix_data(domain)
        except: 
            print("Error in Mitre: Invalid domain. Exiting.")
            return 
        
        self.attack_dfs_dict = attackToExcel.build_dataframes(self.attack_data, domain)
        self.tactics_df = self.attack_dfs_dict['tactics']['tactics']
        self.techniques_df = self.attack_dfs_dict['techniques']['techniques']
        
    def getAllTactics() -> pd.DataFrame: 
        pass
        
class Tactic: 
    
    tactic_id:int
    tactic_name:str
    
    def __init__(self, id:int, name:str):
        self.tactic_id = id
        self.tactic_name = name

    ''' toString -> str - Return this tactic as a meaningful string 
        :return str representation of this tactic
    '''
    def toString(self) -> str: return f"TACTIC (id: {self.tactic_id}, name: {self.tactic_name})"
             
class Technique: 
    
    class SubTechnique:
        
        pass
    
    pass
