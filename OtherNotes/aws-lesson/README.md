# PART 1 - Create AWS Account

### goto: https://aws.amazon.com/ and click "sign in to console"
<img src="assets/01_sign_in_to_console.png">

### Click "Create a new AWS account"
<img src="assets/02_create_new_account_button.png">

### Fill in Email / password / username
<img src="assets/03_create_new_account_form.png">

### Select personal account
<img src="assets/04_create_new_account_form_2.png">

### Add credit card details
<img src="assets/05_create_new_account_form_3_payment.png">

### Setup SMS 2FA authentication
<img src="assets/06_create_new_account_form_4_sms.png">

### Select basic plan
<img src="assets/07_select_basic_plan.png">

### Sign in to console after account creation
<img src="assets/08_sign_in_to_console_2.png">

### Sign in as root user
<img src="assets/09_sign_in_form.png">

### Select EC2
<img src="assets/10_select_ec2.png">

### Select Instances
<img src="assets/11_select_instances.png">

### Select Launch Instances
<img src="assets/12_select_launch_instances.png">

### Select Ubuntu Server 20.04, 64-bit
<img src="assets/13_select_ubuntu20.png">

### Select t2.micro
<img src="assets/14_select_t2micro.png">

### Select next until security group
<img src="assets/15_configure_instance_details.png"><br>
<img src="assets/16_add_storage.png"><br>
<img src="assets/17_add_tags.png"><br>

### Configure Security group
- Add HTTP
- Add HTTPS
- Add Custom TCP with port range 5000
<img src="assets/18_configure_security_group.png"><br>

### Review and Launch
*image detals may not be matching. please ignore discrepencies*
<img src="assets/19_review.png">

### Create New Key Pair
- Select "Create a new key pair
- give the key a name
- download key pair
- **DO NOT LOSE THIS KEY!**
- Launch instance

<img src="assets/20_create_new_key_pair.png">

### View Instance
nothing interesting here. next!
<img src="assets/21_instance_being_launched.png">

### Select instance
Select the instance after it is running.
<img src="assets/22_instance_dashboard.png">

### Select instance
Connect to the terminal<br>
<img src="assets/23_connect.png"><br>
<img src="assets/24_connect2.png">

### Check point!
If you see this, you are at the right place

<img src="assets/25_browsershell.png" width="400">

# PART 2 - Running flask app on AWS

## About
This is an educational project intended to introduce basic concepts of running flask on aws. It is by no means secure or production grade.

## Instructions Part 1 - Local Computer

### clone this repo
We will clone this repo to your local computer. Open `Git Bash / Terminal` and type:
```
git clone https://github.com/mrivantan/aws-lesson.git
```

### Create a new **blank** repo in your own github account
Use your personal github not `git.generalassemb.ly`
- public
- no readme
- no .gitignore
- nothing

<img src="assets/26_new_repo.png">

### Change the origin to your repo
```
git remote set-url origin http://github.com/YOU/YOUR_REPO.git
```
The repo is similar to the previous lesson on APIs. At this point, let's assume that you know how to get your project to this current state.

```
git add .
git commit -m "my first flask app for aws"
git push origin main
```

## Instructions Part 2 - AWS terminal
Now that we have our flask app and all the necessary files in github, we are ready to clone it into AWS.

Return to our AWS terminal

<img src="assets/25_browsershell.png" width="400">

### Install tools
- `python3-pip` is the pip package manager
- `git` lets us clone from our repo
- `tmux` lets us run the flask server in the background
```
sudo apt update
sudo apt install python3-pip git tmux
```

### Clone the repo into your aws instance
change the address to **Your own repo address**
```
git clone https://github.com/your/repo.git
```

### Create a virtual environment
```
cd aws-lesson
pip3 install virtualenv
python3 -m virtualenv -p python3 env
source env/bin/activate
```

### Install dependency packages
This will install all packages described in the `requirements.txt` file
```
pip install -r requirements.txt
```

### Create a new session
If we were to run our flask app currently, the app will shutdown when we close the terminal. By creating a tmux session, we can run the flask app even after the terminal is closed.

https://github.com/tmux/tmux/wiki/Getting-Started

https://tmuxcheatsheet.com/
```
tmux new -s app_session
```

### Start the flask app
```
cd deployment
export FLASK_ENV=development
export FLASK_APP=app.py
flask run --host=0.0.0.0
```

### Try your new API
```
http://YOUR_EC2_PUBLIC_URL:5000/api/diabetes?x=0,1,2,3,4,5,6,7,8,9

for example:
http://ec2-18-191-183-22.us-east-2.compute.amazonaws.com:5000/api/diabetes?x=0,1,2,3,4,5,6,7,8,9
```