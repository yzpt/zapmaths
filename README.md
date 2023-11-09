# --- Work in progress editing Readme ---

# Zapmaths: Web application for arithmetic akills practice

## Presentation

Zapmaths is a web application for practicing arithmetic skills that I developed during my teaching career. It is used both in the classroom and at home. The numerical values of the questions are random and are automatically corrected. Students can practice at their own pace, and teachers can track their students' progress and help them target their difficulties.

I started it during the lockdown, relying on old memories and sames tutorials when I used to create websites in PHP/MySQL back in the 2000s. <u>The code is not clean at all, and the database management is quite messy. Nevertheless, it remains functional.</u> I wanted to make it available to my students as soon as possible, so I didn't take the time to learn how to do it properly.

Excel (question writing) --> Python (xls_to_csv_questions_generator.py) --> MySQL (phpMyAdmin) <--> PHP/HTML/CSS (LAMP Stack)

A version is currently available at the following address:

['https://zapart.ovh'](https://zapart.ovh)

You can log in with:

- login : demo01/demo02/.../demo99
- password  : demo02/demo02/.../demo99


<div style="display: flex; flex-wrap:wrap;">

![Screenshot](./img/screenshots/a.jpg)
![Screenshot](./img/screenshots/b.jpg)
![Screenshot](./img/screenshots/c.jpg)
![Screenshot](./img/screenshots/d.jpg)
![Screenshot](./img/screenshots/e.jpg)
![Screenshot](./img/screenshots/f.jpg)
![Screenshot](./img/screenshots/g.jpg)
![Screenshot](./img/screenshots/h.jpg)

</div>

## === to write : ===

## Editing questions on EXCEL

* generating semi-random values on EXCEL

* usage of Mathjax.js to display mathematical formulas

## Converting EXCEL to CSV with python

* usage of matplotlib.pyplot to generate graphs according to the values of the questions

* usage of base64 to encode images, specials questions, etc

## Web app

* minimal html/css/php/msql with phpMyAdmin

* SQL supervision

## Access to an anonymized and refactored real database sample

* just an idea, i'm quite focused on learning Airflow, Spark & Kafka right now.
