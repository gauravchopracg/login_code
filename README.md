# Automate Login using Selenium and Python

## Demo Video
https://youtu.be/_YsRRbYkv4U

**Video Recorded using the built-in Snipping Tool by pressing Win + Shift + R**

## To reproduce results and run it on your computer

1. Clone the repo

```bash
git clone https://github.com/gauravchopracg/login_code.git
cd login_code/
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate virtual environment
```bash
.\venv\Scripts\activate
```

4. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Add **EMAIL** and **PASSWORD**

a. open automate_login_code.py
b. on line number 23, email_input_box.send_keys("INSERT YOUR EMAIL ADDRESS HERE"), insert your email id
c. on line number 31, password_input_box.send_keys("INSERT YOUR PASSWORD HERE"), insert your password
d. save the file

5. run the code

```bash
python automate_login_selenium_python.py
```