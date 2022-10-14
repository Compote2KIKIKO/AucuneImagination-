from flask import Flask,render_template, session , redirect
import random

app = Flask("Mmh")
app.secret_key = "cookies"
@app.route("/")
def page_acceuil():
  session["score"] = 0
  session["quest"] = 0
  return render_template("Acceuil.html")

@app.route("/Europe")
def page_europe():
  session["score"] = 0
  session["quest"] = 0
  session["route"] = "/EuropeFlag"
  return render_template("Mmh.html")




@app.route("/AmeriqueDuSud")
def page_ameriquedusud():
  session["score"] = 0
  session["quest"] = 0
  session["route"] = "/AmeriqueDuSudFlag"
  return render_template("AmeriqueDuSud.html")

@app.route("/AmeriqueDuSudFlag")
def page_ameriquedusudflag():
  liste_drapeaux =["Argentine.png","Bolivie.png","Brésil.png","Chili.png","Colombie.png","Equateur.png","Guyana.png","Paraguay.png","Pérou.png","Suriname.png","Uruguay.png","Venezuela.png"]
  drapeaux = random.sample(liste_drapeaux, 12) 
  pays = drapeaux[0]
  size = len(pays)
  bonne_reponse = pays
  pays = pays[:size - 4]
  random.shuffle(drapeaux)
  session["reponse"] = "/ResultatAmeriqueDuSud"
  session["numero_bonne_reponse"]= drapeaux.index(bonne_reponse)
  return render_template("AmeriqueDuSudFlag.html", drapeaux = drapeaux, pays = pays)
  


  

@app.route("/Oceanie")
def page_oceanie():
  session["score"] = 0
  session["quest"] = 0
  session["route"] = "/OceanieFlag"
  return render_template("Oceanie.html")
  
@app.route("/OceanieFlag")
def page_oceanieflag():
  liste_drapeaux = ["Australie.png","Îles Fidji.png","Îles Marshall.png","Îles Salomon.png","Kiribati.PNG","Micronésie.png","Nauru.PNG","Nouvelle Zélande.png","Palaos.png","Papouasie Nouvelle Guinée.PNG","Samoa.png","Tonga.png","Tuvalu.png"]
  drapeaux = random.sample(liste_drapeaux, 12) 
  pays = drapeaux[0]
  size = len(pays)
  bonne_reponse = pays
  pays = pays[:size - 4]
  random.shuffle(drapeaux)
  session["reponse"] = "/ResultatOceanie"
  session["numero_bonne_reponse"]= drapeaux.index(bonne_reponse)
  return render_template("OceanieFlag.html", drapeaux = drapeaux, pays = pays)
  
  
@app.route("/ResultatAsie")
def page_resuasie():
  
  return render_template("ResAsie.html")


@app.route("/ResultatEurope")
def page_resasie():
  return render_template("ResEurope.html")
  awa = session["score"]
  pourcentage = awa*1/100
  print(pourcentage)
  


@app.route("/ResultatAfrique")
def page_resafrique():
  return render_template("ResAfrique.html")


@app.route("/ResultatAmeriqueDuNord")
def page_resameriquenord():
  return render_template("ResAmeriqueNord.html")


@app.route("/ResultatAmeriqueDuSud")
def page_resameriquesud():
  return render_template("ResAmeriqueSud.html")
  


@app.route("/ResultatOceanie")
def page_resoceanie():
  return render_template("ResOceanie.html")




@app.route("/Afrique")
def page_afrique():
  session["score"] = 0
  session["quest"] = 0
  
  
  session["route"] = "/AfriqueFlag"
  return render_template("Afrique.html")



@app.route("/AmeriqueDuNord")
def page_ameriquenord():
  session["route"] = "/AmeriqueDuNordFlag"
  return render_template("AmeriqueDuNord.html")


@app.route("/AmeriqueDuNordFlag")
def page_ameriquedunordflag():
  liste_drapeaux = ["Bélize.png","Canada.png","Costa Rica.png","Cuba.png","Etats Unis.png","Guatemala.png","Haiti.png","Honduras.png","Jamaique.png","Mexique.png","Nicaragua.png","Panama.png","Republique Dominicaine.png","Salvador.png"]
  
  drapeaux = random.sample(liste_drapeaux, 12) 
  pays = drapeaux[0]
  size = len(pays)
  bonne_reponse = pays
  pays = pays[:size - 4]
  random.shuffle(drapeaux)
  session["reponse"] = "/ResultatAmeriqueDuNord"
  
  session["numero_bonne_reponse"]= drapeaux.index(bonne_reponse)
  return render_template("AmeriqueDuNordFlag.html", drapeaux = drapeaux, pays = pays)
  
  
  
  


  

@app.route("/AfriqueFlag")

def page_afriqueflag():
  
  liste_drapeaux = ["Afrique Centrale.png","Algerie.png","Benin.png","Botstawana.png","Burkina Faso.png","Burundi.png","Cameroun.png","Cap Vert.png","Comores.png","Côte d'ivoire.png","Djibouti.png","Egypte.png","Erithrée.png","Eswatani.png","Ethiopie.png","Gabon.png","Gambie.png","Ghana.png","Guinée Bisseau.png","Guinée Equitorial.png","Guinée.png","Kenya.png","Lesotho.png","Liberia.png","Libye.png","Madagascar.png","Malawi.png","Mali.png","Maroc.png","Maurice.png","Mauritanie.png","Mozambique.png","Namibie.png","Niger.png","Nigeria.png","Ouganda.png","Republique Democratique Du Congo.png","Republique du Congo.png","Rwanda.png","Sao Tomé et Principe.png","Sénégal.png","Seychelles.png","Sierra Leone.png","Somalie.png","Soudan Du Sud.png","Soudan.png","Tanzanie.png","Tchad.png","Togo.png","Tunisie.png","Zambie.png","Zimbabwe.png"]
  
  drapeaux = random.sample(liste_drapeaux, 12) 
  pays = drapeaux[0]
  size = len(pays)
  bonne_reponse = pays
  pays = pays[:size - 4]
  random.shuffle(drapeaux)
  session["reponse"] = "/ResultatAfrique"
  session["numero_bonne_reponse"]= drapeaux.index(bonne_reponse)
  return render_template("AfriqueFlag.html", drapeaux = drapeaux, pays = pays)
  


