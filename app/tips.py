import random

messages = [
    "#explicando_1: O Classificador Gramatical é baseado na biblioteca Spacy que, por sua vez, foi construída utilizando o projeto Universal Dependencies",
    "#redes_sociais_1: Que tal um app de linguística? Baixe 'Isso não é uma gramática' na Playstore!",
    "#explicando_2: Classificar palavras é difícil... Tem contexto, tem ambiguidades, mas a gente chega lá!",
    "#explicando_3: Para chegar nesse nível de acertos, foi preciso testar MUITO (e ainda precisa testar MAIS)",
    "#explicando_4: Substantivos e adjetivos são as palavras mais difíceis de classificar...",
    "#explicando_5: Lembre-se: o Classificador funciona melhor no gênero escrito formal culto",
    "#redes_sociais_2: Eiii, enquanto o resultado não sai, segue a gente no Instagram: @classificador.gramatical",
    "#redes_sociais_3: Se algo deu errado conta pra gente no Insta: @classificador.gramatical",
    "#explicando_6: Aqui (https://github.com/UniversalDependencies/UD_Portuguese-Bosque) você encontra informações sobre a participação brasileira no projeto Universal Dependencies",
    "#explicando_7: Muitas adaptações foram feitas pelos membros do projeto na versão original de etiquetagem do Spacy",
    "#explicando_8: Etiquetagem é o termo técnico utilizado na área para a classificação gramatical de uma palavra",
    "#explicando_9: O classificador gramatical se insere na área de Processamento de Linguagem Natural (PLN)",
    "#momento_linguistíco_1: O preconceito linguístico é uma forma de preconceito a determinadas variedades linguísticas.",
    "#momento_linguistíco_2:Para a linguística os chamados “erros” gramaticais não existem nas línguas naturais.",
    "#momento_linguistíco_3: A língua escrita e  a língua falada são coisas bem diferentes: a escrita é estática, já a segunda está sempre se adaptando a cada nova geração.",
    "#momento_linguistíco_4: Um sistema de escrita é UMA representação da fala, não A representação da fala.",
    "#redes_sociais_4: No nosso perfil no Instagram (@classificador.gramatical), você pode ver muitas curiosidades gramaticais sobre classes de palavras.",
    "#momento_linguistíco_5: Palavras mudam de classe porque podem assumir novos sentidos exigidos por mudanças extralinguísticas.",
    "#redes_sociais_5: Procure por #linguística no Instagram e descubra um mundo de divulgação dessa ciência!",
    "#momento_linguistíco_6: \"Menos\" nem sempre é advérbio: em \"menos queijo\", está modificando um substantivo e deve ser um pronome.",
    "#momento_linguistíco_7: Regularizar formas irregulares é uma atividade comum na aquisição da linguagem e também em registros cotidianos.",
    "#momento_linguistíco_8: Em \"vamos sair\", \"vamos\" é auxiliar e \"sair\" principal. Assim, em \"vamos ir\", não há redundância: temos um auxiliar e um principal também.",
    "#momento_linguistíco_9: A prática do preconceito linguístico não tem fundamento científico e é tão abominável quanto os demais preconceitos.",
]

def get_tip():
    return random.choice(messages)