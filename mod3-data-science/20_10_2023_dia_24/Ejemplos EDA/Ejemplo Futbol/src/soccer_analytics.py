import pandas as pd
from tqdm.notebook import tqdm
import warnings
import json
from mplsoccer.pitch import Pitch
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
warnings.filterwarnings('ignore')

class PreprocessData:
    
    def generate_teams_match_data(file:str, file2:str)->(pd.DataFrame, pd.DataFrame):
        
        '''
            This function create a dataframe with all the events from a tracking data file of all the players that participate on this match.
            
            Parameters:
                - file: Route of the file that stores the structured data of the match obtained from SkillCorner
                - file2: Route of the file that stores the data of the match obtained from SkillCorner
                
            
            Returns:
            
                DataFrames with all the events of the match for the home team and away team separated.
        
        
        '''
    
        with open(file) as f:
            match_js = json.load(f)

        with open(file2) as f2:
            match_data_js = json.load(f2)

        event = 0
        events = []
        for i in tqdm(range(len(match_js))):
            for j in range(len(match_js[i]['data'])):
                    try:
                        if match_js[i]['data'][j]['trackable_object']:
                            event_id = event +1
                            pos_x = match_js[i]['data'][j]['x']
                            pos_y = match_js[i]['data'][j]['y']
                            time = match_js[i]['time']
                            period = match_js[i]['period']
                            track_object = match_js[i]['data'][j]['trackable_object']
                            track_id = match_js[i]['data'][j]['track_id']


                            ev = {'event_id': event_id,
                                  'pos_x': pos_x,
                                  'pos_y':pos_y,
                                  'time': time,
                                  'period': period,
                                  'track_object': track_object,
                                  'track_id': track_id}
                            events.append(ev)
                        else:
                            pass
                    except:
                        pass

        match = pd.DataFrame(events)
        p1 = match[match.period == 1]
        p2 = match[match.period == 2]
        p2['pos_x_abs'] = [-1 * i for i in p2.pos_x]
        p2['pos_y_abs'] = [-1 * i for i in p2.pos_y]
        p1['pos_x_abs'] = [1 * i for i in p1.pos_x]
        p1['pos_y_abs'] = [1 * i for i in p1.pos_y]
        all_p = pd.concat([p1,p2],0)

        players = pd.DataFrame(match_data_js['players'])[['id','trackable_object','first_name','last_name','team_id']]
        pos = [match_data_js['players'][i]['player_role']['name'] for i in range(len(players))]
        id_pos = [match_data_js['players'][i]['player_role']['id'] for i in range(len(players))]
        home_away = ['Home' if match_data_js['home_team']['id'] == players['team_id'][i] else 'Away' for i in range(len(players))]
        players['Position'] = pos
        players['id_pos'] = id_pos
        players['Home_Away'] = home_away

        final = all_p.merge(players, how='left', left_on='track_object', right_on='trackable_object' )

        final_home = final[final.Home_Away=='Home'].reset_index(drop=True)
        final_home.reset_index(drop=True, inplace=True)
        final_away = final[final.Home_Away=='Away']
        final_away.reset_index(drop=True, inplace=True)

        return final_home, final_away
    
    def generate_player_match_data(file:str, file2:str, id_player:str)->pd.DataFrame:
        
        '''
            This function create a dataframe with all the events from a tracking data file of an unique player.
            
            Parameters:
                - file: Route of the file that stores the structured data of the match obtained from SkillCorner
                - file2: Route of the file that stores the data of the match obtained from SkillCorner
                - id_player: id of the trackcable object of the player, you can find it on the file2
            
            Returns:
            
                DataFrame with all the events of the match for the player
        
        
        '''
        
    
        with open(file) as f:
                match_js = json.load(f)

        with open(file2) as f2:
                match_data_js = json.load(f2)

        event = 0
        events = []
        for i in tqdm(range(len(match_js))):
            for j in range(len(match_js[i]['data'])):
                try:
                    if match_js[i]['data'][j]['trackable_object'] == id_player:
                        event_id = event +1
                        pos_x = match_js[i]['data'][j]['x']
                        pos_y = match_js[i]['data'][j]['y']
                        time = match_js[i]['time']
                        period = match_js[i]['period']
                        track_object = id_player


                        ev = {'event_id': event_id,
                              'pos_x': pos_x,
                              'pos_y':pos_y,
                              'time': time,
                              'period': period,
                              'track_object': track_object}
                        events.append(ev)
                    else:
                        pass
                except:
                    pass

        match = pd.DataFrame(events)
        p1 = match[match.period == 1]
        p2 = match[match.period == 2]
        p2['pos_x_abs'] = [-1 * i for i in p2.pos_x]
        p2['pos_y_abs'] = [-1 * i for i in p2.pos_y]
        p1['pos_x_abs'] = [1 * i for i in p1.pos_x]
        p1['pos_y_abs'] = [1 * i for i in p1.pos_y]
        all_p = pd.concat([p1,p2],0)

        players = pd.DataFrame(match_data_js['players'])[['id','trackable_object','first_name','last_name','team_id']]
        pos = [match_data_js['players'][i]['player_role']['name'] for i in range(len(players))]
        id_pos = [match_data_js['players'][i]['player_role']['id'] for i in range(len(players))]
        home_away = ['Home' if match_data_js['home_team']['id'] == players['team_id'][i] else 'Away' for i in range(len(players))]
        players['Position'] = pos
        players['id_pos'] = id_pos
        players['Home_Away'] = home_away

        final = all_p.merge(players, how='left', left_on='track_object', right_on='trackable_object' )

        return final
    
