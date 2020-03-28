 #bin utf-8
class AutoDiagnostic():
	parsedTemp=37
	hasTemp=True

def Welcome():
  msg=" 
       Welcome to the COVID-19 ** self-diagnostic test **, is based ob the algorithm carried out in partnership with ** the Pasteur Institute ** and the ** Ministry of Health **.
       ⚠️ Please note, this information site ** is not a medical device **, it does not deliver medical advice. "
       🚨 ** Important Information ** 🚨: Taking anti-inflammatory drugs (ibuprofen, cortisone ...) could be a factor in worsening the infection.
      In case of fever 🤒, take paracetamol. If you are already on anti-inflammatory drugs or in doubt, ask your doctor for advice 👨‍⚕️👩‍⚕️. "
   return msg

def BeginTest():
	question=" *** I acknowledge having read the preamble and wish to start the test *** ",
   	return question

def checkBeginTest(response):
	if response in ["yes", "Yes"]:
		msg="Let’s go."
		 q1 
		
	else:
		msg="Noted. Have a good day ! 🙂"
	
def question1(question,event):
	msg="**1/23** : Do you think you have or have had a fever in the past few days (chills, sweating)?",
	btnyes=["Oui","oui", "yes", "Yes", "Ouais", "ouais"]
	btnno=["Non","non", "no", "Nope", "nope", "No", "Pas du tout"]
	if event in  btnyes:
		self.hasTemp = 1
		goto q2
	else if event in btnno:
		self.hasTemp = 0
		# Verifier la valeur envoyée à l'api de `temp`
		self.temp = 0
		goto q3
	else:
		msg= "Veuillez s'il vous plait cliquer sur un des boutons."
		goto q1
	

def question:(question,event):
	question= "**1bis/23** : Quelle est votre température corporelle (ex: 38) ?"
	self.parsedTemp=float(event)
	if (parsedTemp=
		say "Veuillez saisir ue température valide."
		goto q2
	}
	if (parsedTemp.is_number() && parsedTemp >= 34 && parsedTemp <= 42) {
		remember temp = parsedTemp
		goto q3
	} else {
		say "Veuillez saisir une température valide, entre 34 et 42 degrés."
		goto q2
	}

q3:
	say Question(
		"**2/23** : Ces derniers jours, avez-vous une **toux ou une augmentation de votre toux habituelle** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasCaugh = 1
		goto q4
	} else if (event match btnno) {
		remember hasCaugh = 0
		goto q4
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons."
		goto q3
	}

q4:
	say Question(
		"**3/23** : Ces derniers jours, avez-vous noté une **forte diminution ou perte de votre goût ou de votre odorat** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasNoTaste = 1
		goto q4b
	} else if (event match btnno) {
		remember hasNoTaste = 0
		goto q4b
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q4
	}

q4b:
	say Question(
		"**4/23** : Avez-vous des **douleurs musculaires** ou **des courbatures inhabituelles** ces derniers jours ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasMusclePain = 1
		goto q5
	} else if (event match btnno) {
		remember hasMusclePain = 0
		goto q5
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q4
	}

q5:
	say Question(
		"**5/23** : Ces derniers jours, avez-vous un **mal de gorge** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasPainfulThroat = 1
		goto q6
	} else if (event match btnno) {
		remember hasPainfulThroat = 0
		goto q6
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q5
	}

q6:
	say Question(
		"**6/23** : Ces dernières 24 heures, avez-vous de la **diarrhée** ? Avec au moins 3 selles molles.",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasDiarrhea = 1
		goto q7
	} else if (event match btnno) {
		remember hasDiarrhea = 0
		goto q7
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q6
	}

q7:
	say Question(
		"**7/23** : Ces derniers jours, avez-vous une **fatigue inhabituelle** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasFatigue = 1
		goto q8
	} else if (event match btnno) {
		remember hasFatigue = 0
		remember hasDailyNap = 0
		goto q9
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q6
	}

q8:
	say Question(
		"**7bis/23** : Cette fatigue vous oblige-t-elle à vous reposer plus de la moitié de la journée ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasDailyNap = 1
		goto q9
	} else if (event match btnno) {
		remember hasDailyNap = 0
		goto q9
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q8
	}

q9:
	say Question(
		"**8/23** : Êtes vous dans l'impossibilité de vous alimenter ou de boire **DEPUIS 24 HEURES OU PLUS** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasFeedStruggle = 1
		goto q10
	} else if (event match btnno) {
		remember hasFeedStruggle = 0
		goto q10
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q9
	}

