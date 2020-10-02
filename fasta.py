import discord
import time 


class Translation:
    adenine = {'char':'a','dna':'a','match':'t','rna':'a'}
    guanine = {'char':'g','dna':'g','match':'c','rna':'g'}
    cytosine = {'char':'c','dna':'c','match':'g','rna':'c'}
    thymine = {'char':'t','dna':'t','match':'a','rna':'u'}
    uracil = {'char':'u','dna':'t','match':'a','rna':'u'}
    methionine = {'config':('atg'),'name':'Methionine','letter_code':'M','tri_char':'Met','amino_class':'sulfuric','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':1.9,'amino_weight':149.208}
    leucine = {'config':('tta','ttg','ctt','ctc','cta','ctg'),'name':'leucine','letter_code':'L','tri_char':'Leu','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':3.8,'amino_weight':131.175}
    phenylalanine = {'config':('ttt','ttc'),'name':'phenylalanine','letter_code':'F','tri_char':'Phe','amino_class':'aromatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':2.8,'amino_weight':165.192}
    serine = {'config':('tct','tcc','tca','tcg','agc','agt'),'name':'serine','letter_code':'S','tri_char':'Ser','amino_class':'hydroxylic','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':1.9,'amino_weight':149.208}
    cysteine = {'config':('tgt','tgc'),'name':'cysteine','letter_code':'C','tri_char':'Cys','amino_class':'sulfuric','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':2.5,'amino_weight':121.154}
    tryptophan = {'config':('tgg'),'name':'tryptophan','letter_code':'W','tri_char':'Trp','amino_class':'aromatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':-0.9,'amino_weight':204.228}
    proline = {'config':('ccc','cca','cct','ccg'),'name':'proline','letter_code':'P','tri_char':'Pro','amino_class':'cyclic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':-1.6,'amino_weight':115.132}
    histidine = {'config':('cat','cac'),'name':'histidine','letter_code':'H','tri_char':'His','amino_class':'basic-aromatic','amino_polarity':'basic-polar','amino_charge':'neutral-positive','amino_hydropathy':-3.2,'amino_weight':155.156}
    glutamine = {'config':('caa','cag'),'name':'glutamine','letter_code':'Q','tri_char':'Gln','amino_class':'amide','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':-3.5,'amino_weight':146.146}
    arginine = {'config':('cgg','cgt','cgc','cga','agg','aga'),'name':'arginine','letter_code':'R','tri_char':'Arg','amino_class':'basic','amino_polarity':'basic-polar','amino_charge':'positive','amino_hydropathy':-4.5,'amino_weight':174.203}
    isoleucine = {'config':('att','atc','ata'),'name':'isoleucine','letter_code':'I','tri_char':'Ile','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':4.5,'amino_weight':131.175}
    valine = {'config':('gtg','gtt','gtc','gta'),'name':'valine','letter_code':'V','tri_char':'Val','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':4.2,'amino_weight':117.148}
    tyrosine = {'config':('tat','tac'),'name':'tyrosine','letter_code':'Y','tri_char':'Tyr','amino_class':'aromatic','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':-1.3,'amino_weight':181.191}
    threonine = {'config':('aca','acc','act','acg'),'name':'threonine','letter_code':'T','tri_char':'Thr','amino_class':'hydroxylic','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':-0.7,'amino_weight':119.119}
    alanine = {'config':('gcg','gcc','gct','gca'),'name':'alanine','letter_code':'A','tri_char':'Ala','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':1.8,'amino_weight':89.094}
    asparagine = {'config':('aat','aac'),'name':'asparagine','letter_code':'N','tri_char':'Asn','amino_class':'amide','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':-3.5,'amino_weight':132.119}
    lysine = {'config':('aaa','aag'),'name':'lysine','letter_code':'K','tri_char':'Lys','amino_class':'basic','amino_polarity':'basic-polar','amino_charge':'positive','amino_hydropathy':-3.9,'amino_weight':146.189}
    glutamic = {'config':('gaa','gag'),'name':'glutamic','letter_code':'E','tri_char':'Glu','amino_class':'acidic','amino_polarity':'acidic-polar','amino_charge':'negative','amino_hydropathy':-3.5,'amino_weight':147.131}
    aspartic = {'config':('gat','gac'),'name':'aspartic','letter_code':'D','tri_char':'Asp','amino_class':'acidic','amino_polarity':'acidic-polar','amino_charge':'negative','amino_hydropathy':-3.5,'amino_weight':133.104}
    glycine = {'config':('ggg','gga','ggc','ggt'),'name':'glycine','letter_code':'G','tri_char':'Gly','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':-0.4,'amino_weight':133.104}
    ochre = {'config':('taa'),'name':'Ochre','letter_code':'X','tri_char':'_Ochre','amino_class':'Stop','amino_polarity':None,'amino_charge':None,'amino_hydropathy':None,'amino_weight':0}
    amber = {'config':('tag'),'name':'Amber','letter_code':'B','tri_char':'_Amber','amino_class':'Stop','amino_polarity':None,'amino_charge':None,'amino_hydropathy':None,'amino_weight':0}
    opal = {'config':('tga'),'name':'Opal','letter_code':'Z','tri_char':'_Opal','amino_class':'Stop','amino_polarity':None,'amino_charge':None,'amino_hydropathy':None,'amino_weight':0}
    nucleotide = (adenine,guanine,cytosine,thymine,uracil)
    amino_acids = (methionine,leucine,phenylalanine,serine,cysteine,tryptophan,proline,histidine,glutamine,arginine,isoleucine,valine,tyrosine,threonine,alanine,asparagine,lysine,glutamic,aspartic,glycine,ochre,amber,opal)
    def __init__(self, dna_input):
        self.dna_typed = []
        self.rna_typed = []
        self.direct_start_index = []
        self.reversed_start_index = []
        self.direct_sequences = []
        self.stopped_chains_list = []
        self.translated_chains_letter = [] 
        self.possible_chain = {}
        self.stopped_chains = {}
        self.codon_result_dict = {}
        self.chain_result_dict = {}
        self.dna_transcript = dna_input.lower()
        for i in range(len(dna_input)):
            for f in range(len(self.nucleotide)):
                if self.dna_transcript[i] in self.nucleotide[f]['char']:
                    self.dna_typed.append(self.nucleotide[f]['dna'])
                    self.rna_typed.append(self.nucleotide[f]['rna'])
        self.chain_sequence = ''.join(self.dna_typed)
        self.dna_typed.reverse()
        self.reversed_sequence = ''.join(self.dna_typed)
        self.dna_typed.reverse()
        for i in range(len(self.chain_sequence)):
            if self.chain_sequence[i:i+3] == self.methionine['config']:
                self.direct_start_index.append(i)
        for i in range(len(self.reversed_sequence)):
            if self.reversed_sequence[i:i+3] == self.methionine['config']:
                self.reversed_start_index.append(i)
        for i in range(len(self.direct_start_index)):
            index_var = self.direct_start_index[i]
            self.direct_sequences.append(self.chain_sequence[index_var:])
        for i in range(len(self.reversed_start_index)):
            index_var = self.reversed_start_index[i]
            self.direct_sequences.append(self.reversed_sequence[index_var:])
        for i in range(len(self.direct_sequences)):
            chain_names = "chain{}".format(i)
            for f in range(len(self.direct_sequences[i])):
                self.possible_chain[chain_names] = [self.direct_sequences[i][f:f+3] for f in range(0, len(self.direct_sequences[i]), 3)]
            for f in range(len(self.possible_chain[chain_names])):
                codon = self.possible_chain[chain_names][f]
                if codon == self.opal['config'] or codon == self.amber['config'] or codon == self.ochre['config']:
                    stop_index = self.possible_chain[chain_names].index(codon)+1
                    self.stopped_chains[chain_names] = self.possible_chain[chain_names][0:stop_index]
        for i in self.stopped_chains:
            self.stopped_chains_list.append(self.stopped_chains[i])
        for i in range(len(self.stopped_chains_list)):
            self.translated_chains_letter.append([])
            for f in range(len(self.stopped_chains_list[i])):
                for k in range(len(self.amino_acids)):
                    if self.stopped_chains_list[i][f] in self.amino_acids[k]['config']:
                        self.translated_chains_letter[i].append(self.amino_acids[k]['letter_code'])
        for i in range(len(self.translated_chains_letter)):
            self.chain_result_dict['peptide_{}'.format(i+1)] = ''.join(self.translated_chains_letter[i])
        for i in range(len(self.stopped_chains_list)):
            self.codon_result_dict['peptide_{}'.format(i+1)] = ''.join(self.stopped_chains_list[i])
    def get_translation(self):
        self.out_1 = ("cDNA: {}".format(''.join(self.dna_typed)))
        self.out_2 = ("mRNA: {}".format(''.join(self.rna_typed)))
        self.out_3 = ("Reversed DNA sequence: {}".format(self.reversed_sequence))
        self.out_4 = ("Peptides Letter: {}".format(self.chain_result_dict))
        self.out_5 = ("Peptides Codons: {}".format(self.codon_result_dict))
        return '{},\n{},\n{},\n{},\n{}'.format(self.out_1, self.out_2, self.out_3, self.out_4, self.out_5)

