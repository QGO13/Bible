CREATE TABLE TESTAMENT(
   NOM_TESTAMENT VARCHAR(50),
   PRIMARY KEY(NOM_TESTAMENT)
);

CREATE TABLE LIVRE(
   Nom_livre VARCHAR(100),
   NOM_TESTAMENT VARCHAR(50) NOT NULL,
   PRIMARY KEY(Nom_livre),
   FOREIGN KEY(NOM_TESTAMENT) REFERENCES TESTAMENT(NOM_TESTAMENT)
);

CREATE TABLE CHAPITRE(
   Numero_CHAPITRE COUNTER,
   Verset_du_chapitre TEXT,
   Nom_livre VARCHAR(100) NOT NULL,
   PRIMARY KEY(Numero_CHAPITRE),
   FOREIGN KEY(Nom_livre) REFERENCES LIVRE(Nom_livre)
);