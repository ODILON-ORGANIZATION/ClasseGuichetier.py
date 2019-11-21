coding:utf-8

class guichetier: 
      def __init__(self, id, MotDePasse):#methode permettant de connaitre le montant danscompte
        self.id = id
        self.MotDePasse = MotDePasse
        self.solde = 50000
      def depot(self):#methode pour le depot de la somme
        montant = input("entrer le montant du depot...\n")
        montant = int(montant)
        self.solde += montant
        print("vous avez effectuer un depot de ", montant)
        print("nouveau solde", self.solde)
      def retret (self):#methode pour retirer
        montants = input("combien vouliez vous retirer\n")
        montants = int(montants)
        if montants <= self.solde:
           self.solde = self.solde-montants
           print("vous avez effectuer un retrait de ", montants)
           print("nouveau solde", self.solde)
        else:
           print("solde insuffisant")        
      def virement(self):
        compt = 10000
        som = input("combien vouliez vous virer\n")
        som = int(som)
        if som <= self.solde:
            compt += som
            self.solde = self.solde - som
            print("vous avez effectuer un virement de", som)
            print("votre nouveau solde est ", self.solde)
        else:
            print("desole solde insuffisant")
ab = guichetier("adan", "azer123")
ab.depot()
ab.retret()
ab.virement()
