import json
import re

def getSalDict(sal):
    '''
    ## para sal: sal diction transformed from json file
    ## return sal_dict: {'suburb name that in gcc': [state number]}
                        example: 'richmond': [1, 2, 4, 6]
    '''

    gcc_names = ['1gsyd','2gmel' ,'3gbri', '4gade' , '5gper', '6ghob' , '7gdar', '8acte', '9oter']
    sal_dict = {}

    for k in sal.keys():
        g = sal[k]['gcc']
        # only consider the gcc area, ignore the rural area
        if g in gcc_names:
            #reform the suburb name into a list
            new = k.replace(' (',';').replace(')','').replace(' - ', ';')
            new = new.split(';')
            #assign state number
            s = int(sal[k]['ste'])

            if '(' not in k: #suburb name is unique (ie only appears in one state)
                sal_dict[k]=[s]
            else: # suburb name contains state abbrev (ie suburb name is not unique)
                for nn in new:
                    if nn in sal_dict and s not in sal_dict[nn]:
                        sal_dict[nn].append(s)
                    else:
                        sal_dict[nn]=[s]
    return sal_dict

def check_gcc(place,sal_dict):
    '''
    ## para place: string of place name
    ## sal_dict : dict that contains all the suburb names in gcc
    ## return gcc: string of gcc name, if not in gcc, gcc = 'nan' 
    '''    
    gcc_names = ['1gsyd','2gmel' ,'3gbri', '4gade' , '5gper', '6ghob' , '7gdar', '8acte', '9oter']
    gcc_full = ['sydney' , 'melbourne', 'brisbane', 'adelaide','perth','hobart', 'darwin','canberra']
    states = {'new south wales':1, 'queensland':3, 'south australia':4,'tasmania':6, 
              'victoria':2, 'western australia':5, 'australian capital territory':8, 
              'northern territory':7,'christmas island':9, "home island":9, "jervis bay":9, 
              "norfolk island":9, "west island":9,'nsw':1, 'qld':3, 'sa':4,'tas':6, 'vic':2, 
              'wa':5, 'act':8, 'nt':7}
    
    gcc_full = dict(zip(gcc_full,gcc_names))
    # reform the place name into a list
    place = place.lower()
    new = place.replace('(',',').replace(')',',').replace(' - ', ',').replace('.','').replace(",,",',')
    plist = re.split(', | ,|,',new)
    gcc = 'nan'

    
    if plist[-1] == 'australia':
        plist.pop(-1)
    
    if len(plist)>0:
        # check plist[0] first
        if plist[0] in sal_dict.keys():
            #p_ste is the (list of) protential state number
            p_ste = sal_dict[plist[0]]
            # if urb name is unique, assign gcc
            if len(plist)==1: 
                if len(p_ste)==1:
                    gcc = gcc_names[p_ste[0]-1]
            else:
                # if urb name is not unique, check if plist[-1] is state or gcc
                #print('len(plist)>1')
                ss = states.get(plist[-1],0)
                # if state matches suburb name, assign gcc
                if ss in p_ste: 
                    #print('in p_ste')
                    gcc = gcc_names[ss-1]
                else:
                    # if plist[-1] matches one of gcc
                    if plist[-1] in gcc_full.keys():
                        gcc = gcc_full[plist[-1]]
                        #gcc = gcc_names[gcc.index(plist[-1])+1]
                    else:
                        #print('not in gcc')
                        None
                        
            
        else:
            #print('nan')
            if len(plist)>1 and plist[1] in sal_dict.keys():
                #print('yes plist[-1] gcc')
                p_ste = sal_dict[plist[1]]
                gcc = gcc_names[p_ste[0]-1]
            None

    return gcc

if __name__ == "__main__":
    with open("final_json.json", "w", encoding="utf-8") as output_f:
        with open("sal.json", "r", encoding = 'utf-8') as f:
            sal = json.load(f)
            sal_dict = getSalDict(sal)
        with open('preprocess_homeless_twitterdata.json','r') as json_file:
            json_file.readline()
            output_f.write("[\n")
            while True:
                try:
                    current_line = json_file.readline()
                    if current_line == "]" or current_line == "\n" or current_line == "":
                        output_f.write("]")
                        break
                    else:
                        current_line = current_line[:-2]
                        json_object = json.loads(current_line)
                        place = json_object['full_name']
                        json_object['gcc'] = check_gcc(place,sal_dict)
                        json.dump(json_object, output_f, indent=4)
                        output_f.write(",\n")
                        
                except json.JSONDecodeError:
                    print(f'Error decoding JSON for line: {current_line}')
                    continue  # skip to the next line
            