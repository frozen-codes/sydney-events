import os
import subprocess
import sys
import time
from threading import Thread

def run_backend():
    """Run the Flask backend server"""
    os.chdir(os.path.join(os.path.dirname(__file__), 'backend'))
    
    # Check if virtual environment exists, if not create one
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
    
    # Activate virtual environment and install requirements
    if os.name == 'nt':  # Windows
        activate_script = os.path.join('venv', 'Scripts', 'activate')
        pip_path = os.path.join('venv', 'Scripts', 'pip')
        python_path = os.path.join('venv', 'Scripts', 'python')
    else:  # Unix/Linux/Mac
        activate_script = os.path.join('venv', 'bin', 'activate')
        pip_path = os.path.join('venv', 'bin', 'pip')
        python_path = os.path.join('venv', 'bin', 'python')
    
    # Install requirements
    print("Installing backend dependencies...")
    if os.name == 'nt':  # Windows
        subprocess.run(f"{python_path} -m pip install -r requirements.txt", shell=True)
    else:
        subprocess.run(f"source {activate_script} && pip install -r requirements.txt", shell=True)
    
    # Initialize database
    print("Initializing database...")
    if os.name == 'nt':  # Windows
        subprocess.run(f"{python_path} database/schema.py", shell=True)
    else:
        subprocess.run(f"source {activate_script} && python database/schema.py", shell=True)
    
    # Run Flask app
    print("Starting Flask backend server...")
    if os.name == 'nt':  # Windows
        subprocess.run(f"{python_path} app.py", shell=True)
    else:
        subprocess.run(f"source {activate_script} && python app.py", shell=True)

def run_frontend():
    """Run the React frontend server"""
    os.chdir(os.path.join(os.path.dirname(__file__), 'frontend'))
    
    # Install dependencies if node_modules doesn't exist
    if not os.path.exists('node_modules'):
        print("Installing frontend dependencies...")
        subprocess.run(['npm', 'install'], check=True)
    
    # Start React development server
    print("Starting React frontend server...")
    subprocess.run(['npm', 'start'], check=True)

if __name__ == "__main__":
    # Start backend in a separate thread
    backend_thread = Thread(target=run_backend)
    backend_thread.daemon = True
    backend_thread.start()
    
    # Give the backend some time to start
    time.sleep(5)
    
    # Start frontend (this will block until frontend is closed)
    run_frontend()
    
    print("Shutting down servers...") 