help_1 = '```'
help_2 =  '###########################################'
help_3 =  '#  .He1p !Commands index                  #'
help_4 =  '###########################################'
help_5 =  '#  Conversions: f2m m2f m2km m2km i2m m2i #'
help_6 =  '###########################################'
help_7 =  '#  Eastern standard time: est             #'
help_8 =  '###########################################'
help_9 =  '#  Scale unit system: scale               #'
help_10 = '###########################################'
help_11 = '#  DNA/RNA to Protein translation: tr     #'
help_12 = '###########################################'
help_13 = '#  Links: plasmidclub journalclub library #'
help_14 = '###########################################```'
def get_help():
    return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(help_1, help_2, help_3, help_4, help_5, help_6, help_7, help_8, help_9, help_10, help_11, help_12, help_13, help_14)



jclub_1 = 'https://youtu.be/4Qf6eLCdL_Q'
jclub_2 = 'https://youtu.be/H4nxDmWbjwU'
jclub_3 = 'https://youtu.be/OKl6N-jzoSw'
jclub_4 = 'https://youtu.be/eDHdK5bGkpg'
jclub_5 = 'https://youtu.be/VDrM-N8yTqc'
jclub_6 = 'https://youtu.be/NfBLW5qgIIU'
jclub_7 = 'https://youtu.be/xzUVmeDNbMM'
def get_journal_club():
    return '{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(jclub_1, jclub_2, jclub_3,jclub_4, jclub_5, jclub_6, jclub_7)


