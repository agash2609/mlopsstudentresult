# Student Result Predictor (MLOps)

A beginner-friendly Flask machine-learning demo that predicts Pass/Fail from study hours, attendance, and internal marks. The model is trained on synthetic demonstration data; it is not an academically validated predictor.

## Files

- `train.py` — creates synthetic training data and trains a Logistic Regression model.
- `app.py` — Flask web interface for predictions.
- `Dockerfile` — builds and runs the application in Docker.
- `appspec.yml` and `scripts/deploy.sh` — AWS CodeDeploy deployment configuration for an Ubuntu EC2 instance.

## Run locally (Windows)

1. Install Python 3.12 and Git. Install Docker Desktop only if you want to test Docker.
2. Open this folder in VS Code.
3. In the VS Code terminal, run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python train.py
python app.py
```

4. Open `http://127.0.0.1:5000` in your browser.

If PowerShell blocks activation, open Command Prompt in VS Code and use `.venv\\Scripts\\activate.bat`.

## Run with Docker

```bash
docker build -t student-result-predictor .
docker run --rm -p 8080:5000 student-result-predictor
```

Open `http://localhost:8080`.

## Upload to GitHub

Create a repository on GitHub, then open a terminal in this folder and run (replace the URL with your repository URL):

```bash
git init
git add .
git commit -m "Initial student result predictor"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

## AWS deployment notes

This setup expects an Ubuntu EC2 instance with Docker, curl, and the AWS CodeDeploy agent installed. Configure the EC2 instance role, CodeDeploy service role, deployment group, and CodePipeline source/deploy stages in AWS. Allow inbound HTTP (port 80) in the EC2 security group. AWS usage may incur charges.

For a real production deployment, use HTTPS, restrict access, add monitoring, and validate the model on real representative data.
