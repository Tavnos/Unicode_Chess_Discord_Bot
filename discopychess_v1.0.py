import discord

class Variables_Method:
    chess_dict= {'pieces_position':{'king':{'black':{'col':0,'row':3,'char_id':9818,'alive':1},'white':{'col':7,'row':4,'char_id':9812,'alive':1}},
                                'queen':{'black':{'col':0,'row':4,'char_id':9819,'alive':1},'white':{'col':7,'row':3,'char_id':9813,'alive':1}},
                                'bishop_1':{'black':{'col':0,'row':2,'char_id':9821,'alive':1},'white':{'col':7,'row':2,'char_id':9815,'alive':1}},
                                'bishop_2':{'black':{'col':0,'row':5,'char_id':9821,'alive':1},'white':{'col':7,'row':5,'char_id':9815,'alive':1}},
                                'knight_1':{'black':{'col':0,'row':1,'char_id':9822,'alive':1},'white':{'col':7,'row':1,'char_id':9816,'alive':1}},
                                'knight_2':{'black':{'col':0,'row':6,'char_id':9822,'alive':1},'white':{'col':7,'row':6,'char_id':9816,'alive':1}},
                                'ruc_1':{'black':{'col':0,'row':0,'char_id':9820,'alive':1},'white':{'col':7,'row':0,'char_id':9814,'alive':1}},
                                'ruc_2':{'black':{'col':0,'row':7,'char_id':9820,'alive':1},'white':{'col':7,'row':7,'char_id':9814,'alive':1}},
                                'pawn_1':{'black':{'col':1,'row':0,'char_id':9823,'alive':1},'white':{'col':6,'row':0,'char_id':9817,'alive':1}},
                                'pawn_2':{'black':{'col':1,'row':1,'char_id':9823,'alive':1},'white':{'col':6,'row':1,'char_id':9817,'alive':1}},
                                'pawn_3':{'black':{'col':1,'row':2,'char_id':9823,'alive':1},'white':{'col':6,'row':2,'char_id':9817,'alive':1}},
                                'pawn_4':{'black':{'col':1,'row':3,'char_id':9823,'alive':1},'white':{'col':6,'row':3,'char_id':9817,'alive':1}},
                                'pawn_5':{'black':{'col':1,'row':4,'char_id':9823,'alive':1},'white':{'col':6,'row':4,'char_id':9817,'alive':1}},
                                'pawn_6':{'black':{'col':1,'row':5,'char_id':9823,'alive':1},'white':{'col':6,'row':5,'char_id':9817,'alive':1}},
                                'pawn_7':{'black':{'col':1,'row':6,'char_id':9823,'alive':1},'white':{'col':6,'row':6,'char_id':9817,'alive':1}},
                                'pawn_8':{'black':{'col':1,'row':7,'char_id':9823,'alive':1},'white':{'col':6,'row':7,'char_id':9817,'alive':1}}},
                  'board_stat':{'black':11035,'white':11036,'board_length':9,'board_list':[],'board_string':'','abc_move_param': {}}}
    def __init__(self):
        self.__chess_dict = self.chess_dict
    def get_var(self):
        return self.__chess_dict
class Board_Method:
    def place_pieces(self):
        for col in range(self.instance_dict['board_stat']['board_length']):
            for row in range(self.instance_dict['board_stat']['board_length']):
                for pieces in self.instance_dict['pieces_position']:
                    for colour in self.instance_dict['pieces_position'][pieces]:
                        if self.instance_dict['pieces_position'][pieces][colour]['row'] == row and self.instance_dict['pieces_position'][pieces][colour]['col'] == col and self.instance_dict['pieces_position'][pieces][colour]['alive'] == 1 :
                            self.instance_dict['board_stat']['board_list'][col][row] = chr(self.instance_dict['pieces_position'][pieces][colour]['char_id'])
    def check_even_odd(self, col_check, row_check, even_odd_check):
        if (((col_check+1)/2)==int((col_check+1)/2) and ((row_check+1)/2)==int((row_check+1)/2)) and even_odd_check==1:
            return True
        if (((col_check+2)/2)==int((col_check+2)/2) and ((row_check+2)/2)==int((row_check+2)/2)) and even_odd_check==2:
            return True
    def enumerate_board(self):
        self.tuple_alphabet = (' '+chr(9398),' '+chr(9399),' '+chr(9400),' '+chr(9401),' '+chr(9402),' '+chr(9403),' '+chr(9404),' '+chr(9405))
        self.tuple_num = (' '+chr(9461),' '+chr(9462),' '+chr(9463),' '+chr(9464),' '+chr(9465),' '+chr(9466),' '+chr(9467),' '+chr(9468))
        for i in range(8):
            self.instance_dict['board_stat']['board_list'][8][i] = self.tuple_alphabet[i]
            self.instance_dict['board_stat']['board_list'][i][8] = self.tuple_num[8-(i+1)] 
            self.instance_dict['board_stat']['board_list'][8][8] = ''
    def draw_board(self):
        self.instance_dict['board_stat']['board_list'] = []
        for i in range(self.instance_dict['board_stat']['board_length']):
            self.instance_dict['board_stat']['board_list'] += [[chr(self.instance_dict['board_stat']['white'])]*(self.instance_dict['board_stat']['board_length']-1)]
        for i in range(self.instance_dict['board_stat']['board_length']): # merge possible
            self.instance_dict['board_stat']['board_list'][i] += [chr(self.instance_dict['board_stat']['white'])]
        for col in range(self.instance_dict['board_stat']['board_length']):
            for row in range(self.instance_dict['board_stat']['board_length']):
                if self.check_even_odd(col,row,1):
                    self.instance_dict['board_stat']['board_list'][col][row] = chr(self.instance_dict['board_stat']['black'])
                elif self.check_even_odd(col,row,2):
                    self.instance_dict['board_stat']['board_list'][col][row] = chr(self.instance_dict['board_stat']['black'])
        self.enumerate_board()
        self.place_pieces()
    def render_board(self):
        self.instance_dict['board_stat']['board_string'] = '' 
        for i in range(self.instance_dict['board_stat']['board_length']):
            self.instance_dict['board_stat']['board_string'] = self.instance_dict['board_stat']['board_string'] + ''.join(self.instance_dict['board_stat']['board_list'][i])
            self.instance_dict['board_stat']['board_string'] = self.instance_dict['board_stat']['board_string'] + ''.join('\n')
        