pclub_1 = '```'
pclub_2 = '#################################'
pclub_3 = '#  https://youtu.be/zlGy9YHAK3A #'
pclub_4 = '#################################'
pclub_5 = '#  https://youtu.be/pqCZobaBcWM #'
pclub_6 = '#################################```'
def get_plasmid_club():
    return '{}\n{}\n{}\n{}\n{}\n{}'.format(pclub_1, pclub_2, pclub_3, pclub_4, pclub_5, pclub_6)

rawr_1 = '𒁂𐦠𑀕𐡔Ꝛ෴'
def get_rawr():
    return '{}'.format(rawr_1)

plib_1 = 'https://drive.google.com/drive/folders/1inAhfU9W18A83YqVI6A5uFO8eHyeKC3W'
def get_library():
    return '{}'.format(plib_1)

def get_est_time():
    tim_fx = time.asctime()
    prev_tim = tim_fx.split()[3][0:2]
    new_fx = str(int(tim_fx.split()[3][0:2])-6)
    tim_fx_n = tim_fx.replace(prev_tim, new_fx)
    return tim_fx_n

def km_miles(kilometer):
    return round(kilometer * 0.621371, 4)
def miles_km(miles):
    return round(miles / 0.621371, 4)
def meter_feet(meter):
    return round(meter / 0.3048, 4)
