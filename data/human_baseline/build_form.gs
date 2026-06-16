/**
 * build_form.gs — cria o Google Form do baseline humano (coleta do padrão-ouro).
 *
 * COMO USAR:
 *   1. Acesse https://script.google.com  ->  "Novo projeto".
 *   2. Apague o conteúdo padrão, cole TODO este arquivo e salve.
 *   3. Selecione a função "criarFormulario" e clique em "Executar".
 *   4. Autorize o acesso quando pedir (é a sua conta criando um form na sua Drive).
 *   5. Abra "Execução" / "Logs": ele imprime o LINK PÚBLICO (para enviar aos
 *      professores) e o LINK DE EDIÇÃO (para você ajustar, se quiser).
 *
 * O que o form coleta: identificação por código (anônimo), perfil profissional,
 * consentimento, e a devolutiva livre para cada um dos 13 cenários.
 * As respostas caem numa planilha (aba "Respostas") exportável para JSON.
 */

var CENARIOS = [
  "Resenha sobre A Cartomante: A cartomante falou pro Camilo que tava tudo bem. A cartomante leu as cartas. A cartomante sorriu pra ele. A cartomante deu certeza pra ele. Depois o Camilo foi pra casa do Vilela e morreu. A cartomante tinha errado tudo.",
  "No conto O Alienista, o Simão Bacamarte prendeu o barbeiro porque ele achava que ele era louco e ele queria provar a teoria dele pra ele, mas no fim ele soltou ele e ele ficou confuso.",
  "Eu gostei muito do conto A Cartomante porque ele é triste, portanto eu ri bastante nas partes do meio. Embora o final seja chocante, mas era óbvio que ia acontecer aquilo.",
  "Crônica que eu escrevi: O Camilo morreu no final. Mas antes disso ele recebeu um bilhete do Vilela. A cartomante já tinha dito que tava tudo certo. Então ele conheceu a Rita primeiro de tudo. Aí ele foi na casa do amigo.",
  "Minha opinião sobre O Alienista: A Casa Verde foi importante. Foi muito grande. O povo de Itaguaí tinha medo. Bacamarte estudava muito. A ciência dele era estranha. As pessoas se revoltaram um dia.",
  "Resumo de O Alienista: A Casa Verde era o lugar onde os loucos ficavam. A Casa Verde foi feita pelo Bacamarte. A Casa Verde assustava o povo. A Casa Verde ficava cheia. No final a Casa Verde foi esvaziada porque a Casa Verde não fazia mais sentido.",
  "Reconto de O Homem Nu: O homem ficou pelado. Ele abriu a porta. O bonde passou. A mulher dele saiu. Ele tava devendo o aluguel. O cobrador bateu. Ele se escondeu no elevador. Ficou todo mundo rindo dele na rua. Ele entrou de novo em casa.",
  "Sobre A Moça Tecelã: A moça teceu o marido com o tear. Ela queria companhia. Quando ele chegou ele pediu mais coisas pra ela. Ela teceu pra ele um palácio. Aí ela desfez ele e ela ficou livre. Ela gostava dela mesma de novo.",
  "O Caso da Borboleta Atíria, minha parte favorita: O detetive chegou. Era de noite. A casa era grande. Tinha uma borboleta. A borboleta era rara. O homem morreu. Ninguém viu nada. O detetive achou uma pista. A pista era pequena. Todo mundo era suspeito.",
  "Resenha de Cemitério dos Vivos: O personagem foi internado, portanto ele se sentia muito sozinho lá dentro. O lugar era horrível, mas por isso ele queria ficar. Embora ele sofresse, contudo ele continuava escrevendo, assim ele desistiu de tudo no fim.",
  "Resenha de A Cartomante: Camilo vivia angustiado com os bilhetes anônimos. Por isso, procurou a cartomante, que leu as cartas e o tranquilizou. Saiu de lá aliviado e seguiu para a casa do amigo. Quando chegou, porém, encontrou Vilela à sua espera. A previsão, afinal, não o havia salvado.",
  "Sobre O Alienista: Simão Bacamarte fundou a Casa Verde para estudar a loucura. No início, internava apenas casos extremos; depois, passou a recolher quase toda a cidade. Como a teoria não se sustentava, ele inverteu o critério e libertou os internos. Por fim, restou um único louco aos seus próprios olhos: ele mesmo.",
  "Reconto de O Homem Nu: Naquela manhã, o homem tirou a roupa para tomar banho. Enquanto o café passava, ouviu a campainha e, distraído, abriu a porta. Nesse instante, ela bateu atrás dele e o deixou nu no corredor. Sem saída, desceu pelo elevador; logo depois, percebeu que a confusão só aumentava."
];

// Logos exibidas no topo do form (buscadas por URL pública pelo UrlFetchApp).
// São as PNGs versionadas no repo público; o branch é "main".
var LOGO_URLS = [
  "https://raw.githubusercontent.com/RandMelville/slm-writing-feedback-tutor-ptbr/main/data/human_baseline/logo-ufrgs.png",
  "https://raw.githubusercontent.com/RandMelville/slm-writing-feedback-tutor-ptbr/main/data/human_baseline/ppgie-logo.png"
];

