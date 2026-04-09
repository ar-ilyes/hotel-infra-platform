# Hotel & Infra Platform

Monorepo pour les services hôteliers Accor :
- **src/payment/** — Système de paiement (Apple Pay, Google Pay, QR Code)
- **src/checkin/** — Check-in/check-out mobile
- **src/keys/** — Clés digitales Bluetooth
- **src/loyalty/** — Programme de fidélité ALL
- **infra/** — Infrastructure as Code (Terraform, K8s)

## Stack technique
- Python 3.12 + FastAPI
- PostgreSQL + Redis
- GKE (Google Kubernetes Engine)
- Prometheus + Grafana

## CI/CD
- GitHub Actions pour les tests et le build
- Déploiement automatique sur staging via merge sur `develop`
- Déploiement prod via release tags
