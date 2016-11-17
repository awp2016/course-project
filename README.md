# awp-project

Course Project for http://purepython.eaudeweb.ro

System prerequisites
--------------------

1. Install pip:

  ```
  wget https://bootstrap.pypa.io/get-pip.py
  sudo python get-pip.py
  ```

2. Install virtualenv

  ```
  sudo pip install virtualenv
  ```

Project installation
--------------------

1. Clone repository:

  ```
  git clone https://github.com/awp2016/course-project.git
  ```

2. Create virtual environment:

  ```
  cd course-project
  virtualenv sandbox
  ```

3. Activate environment:

  ```
  source sandbox/bin/activate
  ```

4. Install Django inside virtual environment:

  ```
  pip install Django
  ```

5. Apply migrations:

  ```
  ./manage.py migrate
  ```

6. Run development server:

  ```
  ./manage.py runserver
  ```