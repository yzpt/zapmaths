# Zapmaths: Web application for practicing calculation skills

## Presentation

Zapmaths is a web application I created during my teaching career, designed for both classroom and home use. The application generates questions, corrections, graphics, diagrams, and schemas using random values. This allows students to practice at their own pace, while I can monitor their progress and activities.

I started it during the lockdown, relying on old memories and sames tutorials when I used to create websites in PHP/MySQL back in the 2000s. <u>The code is not clean at all, and the database management is quite messy. Nevertheless, it remains functional.</u> I wanted to make it available as soon as possible, so I didn't take the time to learn how to do it properly.

Excel (question writing) --> Python (xls_to_csv_questions_generator.py) --> MySQL (phpMyAdmin) <--> PHP/HTML/CSS (LAMP Stack)

A release is currently available at the following address:

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

### Editing questions on EXCEL

* generating semi-random values on EXCEL
* usage of Mathjax.js to display mathematical formulas

### Converting EXCEL to CSV with python

* PIL & matplotlib.pyplot to generate graphs, diagrams and images according to the values of the questions

### Web app

* Minimal html/css/php/msql with phpMyAdmin