class PlotGraphs:
    
    def plot_team_hist(df:pd.DataFrame)->None:
    
        '''
            This function reveices a dataframe and returns an histplot from the x values of all the players

            Parameters:
                df: Pandas dataframe with the team data

            Returns:

                Histogram of th value pos_x_abs

        '''

        plt.figure(figsize=(12,6))
        sns.histplot(df.pos_x_abs)
        plt.title(f'{df.Home_Away[0]} X Position')
        plt.ylabel(None)
        plt.xlabel(None)
        plt.show();
        
    def plot_heatmap_team(df:pd.DataFrame, players:str)->None:
        
        '''
            This function receives a pandas dataframe with all the data of a team created with generate_team_match_data function and returns a
            heatmap mlpsoccer plot with positions of each player of the team and classify the players on a team's tactical line 
            
            Parameters:
            
                df: Pandas dataframe
                players: List of players that want to plot
            
            Return:
            
                Mlpsoccer heatmap
        
        '''
    
        print('Calculando posición de los jugadores en el terreno de juego ...\n')

        start_p = [n for n in df[df.period == 2].sort_values('id_pos').trackable_object.unique() if n in df[df.period == 1].trackable_object.unique()]
        subs = [n for n in df[df.period == 2].sort_values('id_pos').trackable_object.unique() if n not in df[df.period == 1].trackable_object.unique()]

        with plt.xkcd():
            matplotlib.rcParams['font.family'] = ['CENTAUR']
            pitch = Pitch(pitch_type='skillcorner', pitch_length= 105, pitch_width=68, pitch_color='limegreen', 
                      line_color='white', stripe=True, line_zorder=3)

            fig, ax = pitch.draw(figsize=(12,6))

            custcmap = matplotlib.colors.LinearSegmentedColormap.from_list('custom', ['limegreen','green','yellow','gold','orange','orangered','red'])
            kde = pitch.kdeplot(df.pos_x_abs, df.pos_y_abs, fill=True, ax=ax,
                           levels=100,shade=True, shade_lowest=True, cut=4, cmap=custcmap, zorder=1)

            print('Creando Mapa de calor ...\n')

            if players == 'start':
                def_line = 0
                mid_line = 0
                atk_line = 0
                for p in tqdm(start_p):

                    name = df[df.trackable_object == p]['last_name'].values[0]
                    x = round(df[df.trackable_object == p].pos_x_abs.median(),2)
                    y = round(df[df.trackable_object == p].pos_y_abs.median(),2)

                    if df.Home_Away.unique()[0] == 'Away':

                        if 12 < x:
                            pl_clas = 'Defending Line'
                            def_line += 1
                        elif -12 < x < 12:
                            pl_clas = 'Midfield Line'
                            mid_line += 1
                        else:
                            pl_clas = 'Attacking Line'
                            atk_line += 1
                    else:

                        if 12 < x:
                            pl_clas = 'Attacking Line'
                            atk_line += 1
                        elif -12 < x < 12:
                            pl_clas = 'Midfield Line'
                            mid_line += 1
                        else:
                            pl_clas = 'Defending Line'
                            def_line += 1

                    print(f'{name} : {pl_clas} --> ({x},{y})')
                    plt.annotate(f'+ {name}',(x,y), fontsize=20, zorder=4)
                #plt.annotate(f'Initial Squad - Tactic 1-{def_line-1}-{mid_line}-{atk_line}', (-25,35), color='black', fontsize= 20, zorder=4)
                plt.plot([-12,-12],[-35,35] ,color='r', zorder=3)
                plt.plot([12,12],[-35,35] ,color='r', zorder=3)
                plt.title(f'{df.Home_Away.unique()[0]} Team Initial Squad - Tactic 1-{def_line-1}-{mid_line}-{atk_line}', fontsize=25)

                print('\nGuardando imagen ...\n')
                plt.savefig(f'images/{df.Home_Away.unique()[0]}_Team.png')

            else:

                for p in tqdm(subs):
                    name = df[df.trackable_object == p]['last_name'].values[0]
                    x = round(df[df.trackable_object == p].pos_x_abs.median(),2)
                    y = round(df[df.trackable_object == p].pos_y_abs.median(),2)

                    if df.Home_Away.unique()[0] == 'Away':

                        if 12 < x:
                            pl_clas = 'Defending Line'
                        elif -12 < x < 12:
                            pl_clas = 'Midfield Line'
                        else:
                            pl_clas = 'Attacking Line'

                    else:

                        if 12 < x:
                            pl_clas = 'Attacking Line'
                        elif -12 < x < 12:
                            pl_clas = 'Midfield Line'
                        else:
                            pl_clas = 'Defending Line'

                    print(f'{name} : {pl_clas} --> (x:{x}, y:{y})')
                    plt.annotate(f'+ {name}',(x,y), fontsize=20, zorder=4)
                #plt.annotate('Subtitutions', (-15,35), fontsize= 20)

                plt.plot([-12,-12],[-35,35] ,color='r', zorder=3)
                plt.plot([12,12],[-35,35] ,color='r', zorder=3)
                plt.title(f'{df.Home_Away.unique()[0]} Team Subtitutions', fontsize=25)

                print('\nGuardando imagen ...\n')
                plt.savefig(f'images/{df.Home_Away.unique()[0]}_Team_Subtitutions.png')
            plt.show();

    def plot_player_heatmap(df:pd.DataFrame)->None:
        
        '''
            This function receives a pandas dataframe with all the data of a player created with generate_player_match_data function and returns a
            heatmap mlpsoccer plot with position of the player and classify it on a team's tactical line 
            
            Parameters:
            
                df: Pandas dataframe with player data
                
            Return:
            
                Mlpsoccer heatmap
        
        '''
    
        name = df['last_name'][0]
        x = round(df.pos_x_abs.median(),2)
        y = round(df.pos_y_abs.median(),2)

        if df.Home_Away.unique()[0] == 'Away':

            if 12 < x:
                pl_clas = 'Defending Line'
            elif -12 < x < 12:
                pl_clas = 'Midfield Line'   
            else:
                pl_clas = 'Attacking Line'

        else:    
            if 12 < x:
                pl_clas = 'Attacking Line'
            elif -12 < x < 12:
                pl_clas = 'Midfield Line' 
            else:
                pl_clas = 'Defending Line'

        print('Calculando posiciónes del jugadore en el terreno de juego ...\n')
        print('Creando Mapa de calor ...\n')

        with plt.xkcd():
            matplotlib.rcParams['font.family'] = ['CENTAUR']
            pitch = Pitch(pitch_type='skillcorner', pitch_length= 105, pitch_width=68, pitch_color='limegreen', 
                      line_color='white', stripe=False, line_zorder=3)
            fig, ax = pitch.draw(figsize=(12,6))

            custcmap = matplotlib.colors.LinearSegmentedColormap.from_list('custom', ['limegreen','green','yellow', 'gold','orange','orangered','red'])
            kde = pitch.kdeplot(df.pos_x_abs, df.pos_y_abs, fill=True, ax=ax,
                           levels=100, shade_lowest=True, cut=4, cmap=custcmap, zorder=1)

            plt.title(f'{df.first_name[0]} {name} - {pl_clas}', fontsize=25) 
            plt.annotate(f'+ {name}',(x,y), fontsize=20, zorder=4)
            plt.plot([-12,-12],[-35,35] ,color='r', zorder=3)
            plt.plot([12,12],[-35,35] ,color='r', zorder=3)


            print(f'{name} : {pl_clas} --> ({x},{y})')
            print('\nGuardando imagen ...\n')
            plt.savefig(f'images/{df.Home_Away[0]}/{name}_heatmap.png')

            plt.show();