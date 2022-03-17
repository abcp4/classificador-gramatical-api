import random

messages = [
"#explicando_1- O Classificador Gramatical é baseado na biblioteca Spacy que, por sua vez, foi construída utilizando o projeto Universal Dependencies.",
"#explicando_2- Classificar palavras é difícil... Tem contexto, tem ambiguidades, mas a gente chega lá!",
"#explicando_3- Para chegar nesse nível de acertos, foi preciso testar MUITO (e ainda precisa testar MAIS).",
"#explicando_4- Substantivos e adjetivos são as palavras mais difíceis de classificar...",
"#explicando_5- Lembre-se: o Classificador funciona melhor no gênero escrito formal culto.",
"#explicando_6- Aqui (https://github.com/UniversalDependencies/UD_Portuguese-Bosque) você encontra informações sobre a participação brasileira no projeto Universal Dependencies.",
"#explicando_7- Muitas adaptações foram feitas pelos membros do projeto na versão original de etiquetagem do Spacy.",
"#explicando_8- Etiquetagem é o termo técnico utilizado na área para a classificação gramatical de uma palavra.",
"#explicando_9- O Classificador Gramatical se insere na área de Processamento de Linguagem Natural (PLN).",
"#momento_linguistíco_1- O preconceito linguístico é uma forma de preconceito a determinadas variedades linguísticas.",
"#momento_linguistíco_2-Para a linguística os chamados <erros> gramaticais não existem nas línguas naturais.",
"#momento_linguistíco_3- A língua escrita e a língua falada são coisas bem diferentes- a escrita tende a ser estática, já a segunda está sempre variando a cada nova geração.",
"#momento_linguistíco_4- Um sistema de escrita é UMA representação da fala, não A representação da fala.",
"#momento_linguistíco_5- Palavras mudam de classe porque podem assumir novos sentidos exigidos por mudanças extralinguísticas.",
"#momento_linguistíco_6- <Menos> nem sempre é advérbio: em <menos queijo>, está modificando um substantivo e é um pronome. E se pronomes variam, falar <menas manteiga> até que faz sentido…",
"#momento_linguistíco_7- Regularizar formas irregulares é uma atividade comum na aquisição da linguagem e também em registros cotidianos.",
"#momento_linguistíco_8- Em <vamos sair>, <vamos> é auxiliar e <sair> principal. Assim, em <vamos ir>, não há redundância- temos um auxiliar e um principal também.",
"#momento_linguistíco_9- A prática do preconceito linguístico não tem fundamento científico e é tão abominável quanto os demais preconceitos.",
"#momento_linguistíco_10- Marcos Bagno é um dos principais autores sobre a questão do preconceito linguístico. Procure por livros dele na Editora Parábola!",
"#momento_linguistíco_11- Sociolinguística é uma corrente linguística que estuda como e por que as línguas variam e as consequências dessa variação na sociedade.",
"#momento_linguistíco_12- Sociolinguística Educacional é o ramo da Sociolinguística que investiga como podemos abordar a questão da variação linguística em sala de aula.",
"#momento_linguistíco_13- Táuba, pobrema, iorgute… essas palavras te assustam? Baixa <Isso não é uma gramática> na Playstore para ver explicações numa linguagem bem informal!",
"#momento_linguistíco_14- Como as línguas mudam? Muitos estudiosos apostam que as crianças são responsáveis pela mudança, reinterpretando estruturas e criando novas análises!",
"#momento_linguistíco_15- Por que falam iorgute? Para criar um par de sílabas com a mesma estrutura (gu.te), isso se chama harmonizar a estrutura da palavra.",
"#momento_linguistíco_16- Em <os menino>, <menino> está no plural (claro, é mais de um), só não tem a marca sonora desse conceito.",
"#momento_linguistíco_17- Se <bem> é advérbio em <Estou bem> porque é como a pessoa está, por que <feliz> em <Estou feliz> não é advérbio!!?? Saiba mais curiosidades em @classificador.gramatical",
"#momento_linguistíco_18- Sabia que <geral> já foi apenas um advérbio (<Ele criticou geral>, o modo como ele criticou), depois substantivo como objeto (<Ele criticou geral>, criticou todo mundo) e agora é o nosso substantivo sujeito (<Geral foi criticada por ele>).",
"#momento_linguistíco_19- O sufixo <inho> só se aplica a substantivo (livrinho) e adjetivo (bonitinho)? Nananinanão, olha o <euzinho> e o <dormindinho>!",
"#momento_linguistíco_20- Já foi o tempo que o prefixo <des-> era para reverter uma ação que afetava algo (desconstruir, desligar). Hoje já dá para <desler>, <desver> e até <desbeijar>!",
"#momento_linguistíco_21- Por que linguistas dizem que <ninguém fala errado>? Porque toda fala é uma variação legítima da língua",
"#momento_linguistíco_22- <Norma culta> é uma expressão que muita gente usa, mas pode ter vários significados, o que pode gerar confusão. Procure por <Norma Culta>, <Norma Padrão> e <Norma Curta> para ver alguns conceitos diferentes.",
"#momento_linguistíco_23 - <Norma não culta> não é um termo que a Linguística usa, pois dá a entender uma falta de algo, de cultura. Preferimos, dependendo do caso, <Norma popular>, <Norma informal>, entre outras.",
"#redes_sociais_1- Que tal um app de linguística? Baixe <Isso não é uma gramática> na Playstore!",
"#redes_sociais_2- Eiii, já seguiu a gente no Instagram?? Olha nós aqui: @classificador.gramatical",
"#redes_sociais_3- Se algo deu errado conta pra gente no Insta: @classificador.gramatical",
"#redes_sociais_4- No nosso perfil no Instagram (@classificador.gramatical), você pode ver muitas curiosidades gramaticais sobre classes de palavras.",
"#redes_sociais_5- Procure por #linguística no Instagram e descubra um mundo de divulgação dessa ciência!",
"#redes_sociais_6- Quer saber quem está por trás do Classificador Gramatical? Vai no nosso Insta (@classificador.gramatical) para ver quem faz parte dessa equipe!",
"#redes_sociais_7- Tem linguística no YouTube? Tem! Tem conteúdos bem básicos numa linguagem moderna? Tem! Começa com <Com a palavra, Linguística> e de lá vê outros canais",
    
    ]

def get_tip():
    return random.choice(messages)