q10:
	say Question(
		"**9/23** : Dans les dernières 24 heures, avez-vous noté un **manque de souffle INHABITUEL** lorsque vous parlez ou faites un petit effort ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasSOB = 1
		goto q11
	} else if (event match btnno) {
		remember hasSOB = 0
		goto q11
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q10
	}

q11:
	say Question(
		"**10/23** : En ce moment, comment vous sentez-vous, physiquement ?",
		buttons=[
			Button("Bien", accepts=["bien"]) as btnbien,
			Button("Assez bien", accepts=["assez bien"]) as btnabien,
			Button("Mal", accepts=["mal"]) as btnmal,
			Button("Très mal", accepts=["Tres mal", "très mal", "tres mal"]) as btntmal
		])
	hold
	if (event match btnbien) {
		remember howgood = "Bien"
		goto q12
	} else if (event match btnabien) {
		remember howgood = "Assez bien"
		goto q12
	} else if (event match btnmal) {
		remember howgood = "Mal"
		goto q11b
	} else if (event match btntmal) {
		remember howgood = "Très mal"
		goto q11b
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q11
	}

q11b:
	say "**10bis/23** : Avez-vous d’autre symptôme ?"
	hold
	remember othersymptoms = event
	goto q12

q12:
	say "**11/23** : Quel est votre âge ? Ceci, afin de calculer un facteur de risque spécifique (ex: 28)."
	hold
	do Fn("norm_units", string=event) as parsedAge
	if (!parsedAge) {
		say "Veuillez saisir un age valide."
		goto q12
	}
	if (parsedAge.is_number() && parsedAge > 15 && parsedAge <= 110) {
		remember age = parsedAge
		goto q13
	} else if (parsedAge <= 15 && parsedAge >= 0) {
		say "En l'absence de recommandations connues pour les affections pédiatriques (de moins de 15 ans), il faut rechercher un avis médical pour tout symptôme sur les enfants. Si l'état de santé du patient semble inquiétant, appelez le 15."
		goto end
	} else if (parsedAge >= 100 && parsedAge <= 110) {
		say "Au-delà d'un certain âge, nous ne sommes pas en mesure de fournir des recommendations fiables, il faut rechercher un avis médical pour tout symptôme. Si l'état de santé du patient semble inquiétant, appelez le 15."
		goto end
	} else {
		say "Veuillez saisir un age valide."
		goto q12
	}

q13:
	say "**12/23** : Quel est votre **taille** en centimetres (ex: 175) ? Afin de calculer l’indice de masse corporelle qui est un facteur influençant le risque de complications de l’infection."
	hold
	do Fn("norm_units", string=event) as parsedSize
	if (!parsedSize) {
		say "Veuillez saisir une taille valide, entre 80 et 250 cm."
		goto q13
	}
	if (parsedSize < 10) do normSize = parsedSize * 100
	else do normSize = parsedSize
	if (normSize.is_number() && normSize >= 80 && normSize <= 250) {
		remember size = normSize
		goto q14
	} else {
		say "Veuillez saisir une taille valide, entre 80 et 250 cm."
		goto q13
	}

q14:
	say "**13/23** : Quel est votre **poids** en kilogrammes (ex: 84) ? Afin de calculer l’indice de masse corporelle qui est un facteur influençant le risque de complications de l’infection. "
	hold
	do Fn("norm_units", string=event) as parsedWeight
	if (!parsedWeight) {
		say "Veuillez saisir un poids valide, entre 20 et 250 kg."
		goto q14
	}
	if (parsedWeight.is_number() && parsedWeight >= 20 && parsedWeight <= 250) {
		remember weight = parsedWeight
		goto q15
	} else {
		say "Veuillez saisir un poids valide, entre 20 et 250 kg."
		goto q14
	}

q15:
	say Question(
		"**14/23** : Avez-vous de **l’hypertension artérielle** mal équilibrée ? Ou avez-vous une **maladie cardiaque ou vasculaire** ? Ou prenez-vous un **traitement à visée cardiologique** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno,
			Button("Ne sait pas", accepts=["ne sait pas", "ne sais pas", "Ne sais pas", "Je ne sais pas", "je ne sais pas", "ne sais pas"]) as btnnsp
		])
	hold
	if (event match btnyes) {
		remember hasCARDISSUE = 1
		goto q16
	} else if (event match btnno) {
		remember hasCARDISSUE = 0
		goto q16
	} else if (event match btnnsp) {
		remember hasCARDISSUE = 2
		goto q16
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q15
	}