def feet_meter(feet):
    return round(feet * 0.3048, 4)
def inch_meter(meter):
    return round(meter / 39.3701, 4)
def meter_inch(inch):
    return round(inch * 39.3701, 4)

help_scale_1 = 'Units prefixes and scale of measures'
help_scale_2 = 'Prefix, Symbol, Scale & formulation'
help_scale_3 = ' tera-,    T   1.000.000.000.000 or 10^12'
help_scale_4 = ' giga-,    G   1.000.000.000 or 10^9'
help_scale_5 = ' mega-,    M   1.000.000 or 10^6'
help_scale_6 = ' kilo-,    k   1.000 or 10^3'
help_scale_7 = ' deci-,    d   0.1 or 1/10 or 10^-1'
help_scale_8 = ' centi-,   c   0.01 or 1/10 or 10^-2'
help_scale_9 = ' milli-,   m   0.001 or 1/10 or 10^-3'
help_scale_10 =' micro-,   µ   0.0001 or 1/10 or 10^-6'
help_scale_11 =' nano-,    n   1/1.000.000.000 or 10^-9'
help_scale_12 =' pico-,    p   1/1.000.000.000.000 or 10^-12'

def get_scale():
    return '{}:\n{}\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{},\n{}'.format(help_scale_1, help_scale_2, help_scale_3, help_scale_4, help_scale_5, help_scale_6, help_scale_7, help_scale_8, help_scale_9, help_scale_10, help_scale_11, help_scale_12)
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!tr'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!tr ','')
        translate_choice = Translation(new_str)
        get_translated = translate_choice.get_translation()
        msg = '{}'.format(get_translated)
        await channel.send(msg)
    elif message.content.startswith('!km2m'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!km2m ','')
        msg = '{} Kilometer is {} Miles'.format(float(new_str), km_miles(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!m2km'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!m2km ','')
        msg = '{} Miles is {} Kilometer'.format(float(new_str), miles_km(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!f2m'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!f2m ','')
        msg = '{} Feet is {} Meter'.format(float(new_str), feet_meter(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!m2f'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!m2f ','')
        msg = '{} Meter is {} Feet'.format(float(new_str), meter_feet(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!m2i'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!m2i ','')
        msg = '{} Meter is {} Inch'.format(float(new_str), meter_inch(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!i2m'):
        channel = message.channel
        new_str = message.content
        new_str = new_str.replace('!i2m ','')
        msg = '{} Inch is {} Meter'.format(float(new_str), inch_meter(float(new_str)))
        await channel.send(msg)
    elif message.content.startswith('!scale'):
        channel = message.channel
        eastern_time = get_est_time()
        msg = '{}'.format(get_scale())
        await channel.send(msg)
    elif message.content.startswith('!rawr'):
        channel = message.channel
        eastern_time = get_est_time()
        msg = '{}'.format(get_rawr())
        await channel.send(msg)
    elif message.content.startswith('.help'):
        channel = message.channel
        eastern_time = get_est_time()
        msg = '{}'.format(get_help())
        await channel.send(msg)
    elif message.content.startswith('!journalclub'):
        channel = message.channel
        eastern_time = get_est_time()
        msg = '{}'.format(get_journal_club())
        await channel.send(msg)
    elif message.content.startswith('!plasmidclub'):
        channel = message.channel
        eastern_time = get_est_time()
        msg = '{}'.format(get_plasmid_club ())
        await channel.send(msg)
    elif message.content.startswith('!library'):
        channel = message.channel
        eastern_time = get_est_time()
        msg = '{}'.format(get_library())
        await channel.send(msg)
    elif message.content.startswith('!est'):
        channel = message.channel
        eastern_time = get_est_time()
        msg = 'Eastern Standard Time: \n{}'.format(eastern_time)
        await channel.send(msg)
        
@client.event
async def on_ready():
    print('Funcky parmesan cheese')
    print(client.user.name)
    print(client.user.id)
    print('-------------')
    

client.run('NzU4NzMzMzA1MzYwMTU0NjM2.X2zPdA.NVSORnjJr-QG2_SSChial30h5PU')