class Init_Method(Board_Method, Variables_Method):
    def __init__(self):
        self.instance_dict_call = Variables_Method()
        self.instance_dict = self.instance_dict_call.get_var()
        for i in enumerate('abcdefgh'):
            self.instance_dict['board_stat']['abc_move_param'][i[1]] = i[0]
    def check_if_piece(self, abc_row_2, int_col_2):
        if self.instance_dict['board_stat']['board_list'][abs(int_col_2-8)][self.instance_dict['board_stat']['abc_move_param'][abc_row_2]] != chr(self.instance_dict['board_stat']['white']):
            if self.instance_dict['board_stat']['board_list'][abs(int_col_2-8)][self.instance_dict['board_stat']['abc_move_param'][abc_row_2]] != chr(self.instance_dict['board_stat']['black']):
                for col in range(self.instance_dict['board_stat']['board_length']):
                    for row in range(self.instance_dict['board_stat']['board_length']):
                        for pieces in self.instance_dict['pieces_position']:
                            for colour in self.instance_dict['pieces_position'][pieces]:                                                                      
                                if self.instance_dict['pieces_position'][pieces][colour]['row'] == self.instance_dict['board_stat']['abc_move_param'][abc_row_2] and self.instance_dict['pieces_position'][pieces][colour]['col'] == abs(int_col_2-8):                                                                         
                                        self.instance_dict['pieces_position'][pieces][colour]['alive'] = 0
    def move_piece(self, abc_row_1, int_col_1, abc_row_2, int_col_2):
        self.check_if_piece(abc_row_2, int_col_2)
        for piece in self.instance_dict['pieces_position']:
            for colour in self.instance_dict['pieces_position'][piece]:
                if self.instance_dict['pieces_position'][piece][colour]['row'] == self.instance_dict['board_stat']['abc_move_param'][abc_row_1] and self.instance_dict['pieces_position'][piece][colour]['col'] == abs(int_col_1-8):
                    self.instance_dict['pieces_position'][piece][colour]['col'] = abs(int_col_2-8)
                    self.instance_dict['pieces_position'][piece][colour]['row'] = self.instance_dict['board_stat']['abc_move_param'][abc_row_2]
        self.draw_board()
        self.render_board()
        return self.instance_dict['board_stat']['board_string']
    def update_board(self):
        self.draw_board()
        self.render_board()
        return self.instance_dict['board_stat']['board_string']
    def rez_piece(self, abc_row_1, int_col_1, piece_name, piece_color):
        for col in range(self.instance_dict['board_stat']['board_length']):
            for row in range(self.instance_dict['board_stat']['board_length']):
                for pieces in self.instance_dict['pieces_position']:
                    if piece_name == pieces:
                        for colour in self.instance_dict['pieces_position'][piece_name]:
                            if piece_color == colour:
                                self.instance_dict['pieces_position'][piece_name][piece_color]['row'] = self.instance_dict['board_stat']['abc_move_param'][abc_row_1]
                                self.instance_dict['pieces_position'][piece_name][piece_color]['col'] = abs(int_col_1-8)
                                self.instance_dict['pieces_position'][piece_name][piece_color]['alive'] = 1
        self.draw_board()
        self.render_board()
        return self.instance_dict['board_stat']['board_string']
    def call_piece_name(self):
        ls_call = []
        str_call = ''
        for pieces in self.instance_dict['pieces_position']:
            ls_call += [pieces]
        self.str0_call = "To move pieces type the location of the piece and destination (!move b 1 c 3)"
        self.str1_call = "To restore pieces type the location, name and colour (!rez g 8 knight_2 black)"
        self.str2_call = ' , '.join(ls_call)

        return "{} \n {} \n The names of the different callable pieces are: {}".format(self.str0_call, self.str1_call , self.str2_call)



main_init = Init_Method()
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!chess'):
        channel = message.channel
        msg = '{}'.format(main_init.update_board())
        await channel.send(msg)
    elif message.content.startswith('!move'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!move ','')
        a_str = new_str.split()
        msg = '{}'.format(main_init.move_piece(a_str[0], int(a_str[1]), a_str[2], int(a_str[3])))
        await channel.send(msg)
        
    elif message.content.startswith('!help'):
        channel = message.channel
        msg = '{}'.format(main_init.call_piece_name())
        await channel.send(msg)
        
    elif message.content.startswith('!rez'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!rez ','')
        a_str = new_str.split()
        msg = '{}'.format(main_init.rez_piece(a_str[0], int(a_str[1]), a_str[2], a_str[3]))
        await channel.send(msg)
        
@client.event
async def on_ready():
    print('Funcky parmesan cheese')
    print(client.user.name)
    print(client.user.id)
    print('-------------')
    

client.run('NzU4NzMzMzA1MzYwMTU0NjM2.X2zPdA.-IGWFv__V655uMpspxhxzKuXVYY')