q16:
	say Question(
		"**15/23** : Êtes-vous diabétique ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasDiabetes = 1
		goto q17
	} else if (event match btnno) {
		remember hasDiabetes = 0
		goto q17
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q16
	}

q17:
	say Question(
		"**16/23** : Avez-vous ou avez-vous eu un **cancer** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasCancer = 1
		goto q18
	} else if (event match btnno) {
		remember hasCancer = 0
		goto q18
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q17
	}

q18:
	say Question(
		"**17/23** : Avez-vous une **maladie respiratoire** ? Ou êtes-vous **suivi par un pneumologue** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasBreathingIllness = 1
		goto q19
	} else if (event match btnno) {
		remember hasBreathingIllness = 0
		goto q19
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q18
	}

q19:
	say Question(
		"**18/23** : Avez-vous une **insuffisance rénale chronique dialysée** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasKidneyFailure = 1
		goto q20
	} else if (event match btnno) {
		remember hasKidneyFailure = 0
		goto q20
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q19
	}

q20:
	say Question(
		"**19/23** : Avez-vous une **maladie chronique du foie** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno
		])
	hold
	if (event match btnyes) {
		remember hasLiverIllness = 1
		goto q21
	} else if (event match btnno) {
		remember hasLiverIllness = 0
		goto q21
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q20
	}

q21:
	say Question(
		"**20/23** : Êtes-vous **enceinte** ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno,
			Button("Non applicable", accepts=["non applicable", "Pas applicable", "na", "n/a", "N/A", "NA"]) as btnna
		])
	hold
	if (event match btnyes) {
		remember isPregnant = 1
		goto q22
	} else if (event match btnno) {
		remember isPregnant = 0
		goto q22
	} else if (event match btnna) {
		remember isPregnant = 2
		goto q22
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q21
	}

q22:
	say Question(
		"**21/23** : Avez-vous une maladie connue pour diminuer vos défenses immunitaires ?",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno,
			Button("Ne sait pas", accepts=["ne sait pas", "ne sais pas", "Ne sais pas", "Je ne sais pas", "je ne sais pas", "ne sais pas"]) as btnnsp
		])
	hold
	if (event match btnyes) {
		remember hasImuneSystemFailure = 1
		goto q23
	} else if (event match btnno) {
		remember hasImuneSystemFailure = 0
		goto q23
	} else if (event match btnnsp) {
		remember hasImuneSystemFailure = 2
		goto q23
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q22
	}

q23:
	say Question(
		"**22/23** : Prenez-vous un **traitement immunosuppresseur** ? C’est un traitement qui diminue vos défenses contre les infections. Voici quelques exemples : corticoïdes, méthotrexate, ciclosporine, tacrolimus, azathioprine, cyclophosphamide (liste non exhaustive).",
		buttons=[
			Button("Oui", accepts=["oui", "yes", "Yes", "Ouais", "ouais"]) as btnyes,
			Button("Non", accepts=["non", "no", "Nope", "nope", "No", "Pas du tout"]) as btnno,
			Button("Ne sait pas", accepts=["ne sait pas", "ne sais pas", "Ne sais pas", "Je ne sais pas", "je ne sais pas", "ne sais pas"]) as btnnsp
		])
	hold
	if (event match btnyes) {
		remember hasImmunosuppresseur = 1
		goto q24
	} else if (event match btnno) {
		remember hasImmunosuppresseur = 0
		goto q24
	} else if (event match btnnsp) {
		remember hasImmunosuppresseur = 2
		goto q24
	} else {
		say "Veuillez s'il vous plait cliquer sur un des boutons"
		goto q23
	}

q24:
	say Question(
		"**23/23** : Quel est votre code postal ?",
		buttons = [
			Button("Je ne suis pas en France",
				accepts=[
					"Pas en France",
					"pas en france",
					"Pas en france",
					"pas en France"
				]
			) as btnhorsfr
		])
	hold
	if (event match btnhorsfr) {
		remember location = "horsFR"
	} else {
		remember location = event
	}
	goto bufferStep

bufferStep:
	if (done == 1) {
		remember done = 0
		goto end
	}
	remember done = 1
	goto flow diag_20200323_algo