function criarFormulario() {
  var form = FormApp.create("Referência especializada — devolutivas de escrita (8º/9º ano)");

  form.setDescription(
    "Obrigado por colaborar. Para cada um dos 13 textos curtos e fictícios (simulando " +
    "produções de alunos do 8º/9º ano), escreva a devolutiva que você daria ao aluno " +
    "para ajudá-lo a aprimorar a escrita, na forma que considerar adequada. Se precisar " +
    "de um foco, priorize aspectos de textualidade (coesão, coerência e progressão).\n\n" +
    "Não há gabarito nem resposta certa, e você não está sendo avaliado(a): suas respostas " +
    "servem como referência humana especializada. Os textos são fictícios (sem dados " +
    "pessoais). Suas respostas entram de forma anônima, por código. Tempo estimado: ~30 min."
  );

  // Configurações: anônimo, sem login obrigatório, barra de progresso.
  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);
  form.setAllowResponseEdits(false);
  form.setLimitOneResponsePerUser(false);

  // --- Logos no topo (UFRGS / PPGIE) ---
  for (var k = 0; k < LOGO_URLS.length; k++) {
    try {
      var blob = UrlFetchApp.fetch(LOGO_URLS[k]).getBlob();
      form.addImageItem().setImage(blob).setAlignment(FormApp.Alignment.CENTER);
    } catch (e) {
      Logger.log("Aviso: não carreguei a logo " + LOGO_URLS[k] + " (" + e + "). " +
                 "Confirme que o repo foi enviado ao GitHub ou adicione a imagem manualmente.");
    }
  }

  // --- Identificação (anônima) ---
  form.addTextItem()
      .setTitle("Código do(a) anotador(a)")
      .setHelpText("Informado pela equipe (ex.: A, B ou C). Não escreva seu nome aqui.")
      .setRequired(true);

  // --- Perfil profissional ---
  form.addSectionHeaderItem()
      .setTitle("Perfil profissional")
      .setHelpText("Só para caracterizar o painel de forma agregada e anônima. " +
                   "Não coletamos dados pessoais ou sensíveis.");

  form.addTextItem()
      .setTitle("Disciplina que leciona")
      .setHelpText("Esperado: Língua Portuguesa.")
      .setRequired(true);

  form.addTextItem()
      .setTitle("Anos/séries em que atua atualmente")
      .setHelpText("Esperado: 8º e/ou 9º ano do Ensino Fundamental II; indique outros se houver.")
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle("Tempo de experiência docente")
      .setChoiceValues(["menos de 2 anos", "2–5 anos", "6–10 anos", "mais de 10 anos"])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle("Experiência com ensino e correção de redação / produção textual")
      .setChoiceValues(["sim, regularmente", "sim, ocasionalmente", "pouca ou nenhuma"])
      .setRequired(true);

  form.addMultipleChoiceItem()
      .setTitle("Familiaridade com feedback formativo / mediação pedagógica")
      .setChoiceValues(["muita", "alguma", "pouca"])
      .setRequired(true);

  form.addTextItem()
      .setTitle("Formação (opcional)")
      .setHelpText("Ex.: Licenciatura em Letras; especialização/mestrado, se houver.")
      .setRequired(false);

  // --- Consentimento ---
  form.addCheckboxItem()
      .setTitle("Aceite de colaboração")
      .setChoiceValues([
        "Li o convite e concordo em colaborar voluntariamente, ciente de que minhas " +
        "respostas serão usadas de forma anônima (por código) no estudo, podendo ser " +
        "publicadas sob licença Creative Commons (CC BY 4.0)."
      ])
      .setRequired(true);

  form.addTextItem()
      .setTitle("Nome (opcional, apenas para agradecimentos)")
      .setHelpText("Mantido separado das respostas. Deixe em branco se preferir permanecer anônimo(a).")
      .setRequired(false);

  // --- Os 13 cenários (devolutiva livre) ---
  form.addPageBreakItem()
      .setTitle("Os 13 textos")
      .setHelpText("Para cada texto, escreva a devolutiva que daria ao aluno. " +
                   "Pode incluir o que está bom, perguntas, pistas, orientações ou correções.");

  for (var i = 0; i < CENARIOS.length; i++) {
    form.addParagraphTextItem()
        .setTitle("Cenário " + (i + 1) + " — sua devolutiva ao aluno")
        .setHelpText("Texto do aluno: " + CENARIOS[i])
        .setRequired(true);
  }

  Logger.log("==========================================================");
  Logger.log("LINK PARA ENVIAR AOS PROFESSORES (público):");
  Logger.log(form.getPublishedUrl());
  Logger.log("LINK DE EDIÇÃO (só você):");
  Logger.log(form.getEditUrl());
  Logger.log("==========================================================");
}
