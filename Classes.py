
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
    
    
    ''' toString -> str - Return this Actor as a meaningful string 
        :return str representation of this actor
    '''
    def toString(self) -> str: 
        s = f"ACTOR (id = {self.actor_id}, primary_alias = {self.primary_alias}):\n\tactor_class: {self.actor_class}\n\tactor_region: {self.actor_region}\n\tactor_priority: {self.actor_priority}\n\taliases:"
        
        for k in self.aliases.keys(): s += f"\n\t\t{k} - {self.aliases[k]}"
        return s
    



class Tactic: 
    
    pass



class Technique: 
    
    class SubTechnique:
        
        pass
    
    pass
