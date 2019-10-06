""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO


def helper_format_name(name: str) -> str:
    """
    Return the name with a change between the first name and last name.
    
    >>> helper_format_name('Wang, Patrick')
    'Patrick Wang'
    >>> helper_format_name('Wang, Yu Lin')
    'Yu Lin Wang'
    
    """
    
    first_name = name[name.find(',') + 2:]
    last_name = name[:name.find(',')]
    return first_name + ' ' + last_name


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    

    line = profiles_file.readline()
    while line != '':
        person_name = helper_format_name(line.strip())
        if person_name not in person_to_friends:
            person_to_friends[person_name] = []
        if person_name not in person_to_networks:
            person_to_networks[person_name] = []
        line = profiles_file.readline()
        while line != '' and line != '\n':
            if ',' in line:
                friend = helper_format_name(line.strip())
                if friend not in person_to_friends[person_name]:
                    person_to_friends[person_name].append(friend)
            else:
                if line.strip() not in person_to_networks[person_name]:
                    person_to_networks[person_name].append(line.strip())
            line = profiles_file.readline()
        if person_to_friends[person_name] == []:
            del person_to_friends[person_name]
        if person_to_networks[person_name] == []:
            del person_to_networks[person_name]
        line = profiles_file.readline()
    for person in person_to_friends:
        person_to_friends[person].sort()
    for person in person_to_networks:
        person_to_networks[person].sort()
            
                            
def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """
    Return the average number of friends that people have.
    
    >>> person_to_friends = {'Bob': ['Lisa', 'Dana'], 'Jeremy': ['A', 'B', 'C']}
    >>> get_average_friend_count(person_to_friends)
    2.5
    >>> person_to_friends = {}
    >>> get_average_friend_count(person_to_friends)
    0.0
    
    """
    
    
    if person_to_friends == {}:
        return 0.0
    else:
        num_of_people = len(person_to_friends)
        total_num = 0
        for key in person_to_friends:
            total_num += len(person_to_friends[key])
        return total_num / num_of_people
         
    
def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Return a dictionary of first names of people who have the same last name.
    
    >>> person_to_friends = {}
    >>> get_families(person_to_friends)
    {}
    >>> person_to_friends = {'A Sh': ['C Sh', 'B Sh', 'E Ck', 'D Ck'], \
                             'B Sh': ['C Sh', 'D Ck']}
    >>> get_families(person_to_friends)
    {'Sh': ['A', 'B', 'C'], 'Ck': ['D', 'E']}
    
    """
    
    
    dict = {}
    for i in person_to_friends:
        i = i.split(' ', 2)
        if i[-1] in dict:
            dict[i[-1]].append(i[0])
        else:
            dict[i[-1]] = [i[0]]
    for i in person_to_friends:
        for k in person_to_friends[i]:
            k = k.split(' ', 2)
            if k[-1] in dict:
                if k[0] not in dict[k[-1]]:
                    dict[k[-1]].append(k[0])
            if k[-1] not in dict:
                dict[k[-1]] = [k[0]]
    for i in dict:
        dict[i].sort()
    return dict
        

def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Return a dictionary of 'network to people'
    
    >>> person_to_networks = {}
    >>> invert_network(person_to_networks)
    {}
    >>> person_to_networks = {'A Sh': ['C Sh', 'B Sh']}
    >>> invert_network(person_to_networks)
    {'C Sh': ['A Sh'], 'B Sh': ['A Sh']}
    
    """
 
    
    result = {}
    for old_key in person_to_networks:
        for old_value in person_to_networks[old_key]:
            if old_value not in result:
                result[old_value] = [old_key]
            else:
                result[old_value].append(old_key)
    for i in result:
        result[i].sort()
    return result


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
    person: str) -> List[str]:
    """
    Return a list of name of friends of friends.
    
    >>> person_to_friends = {'A Sh': ['B Sh', 'D Sh'],\
    'B Sh': ['C Sh'], 'D Sh': ['C Sh']}
    >>> get_friends_of_friends(person_to_friends, 'A Sh')
    ['C Sh', 'C Sh']
    >>> person_to_friends = {'A Sh': ['B Sh', 'C Sh', 'D Sh'],\
    'B Sh': ['A Sh', 'C Sh', 'D Sh'],\
    'C Sh': ['A Sh', 'B Sh', 'D Sh'],\
    'D Sh': ['A Sh', 'B Sh', 'C Sh']}
    >>> get_friends_of_friends(person_to_friends, 'A Sh')
    ['B Sh', 'B Sh', 'C Sh', 'C Sh', 'D Sh', 'D Sh']
    
    """
    
    
    friends = []
    for friend in person_to_friends[person]:
        for i in person_to_friends[friend]:
            if person != i:
                friends.append(i)
    friends.sort()
    return friends
    
    
def get_score(person: str, potential_friends: List[str]) -> List[Tuple[str, int]]:
    """
    Return a list of potential friends and scores of a person.
    
    >>> person = 'Patrick Wang'
    >>> potential_friends = ['B Sh', 'C Sh', 'D Sh']
    >>> get_score(person, potential_friends)
    [('B Sh', 1), ('C Sh', 1), ('D Sh', 1)]
    """
    
    
    acc = []
    for friend in potential_friends:
        last_name = friend[friend.rfind(' ') + 1:]
        if last_name == person[person.rfind(' ') + 1:]:
            score = (friend, potential_friends.count(friend) + 1)
        else:
            score = (friend, potential_friends.count(friend))
        if score not in acc:
            acc.append(score)
    return acc
            

def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """
    
    Return a list of friends recommendation for a person based on \
    person_to_friends and person_to_networks.
    
    >>> person = 'A Sh'
    >>> person_to_friends = {'A Sh': ['X', 'D'], 'B As': ['Y'], 'C Ck': ['Z']}
    >>> person_to_networks = {'A Sh': ['AC'], 'B As': ['AC'], 'C Ck': ['AC']}
    >>> make_recommendations(person, person_to_friends, person_to_networks)
    [('B As', 1), ('C Ck', 1)]
    
    """
    
    
    potential_friends = get_friends_of_friends(person_to_friends, person)
    for friend in potential_friends:
        if friend in person_to_friends[person]:
            potential_friends.remove(friend)
    network_to_person = invert_network(person_to_networks)
    if person in person_to_networks:
        for n in person_to_networks[person]:
            for m in network_to_person[n]:
                if m != person and m not in person_to_friends[person]:
                    potential_friends.append(m)
    potential = get_score(person, potential_friends)
    sort_scores(potential)
    return potential


def sort_scores(friend: List[str]) -> List[str]:
    """
    Return a list of sorted potential friends.
    
    >>> friend = ['Claire Dunphy', 'Manny Delgado', 'Gloria Pritchett']
    >>> sort_scores(friend)
    ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado']
    
    """
    
    
    friend.sort()
    if friend != []:
        end = len(friend) - 1
        while end != 0:
            for k in range(end):
                if friend[k][1] < friend[k + 1][1]:
                    friend[k], friend[k + 1] = friend[k + 1], friend[k]
                end = end - 1
    
    return friend




if __name__ == '__main__':
    import doctest
    doctest.testmod()