@app.route("/reponse0")
def reponse0():
  if session["quest"] == 20 :
    
     return redirect(session["reponse"])
    
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 0 :
    session["score"] += 1
  return redirect(session["route"])
  

@app.route("/reponse1")
def reponse1():
  if session["quest"] == 20 :

    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 1 :
    sessio
    n["score"] += 1
    
  return redirect(session["route"])
  

@app.route("/reponse2")
def reponse2():
  if session["quest"] == 20 :

    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 2 :
    session["score"] += 1
    
  return redirect(session["route"])
  

@app.route("/reponse3")
def reponse3():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 3 :
    session["score"] += 1
    
  return redirect(session["route"])
  

@app.route("/reponse4")
def reponse4():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 4 :
    session["score"] += 1
    
  return redirect(session["route"])
  

@app.route("/reponse5")
def reponse5():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 5 :
    session["score"] += 1
    
  return redirect(session["route"])
  

@app.route("/reponse6")
def reponse6():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 6 :
    session["score"] += 1
    
  return redirect(session["route"])
  

@app.route("/reponse7")
def reponse7():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 7 :
    session["score"] += 1
    
  return redirect(session["route"])
  

@app.route("/reponse8")
def reponse8():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 8 :
    session["score"] += 1
   
  return redirect(session["route"])
  

@app.route("/reponse9")
def reponse9():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 9 :
    session["score"] += 1
   
  return redirect(session["route"])
  

@app.route("/reponse10")
def reponse10():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 10 :
    session["score"] += 1
    
  return redirect(session["route"])
  

@app.route("/reponse11")
def reponse11():
  if session["quest"] == 20 :
    
    
     return redirect(session["reponse"])
  session["quest"] += 1
  if session["numero_bonne_reponse"] == 11 :
    session["score"] += 1
    
  return redirect(session["route"])
  
  

  
@app.route("/Asie")
def page_asie():
  session["score"] = 0
  session["quest"] = 0
  session["route"] = "/AsieFlag"
  return render_template("Asie.html")
  



@app.route("/AsieFlag")
def page_asieflag():
  liste_drapeaux = ["Arabie Saoudite.png","Arménie.png","Bahrein.png","Bangladesh.png","Bhoutan.png","Birmanie.png","Brunei.png","Cambodge.png","Chine.png","Corée Du Nord.png","Corée Du Sud.png","Egypte.png","Emirats Arabes Unis.png","Gorgie.png","Inde.png","Indonésie.png","Iraq.png","Israel.png","Japon.png","Jordanie.png","Kazakhstan.png","Kirghizistan.png","Koweit.png","Laos.png","Liban.png","Malaisie.png","Maldives.png","Mongolie.png","Nepal.png","Oman.png","Ouzbékistan.png","Pakistan.png","Philippines.png","Qatar.png","Singapour.png","Sri Lanka.png","Syrie.png","Tadjikistan.png","Thailande.png","Timor Oriental.png","Turkménistan.png","Turquie.png","Vietnam.png","Yémen.png","Russie.png"]
  
  drapeaux = random.sample(liste_drapeaux, 12) 
  pays = drapeaux[0]
  size = len(pays)
  bonne_reponse = pays
  pays = pays[:size - 4]
  random.shuffle(drapeaux)
  session["reponse"] = "/ResultatAsie"
  
  session["numero_bonne_reponse"]= drapeaux.index(bonne_reponse)
  
  return render_template("AsieFlag.html", drapeaux = drapeaux, pays = pays)
  
  
  
  
  
    
   


    










@app.route("/EuropeFlag")
def page_flag():
  liste_drapeaux = ["Albanie.png","Allemagne.png","Andorre.png","Angleterre.png","Autriche.png","Belgique.png","Biélorussie.png","Bosnie Erségovine.png","Bulgarie.png","Chypre.png","Croatie.png","Danemark.png","Espagne.png","Estonie.png","Finlande.png","France.png","Grece.png","Hongrie.png","Irlande.png","Islande.png","Italie.png","Lettonie.png","Lienchestien.png","Lituanie.png","Luxembourg.png","Macédoine du Nord.png","Malte.png","Moldavie.png","Monaco.png","Montenegro.png","Norvege.png","Pays bas.png","Pologne.png","Portugal.png","Republique Tcheque.png","Roumanie.png","Russie.png","Saint-Marin.png","Serbie.png","Slovaquie.png","Slovenie.png","Suede.png","Suisse.png","Ukraine.png","Vatican.png"]
  drapeaux = random.sample(liste_drapeaux, 12) 
  pays = drapeaux[0]
  size = len(pays)
  bonne_reponse = pays
  pays = pays[:size - 4]
  random.shuffle(drapeaux)
  session["reponse"] = "/ResultatEurope"
  session["numero_bonne_reponse"]= drapeaux.index(bonne_reponse)
  #drapeaux = drapeaux.append("France.png")
  #random.shuffle(drapeaux)
  return render_template("Mah.html", drapeaux = drapeaux, pays = pays)
  
  
    
    
  
  
  

  




  
  print("Awaa")

app.run("0.0.0.0", "3904")

