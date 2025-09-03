# Deploy Daman API to Render

## Quick Deploy Steps

### 1. Push to GitHub
```bash
cd f:\AiPredictor\api\Daman
git init
git add .
git commit -m "Initial Daman API"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/daman-api.git
git push -u origin main
```

### 2. Deploy on Render
1. Go to [render.com](https://render.com)
2. Sign up/login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Use these settings:
   - **Name**: `daman-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Plan**: Free

### 3. Get Your API URL
After deployment, you'll get a URL like:
```
https://daman-api-xyz123.onrender.com
```

### 4. Update Flutter App
Replace in `web_scraper_service.dart`:
```dart
// OLD
Uri.parse('http://localhost:8080/history?pageSize=20')

// NEW  
Uri.parse('https://YOUR-API-URL.onrender.com/history?pageSize=20')
```

## API Endpoints
- `GET /latest` - Current game info
- `GET /history?pageSize=20` - Game results
- `GET /predict?limit=20` - AI prediction

## Test Your Deployed API
```bash
curl https://YOUR-API-URL.onrender.com/history?pageSize=10
```
