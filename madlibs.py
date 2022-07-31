import os, re, json

def getStoryTitles(story_list):
    """ Get story names from txt file names

    Args:
        story_list (array): list of story file names

    Returns:
        array: titles of stories
    """
    story_titles = []
    
    for story in story_list:
        # Trim .txt, replace - with space
        story_titles.append(re.sub('-', ' ', story[0:-4]))
        
    return story_titles

def pickStory(num_stories):
    """ Pick the story

    Args:
        num_stories (int): number of available stories

    Returns:
        int: selected story index
    """
    try: 
        story_id = int(input('Please pick a story: '))
        
        if story_id < 1 or story_id > num_stories:
            print('Please pick a valid number')
            pickStory(num_stories) 
            
        return story_id - 1
    
    except: 
        print('Please enter story number') 
        pickStory(num_stories) 

# TODO: Get words from user
def getWords(story_file):
    """ Get words from the user

    Args:
        story_file (string): name of the story file

    Returns:
        array: an array of arrays to map words
    """
    # Open key file, get dictionary, close
    k = open('key.json', 'r')
    word_keys = json.load(k)
    k.close
    
    x = []  # Initialise array of words
    
    # Set words
    for key in word_keys.keys():
        x.append(key)
    
    # Open selected story file
    with open('./stories/' + story_file, 'r') as f:
        story = f.read()
    f.close
    
    story_keys = re.findall('([A-Z]+\[\d+\])', story)
    
    return story_keys
    

# TODO: Assign words to parts of story

def main():
    # Get list of story txt files and titles
    story_list = os.listdir('./stories')
    story_titles = getStoryTitles(story_list)
    
    list_format = '[{num}] {story}'
    num_stories = len(story_list)
    
    # List story titles
    for i in range(0, num_stories):
        print(list_format.format(num = i + 1, story = story_titles[i]))
    
    # Select a story
    story_id = pickStory(num_stories)
    story_file = story_list[story_id]
    
    words = getWords(story_file)
    
    # TODO: get words, format story
    
    print(words)
    
main()