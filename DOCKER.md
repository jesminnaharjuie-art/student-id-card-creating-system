# Docker Compose Guide - Student ID Card Generator System

## Prerequisites

- Docker (version 20.10+)
- Docker Compose (version 1.29+)
- At least 2GB free disk space
- Ports 5173 and 8000 available

## Installation

### Windows
1. Download and install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
2. Docker Compose is included

### Mac
1. Download and install [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop)
2. Docker Compose is included

### Linux
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Quick Start

### 1. Start Services

```bash
# Navigate to project root
cd sims-project

# Start all services in background
docker-compose up -d

# Or start in foreground (for debugging)
docker-compose up
```

### 2. Access Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### 3. Default Login

- **Username**: admin
- **Password**: admin123

## Common Commands

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Stop Services
```bash
docker-compose down
```

### Stop and Remove Data
```bash
docker-compose down -v
```

### Rebuild Services
```bash
docker-compose build --no-cache
```

### Restart Services
```bash
docker-compose restart
```

### Execute Commands in Container
```bash
# Backend shell
docker exec -it sims-backend bash

# Frontend shell
docker exec -it sims-frontend bash

# Run Python command in backend
docker exec sims-backend python -c "print('Hello')"
```

## Configuration

### Environment Variables

Edit `.env.docker` or create `.env`:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///./sims.db
VITE_API_URL=http://localhost:8000
```

Then pass to docker-compose:
```bash
docker-compose --env-file .env up -d
```

## Development Mode

The docker-compose.yml is configured for development with:
- Hot reload enabled
- Volume mounts for source code
- Debug logging

For changes to take effect:
```bash
# Rebuild and restart
docker-compose up -d --build
```

## Production Deployment

For production, modify `docker-compose.yml`:

1. Change frontend Dockerfile CMD to use `serve` instead of `npm run dev`
2. Set `restart: always` for services
3. Use environment-specific `.env` file
4. Consider adding:
   - Nginx reverse proxy
   - SSL/TLS certificates
   - Health checks
   - Resource limits

Example production settings:
```yaml
services:
  frontend:
    restart: always
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
  backend:
    restart: always
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
```

## Troubleshooting

### Port Already in Use
```bash
# Find and kill process using port
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :8000
kill -9 <PID>
```

### Permission Denied (Linux)
```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

### Container Won't Start
```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild
docker-compose build --no-cache
docker-compose up
```

### Database Issues
```bash
# Reset database
docker-compose down -v
docker-compose up -d
```

### API Connection Issues
```bash
# Check if services are running
docker-compose ps

# Test backend health
curl http://localhost:8000/api/v1/health

# Check container IP
docker inspect sims-backend | grep IPAddress
```

## Health Checks

Monitor service health:
```bash
# Backend health
curl http://localhost:8000/api/v1/health

# Frontend status (when running)
curl http://localhost:5173
```

## Cleanup

```bash
# Remove all containers, volumes, and networks
docker-compose down -v

# Remove unused Docker resources
docker system prune -a

# Remove all images
docker rmi $(docker images -q)
```

## Advanced: Custom Network

To connect other services to SIMS network:
```bash
# Get network name
docker network ls | grep sims

# Connect container to SIMS network
docker network connect sims_sims-network <container_id>
```

## Performance Tuning

### Increase Memory (if needed)
```bash
# In docker-compose.yml under services
deploy:
  resources:
    limits:
      memory: 2G
```

### Resource Limits
```yaml
services:
  backend:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '1'
          memory: 512M
```

## Monitoring

### Check Resource Usage
```bash
docker stats sims-backend sims-frontend
```

### View Running Processes
```bash
docker top sims-backend
docker top sims-frontend
```

## Support

For detailed Docker documentation:
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

For SIMS issues:
- Check logs: `docker-compose logs`
- Review README.md
- Check API docs: http://localhost:8000/docs
