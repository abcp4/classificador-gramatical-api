import re

substituicoes = {
    # 'o, a, os, as' (exceto pronomes) e 'um, uma, uns, umas' como Artigos
    'det_artigos': (r'(?i)(\b([oa]|u((ma?)|n))s?/)[^P]\w+\b', r'\1ARTIGO'),
    # Pronomes (e outros?) classificados como DET passam para Pronomes
    'det_pronomes': (r'(?i)(\b\w{3,}/)DET\b', r'\1PRONOME'),
    # 'tu' e 'te' como Pronomes
    '2ap_pronome': (r'(?i)(\bt[ue]/)\S+\b', r'\1PRONOME'),
    # 'comigo, contigo, conosco, convosco' como Pronomes
    'com_pronome': (r'(?i)(\bco((m|nt)ig|nv?osc)o/)\S+\b', r'\1PRONOME'),
    # 'à, às, ao, aos' como Preposição+Artigo
    'a_art_prep': (r'(?i)(\b(à|ao)s?/)\S+\b', r'\1PREPOSIÇÃO#ARTIGO'),
    # 'do, da, dos das'; 'no, na, nos, nas'; 'pelo, pela, pelos, pelas'; 'pro, pra, pros, pras' como Preposição+Artigo
    'de_em_art_def_prep': (r'(?i)(\b((p(r|el)|[dn])[oa]s?)/)\S+\b', r'\1PREPOSIÇÃO#ARTIGO'),
    # 'dum, duma, duns, dumas', 'num, numa...' como Preposição+Artigo
    'de_em_art_indef_prep_': (r'(?i)(\b[dn]u(m(as?)?|ns)/)\S+\b', r'\1PREPOSIÇÃO#ARTIGO'),
    # 'àquilo, àquele, àqueles, àquela, àquelas' como Preposição+Pronome
    'à_aquele': (r'(?i)(\b(àquel[ea]s?|àquilo)/)\S+\b', r'\1PREPOSIÇÃO#PRONOME'),
    # Contração de 'de' e 'em' com aquele, este, isto, aquilo, outro e variações como Preposição+Pronome
    'de_em_pron_demonstr': (r'(?i)(\b[dn](((aqu)?el[ea]s?)|(es[ts][ea]s?)|is[st]o|aquilo|outr[oa]s?)/)\S+\b', r'\1PREPOSIÇÃO#PRONOME'),
    # Contração de 'de' e 'aí, ali, aqui' como Preposição+ Advérbio
    'de_adv': (r'(?i)(\bd(aqui|aí|ali)/)\S+\b', r'\1PREPOSIÇÃO#ADVÉRBIO'),
    # Situações de ênclise como Verbo+Pronome
    'enclise': (r'(?i)(\w+-([mts]e|lhes?|[lnv][oa]s?)/)\S+\b', r'\1VERBO#PRONOME'),
    # Situações de mesóclise como Verbo+Pronome+Desinência
    'mesoclise': (r'(?i)(\w+-([mts]e|lhes?|[lnv][oa]s?)(-\w+)/)\S+\b', r'\1VERBO#PRONOME#DESINENCIA'),
    # Forçando 'aquele' e variações classificados como Adjetivos para Pronomes
    'aquele_pronome': (r'(?i)(\baquel[ea]s?/)\S+\b', r'\1PRONOME'),
    # Forçando 'de' e 'para' a ser Preposição
    'de_para_prep': (r'(?i)(\b(de|pa?ra)\b/)\S+', r'\1PREPOSIÇÃO'),
    # Forçando 'ante' e 'dentre' como Preposição
    'ante_dentre_prep': (r'(?i)(\b(ante|dentre)/)\S+\b', r'\1PREPOSIÇÃO'),
    # Forçando 'devagar' e 'trás' como Advérbio
    'devagar_trás_adv': (r'(?i)(\b(devagar|trás)/)\S+\b', r'\1ADVÉRBIO'),
    # Forçando 'sã' e 'lindos' como Adjetivo
    'sã_lindos_adjetivo': (r'(?i)(\b(sã|lindos)/)\S+\b', r'\1ADJETIVO'),
    # Forçando 'talvez' como Advérbio
    'talvez_adverbio': (r'(?i)(\btalvez/)\S+\b', r'\1ADVÉRBIO'),
    # Forçando 'tomara' como Interjeição
    'tomara_interjeição': (r'(?i)(\btomara/)\S+\b', r'\1INTERJEIÇÃO'),
    # Forçando 'remos' e como Substantivo
    'remos_substantivo': (r'(?i)(\bremos/)\S+\b', r'\1SUBSTANTIVO'),
    # Forçando 'extremos' como Adjetivo
    'extremos_adjetivo': (r'(?i)(\bextremos/)\S+\b', r'\1ADJETIVO'), # "Os extremos..."
    # Forçando 'roeu' como Verbo
    'roeu_verbo': (r'(?i)(\broeu/)\S+\b', r'\1VERBO'),
    # Forçando 'perto' e 'longe' como Advérbio
    'longe_perto_advérbio': (r'(?i)(\b(longe|perto)/)\S+\b', r'\1ADVÉRBIO'),
    # Forçando números como Numerais
    'numeros_numerais': (r'(?i)(\b\d+/)\S+\b', r'\1NUMERAL'),
    # Forçando 'cada' como Pronome
    'cada_pronome': (r'(?i)(\bcada/)\S+\b', r'\1PRONOME'),
    # Forçando 'oi' e 'olá' como Interjeição
    'oi_ola_interjeicao': (r'(?i)(\b(oi|olá)/)\S+\b', r'\1INTERJEIÇÃO'),
    # Forçando numerais classificados como adjetivos a serem numerais
    'num_adj_numerais_1': (r'(?i)(\b(primeir|segund|terceir|quart|quint|sext|sétim|oitav|non)[oa]s?/)\S+\b', r'\1NUMERAL'), # ver 'Vou sair na quarta'
    'num_adj_numerais_2': (r'(?i)(\b(décim|(vi|tri|quadra|quinqua|sexa|hepta|octa|nona)gésim|(cent|mil)ésim)[oa]s?/)\S+\b', r'\1NUMERAL'), # Faltam: milhão etc.
    # Mudando Verbo-do e variações (Particípio) para Adjetivo
    'participio_adjetivo': (r'(?i)(\b\w+[^n\s]d[oa]s?/)VERB\b', r'\1ADJETIVO'),
    # Muda verbo-adjetivo para verbo-advérbio (errou feio)
    'v_adj': (r'(?i)(\b\w+/VERB\s\w+/)ADJ', r'\1ADVÉRBIO'),

    'somos_refens': (r'(?i)(\bsomos\b/)\S+(\s\breféns\b/)\S+', r'\1VERBO\2ADJETIVO'),
    'e_breve': (r'(?i)(\bé\b/)\S+(\s\bbreve\b/)\S+', r'\1VERBO\2ADJETIVO'),
    'um_sim': (r'(?i)(\bum\b/)\S+(\s\bsim\b/)\S+', r'\1ARTIGO\2SUBSTANTIVO'),

    # Forçando'no entanto' como Conjunção
    'no_entanto': (r'(?i)(\bno\b/)\S+(\s\bentanto\b/)\S+',
                   r'\1CONJUNÇÃO\2CONJUNÇÃO'),
    # Forçando'às vezes' como Conjunção
    'as_vezes': (r'(?i)(\bàs\b/)\S+(\s\bvezes\b/)\S+',
                   r'\1CONJUNÇÃO\2CONJUNÇÃO'),
    # Forçando'posto que' como Conjunção
    'posto_que': (r'(?i)(\bposto\b/)\S+(\s\bque\b/)\S+',
                   r'\1CONJUNÇÃO\2CONJUNÇÃO'),
    # Forçando'por isso' como Conjunção
    'por_isso': (r'(?i)(\bpor\b/)\S+(\s\bisso\b/)\S+',
                   r'\1CONJUNÇÃO\2CONJUNÇÃO'),
    # Forçando'por conseguinte' como Conjunção
    'por_conseguinte': (r'(?i)(\bpor\b/)\S+(\s\bconseguinte\b/)\S+',
                   r'\1CONJUNÇÃO\2CONJUNÇÃO'),
    # Forçando'de novo' como Advérbio
    'de_novo': (r'(?i)(\bde\b/)\S+(\s\bnovo\b/)\S+',
                   r'\1ADVÉRBIO\2ADVÉRBIO'),
    # Forçando'debaixo de' como Advérbio
    'debaixo_de': (r'(?i)(\bdebaixo\b/)\S+(\s\bde\b/)\S+',
                   r'\1ADVÉRBIO\2ADVÉRBIO'),
    # Forçando'a gente' como Pronome
    'a_gente': (r'(?i)(\ba\b/)\S+(\s\bgente\b/)\S+',
                   r'\1PRONOME\2PRONOME'),
    # Forçando'por que' como Pronome
    'por_que': (r'(?i)(\bpor\b/)\S+(\s\bque\b/)\S+',
                   r'\1PRONOME\2PRONOME'),
    # Forçando'com quem, por quem, de quem' como Pronome
    'com_quem_etc': (r'(?i)(\b(com|por|de\b/))\S+(\s\bquem\b/)\S+', # correção da expressão regular
                   r'\2PRONOME\3PRONOME'),
    # Forçando'de qual, de quais' como Pronome
    'de_qual': (r'(?i)(\bde\b/)\S+(\squa(is|l)\b/)\S+',
                   r'\1PRONOME\2PRONOME'),
    # Forçando'o qual,os quais,a qual,as quais,do qual,dos quais,da qual,das quais,no qual,nos quais,na qual,nas quais' como Pronome
    'o_qual_etc': (r'(?i)(\b[dn]?[oa]?s\b/)\S+(\squa(is|l)\b/)\S+',
                   r'\1PRONOME\2PRONOME'),
    # Forçando'por qual,por quais,com qual,com quais' como Pronome
    'por_qual_etc': (r'(?i)(\b(por|com)\b/)\S+(\s\bqua(l|is)\b/)\S+',
                   r'\1PRONOME\3PRONOME'),
    # Forçando'em cima de' como Advérbio
    'em_cima_de': (r'(?i)(\bem\b/)\S+(\s\bcima\b/)\S+(\s\bde\b/)\S+',
                   r'\1ADVÉRBIO\2ADVÉRBIO\3ADVÉRBIO'),
    # Forçando'nós' como Substantivo
    'os_nós': (r'(?i)(\bos\b/)\S+(\s\bnós\b/)\S+',
                   r'\1ARTIGO\2SUBSTANTIVO'),
    # Forçando 'X/VERB embora' como Advérbio
    'verbo_embora':(r'(?i)(\b\w+\b/)VERB(\s\bembora\b/)\S+',
                   r'\1VERBO\2ADVÉRBIO'),
    # Forçando 'o,a,os,as X/VERB' como Pronome
    'clitico_3a_verbo':(r'(?i)(\b[oa]s?\b/)\S+(\s\b\w+[^r]/)VERB\S*',
                   r'\1PRONOME\2VERBO'),
    # Forçando 'nos X/VERB' como Pronome
    'nos_X/VERB':(r'(?i)(\bnos\b/)\S+(\s\b\w+[^r]/)VERB\S*',
                   r'\1PRONOME\2VERBO'),
    # Forçando 'X/SUBST Y/SUBST' como Adjetivo
    'X/SUBST_Y/SUBST':(r'(?i)(\b\w+\b/)NOUN(\s\b\w+/)NOUN\S*',
                   r'\1SUBSTANTIVO\2ADJETIVO'),
    # Forçando 'me X/SUBST' como Verbo
    'me_X/SUBST':(r'(?i)(\bme\b/)\S+(\s\b\w+/)NOUN\S*',
                   r'\1PRONOME\2VERBO'),
    # Forçando 'X/AUX Y/SUBST' como Adjetivo
    'X/AUX_Y/SUBST':(r'(?i)(\b\w+/)AUX\S*(\s\b\w+/)NOUN\S*',
                      r'\1VERBO#LIGAÇÃO\2ADJETIVO'),
    # Forçando 'ser, estar/AUX X/ADJ' como VERBO#LIGAÇÃO
    'ser_estar_X/ADJ':(r'(?i)(\b\w+/)AUX\S*(\s\b\w+/)ADJ\S*',
                   r'\1VERBO#LIGAÇÃO\2ADJETIVO'),
    # Forçando 'quando,onde'como Pronome
    'quando_onde':(r'(\b(Quando|Onde)\b/)\S+', r'\1PRONOME'),

    # Forçando classificação errada de substantivos como verbos
    'casa_etc': (r'(?i)(\b(casa|abraço|morro|debate|canto)\b/)NOUN/ROOT',
                 r'\1VERBO'),
    # Forçando classificação de verbos de 1a pessoa
    'eu_como_etc': (r'(?i)(\beu\b\S+\s)(\b(com|abraç|acord|caminh|viv|morr|cant|precis)o\b/)\S+',
                    r'\1\2VERBO'),
    # Forçando classificação de verbos de 3a pessoa
    'ele_casa_etc': (r'(?i)(\bel[ea]\b\S+\s)(\b(casa|sobre|debate|era)\b/)\S+',
                    r'\1\2VERBO'),
    # Forçando era como substantivo
    'a_uma_era': (r'(?i)(\b(um)?a\b\S+\s)(\bera\b/)\S+', r'\1\3SUBSTANTIVO'),

    # Forçando 'pavê' a ser Substantivo
     'pavê_substantivo': (r'(?i)(\bpavê\b/)\S+\b', r'\1SUBSTANTIVO'),

     # Forçando 'menino, menina' a ser Substantivo
     'menino_substantivo': (r'(?i)(\bmenin[oa]\b/)\S+\b', r'\1SUBSTANTIVO'),

    # Transformando as etiquetas de UD nas da gramática tradicional
    # Tem que vir no final se não as regras det_pronomes, participio_adjetivo não funcionam
    'det_artigo': (r'DET\b', r'ARTIGO'),
    'noun_substantivo': (r'NOUN\b', r'SUBSTANTIVO'),
    'propn_nome_proprio': (r'PROPN\b\S*', r'NOME#PRÓPRIO'), # acréscimo de \S*
    'verb_verbo': (r'VERB\b', r'VERBO'),
    'adj_adjetivo': (r'ADJ\b', r'ADJETIVO'),
    'adv_advérbio': (r'ADV\b', r'ADVÉRBIO'),
    'num_numeral': (r'NUM\b', r'NUMERAL'),
    'pron_pronome': (r'PRON\b', r'PRONOME'),
    'adp_preposição': (r'ADP\b', r'PREPOSIÇÃO'),
    'scconj_conjunção': (r'[CS]CONJ\b', r'CONJUNÇÃO'),
    'intj_interjeição': (r'INTJ\b', r'INTERJEIÇÃO'),
    'aux_auxiliar': (r'AUX\b', r'AUXILIAR'),
    'sym_simb': (r'SYM\b', r'SIMB'),
    'punct_pontuação': (r'PUNCT\b', r'PONTUAÇÃO'),
    'X_outros': (r'/X\b', r'/OUTROS'),
          }
