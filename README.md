# 🩺 AI-Based Remote Patient Monitoring System

Un système de surveillance à distance des patients basé sur l'IA, conçu pour surveiller en temps réel les données de santé des patients atteints de maladies chroniques. Ce projet utilise des algorithmes de détection d'anomalies pour alerter automatiquement les professionnels de santé en cas de détection de valeurs anormales.

---

## 🚀 Fonctionnalités
- **Surveillance en temps réel** des données de santé simulées (fréquence cardiaque, tension artérielle, saturation en oxygène).
- **Détection d'anomalies** basée sur un modèle d'IA (Isolation Forest).
- **Alertes automatiques** en cas de détection de lectures anormales.

---

## ⚙️ Technologies Utilisées
- **Python 3**
- **NumPy** pour la manipulation des données
- **Pandas** pour la gestion des séries temporelles
- **Scikit-learn** pour la détection d'anomalies (modèle Isolation Forest)

---

## 📥 Installation

1. Clonez le dépôt GitHub :
```bash
https://github.com/votre-utilisateur/ai-patient-monitoring.git
cd ai-patient-monitoring
```

2. Installez les dépendances :
```bash
pip install numpy pandas scikit-learn
```

3. Exécutez le script :
```bash
python patient_monitoring.py
```

Appuyez sur `Ctrl + C` pour arrêter la surveillance.

---

## 🧪 Exemple de Résultats
```plaintext
Starting real-time patient monitoring...
HR: 78.2, BP: 118.4, O2: 97.6%
HR: 180.9, BP: 250.2, O2: 85.4%
⚠️ ALERT: Abnormal health reading detected! Notify healthcare provider.
```

- ✅ **Lecture normale :** pas d'alerte.
- ⚠️ **Anomalie détectée :** alerte automatique.

---

## 🗂️ Structure du Projet
```
├── patient_monitoring.py   # Code principal de surveillance
├── README.md               # Documentation du projet
```

---

## ✅ Améliorations Futures
- Intégration de données réelles provenant de capteurs IoT.
- Notifications automatiques par e-mail/SMS.
- Tableau de bord pour la visualisation des données en temps réel.

---

## 🤝 Contribuer
1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature-nouvelle-fonction`).
3. Poussez vos modifications (`git push origin feature-nouvelle-fonction`).
4. Ouvrez une pull request.


## 📜 Licence
Ce projet est sous licence [MIT](LICENSE).

---

## 👨‍💻 Auteur
- **Nom de l'Auteur** - [Votre Profil GitHub](https://github.com/votre-utilisateur)


---

*"Surveiller aujourd'hui pour protéger demain."*

