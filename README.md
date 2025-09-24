# Gabon Citoyen - Backend API

API Django REST pour l'application mobile Gabon Citoyen, une plateforme citoyenne pour suivre l'actualité parlementaire gabonaise et faciliter l'accès aux services administratifs.

## 🚀 Fonctionnalités

- **Authentification** : Inscription, connexion, gestion des profils utilisateurs
- **Parlement** : Suivi des projets de loi, votes, sessions parlementaires
- **Députés** : Profils des députés, activités, messages citoyens
- **Assistant IA** : Service d'assistance pour les démarches administratives
- **Diaspora** : Services spécifiques aux Gabonais de l'étranger
- **Analyse Législative** : Analyse automatique des textes de loi avec IA

## 🏗️ Architecture

- **Framework** : Django 5.0.7 + Django REST Framework
- **Base de données** : SQLite (développement), PostgreSQL (production)
- **Cache** : Redis
- **Tâches asynchrones** : Celery
- **IA** : OpenAI GPT pour l'analyse des textes de loi

## 📦 Installation

### Prérequis
- Python 3.9+
- pip
- Redis (pour Celery)
- PostgreSQL (pour la production)

### Configuration

1. **Cloner le repository**
```bash
git clone https://github.com/manelMoussavou/gabon-citoyen-backend.git
cd gabon-citoyen-backend
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configuration des variables d'environnement**
```bash
cp .env.example .env
# Éditer le fichier .env avec vos configurations
```

5. **Migrations de base de données**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

7. **Lancer le serveur**
```bash
python manage.py runserver
```

## 📚 API Documentation

### Endpoints principaux

#### Authentification
- `POST /api/v1/auth/register/` - Inscription
- `POST /api/v1/auth/login/` - Connexion
- `GET/PUT /api/v1/auth/profile/` - Profil utilisateur

#### Parlement
- `GET /api/v1/parliament/bills/` - Liste des projets de loi
- `GET /api/v1/parliament/bills/{id}/` - Détail d'un projet de loi
- `GET /api/v1/parliament/bills/active/` - Projets de loi actifs
- `GET /api/v1/parliament/bills/recent/` - Projets de loi récents

#### Députés
- `GET /api/v1/deputies/` - Liste des députés
- `GET /api/v1/deputies/{id}/` - Détail d'un député
- `GET /api/v1/deputies/my-deputy/` - Mon député (basé sur la circonscription)
- `POST /api/v1/deputies/messages/create/` - Envoyer un message à un député

#### Assistant
- `GET /api/v1/assistant/procedures/` - Liste des démarches administratives
- `POST /api/v1/assistant/chat/` - Chat avec l'assistant IA

#### Diaspora
- `GET /api/v1/diaspora/services/` - Services consulaires
- `GET /api/v1/diaspora/events/` - Événements communautaires

#### Analyse Législative
- `POST /api/v1/analysis/analyze/` - Analyser un texte de loi
- `GET /api/v1/analysis/history/` - Historique des analyses

## 🔧 Configuration

### Variables d'environnement

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True

# Database
DATABASE_URL=postgres://user:password@localhost:5432/gabon_citoyen

# Redis
CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379

# OpenAI
OPENAI_API_KEY=your-openai-api-key

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 🔄 Tâches Celery

Pour lancer les workers Celery :

```bash
# Dans un terminal séparé
celery -A gabon_citoyen worker -l info

# Pour le planificateur (si nécessaire)
celery -A gabon_citoyen beat -l info
```

## 🧪 Tests

```bash
python manage.py test
```

## 📊 Administration

L'interface d'administration Django est disponible à `/admin/` avec les fonctionnalités suivantes :

- Gestion des utilisateurs et permissions
- CRUD des projets de loi et votes
- Gestion des députés et leurs activités
- Modération des messages citoyens
- Suivi des analyses IA

## 🚀 Déploiement

### Production avec Docker

```bash
# Build de l'image
docker build -t gabon-citoyen-backend .

# Lancement avec docker-compose
docker-compose up -d
```

### Variables de production

- Utiliser PostgreSQL au lieu de SQLite
- Configurer Redis pour la production
- Activer HTTPS
- Configurer les logs
- Paramétrer les sauvegardes

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit les changements (`git commit -am 'Ajouter nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Équipe

- **Développement Backend** : [Manel Moussavou](https://github.com/manelMoussavou)

## 🔗 Liens utiles

- [Application Mobile](https://github.com/manelMoussavou/gabon-citoyen-mobile)
- [Documentation API](https://api.gaboncitoyen.com/docs/)
- [Site Web](https://gaboncitoyen.com)

---

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue ou nous contacter directement.
