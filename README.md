# FindayTube — Télécommande YouTube à distance

FindayTube est une application Flask permettant de contrôler YouTube sur un PC à distance via un téléphone.  
Elle offre des fonctionnalités simples et pratiques : recherche de vidéos, lecture/pause, vidéo suivante et vidéo précédente, le tout depuis une interface web responsive.

---

## 🚀 Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/toncompte/FindayTube.git
cd FindayTube
```

---

2. **Créer et activer un environnement virtuel**

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
# ou
.\venv\Scripts\activate     # Windows

```
---

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```
---

⚙️ Utilisation

Lancer le serveur Flask :

```bash 
python run.py
```

Depuis ton téléphone ou navigateur, accéder à :

http://<IP_de_ton_PC>:5000

    Remplace <IP_de_ton_PC> par l'adresse locale de ta machine (ex : 192.168.43.10)

    ---

🎯 Fonctionnalités

    Recherche YouTube à distance via une interface simple

    Contrôle lecture/pause, vidéo suivante et précédente

    Interface responsive adaptée aux mobiles

    Synchronisation avec YouTube sur le PC via des raccourcis clavier simulés

    ---

🛠️ Détails techniques

    Flask pour le serveur web

    pyautogui pour simuler les actions clavier sur le PC

    HTML/CSS simple et responsive pour l’interface utilisateur

    ---

⚠️ Remarques importantes

    Ce projet fonctionne principalement sur Linux (testé sur Arch Linux avec Firefox)

    Nécessite que la fenêtre du navigateur YouTube soit active pour que les raccourcis clavier fonctionnent correctement

    Ouvrir le port 5000 dans le firewall pour accéder depuis d’autres appareils

📄 License

MIT License © 2025 Dally Maminomenjanahary

Merci d’avoir utilisé FindayTube !
N’hésite pas à contribuer ou poser des questions.
