### MGS 406 Flask Project Demo 

If you have a Python virtual environment, activate it with the following command:

```bash
source venv/bin/activate
```

If you don't have a Python virtural environment or you just created a new work directory, use the following commands to create a new virtual environemnt:  

```bash
# You may need to use python3 to replace python depending on your system settings 
python -m venv venv 

# Activate the venv and check the pip list  
source venv/bin/activate  
pip list  

# Install necessary python packages using pip install  
pip install ____________  

# You can use the requirements.txt file to install all necessary packages for this example project  

pip install -r requirements.txt  
```


Run the Flask app:
```bash
python hello.py
```

The Flask app will be running on http://127.0.0.1:5000 and supports the following routes:

```bash
/python
/user/<name>

/admin
/guest/<guest>
```