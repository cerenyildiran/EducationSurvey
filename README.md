# Education Satisfaction Survey Application
A Python-based application that allows educational institutions to gather feedback from teachers, parents, and students to evaluate and improve the quality of education.

## Features
- Role-based survey for teachers, parents, and students.
- Google Sheets integration for storing and managing responses.
- Real-time results display and feedback.
- Easy-to-use interface with role-specific options.
- Ability to exit the survey anytime with a single key press.

## Technologies Used
- **Python:** Core programming language for the survey logic.
- **Google Sheets API:** For storing and retrieving survey responses.
- **Node.js:** Used for serving the frontend and backend.
- **Heroku:** Hosting platform for deploying the application.

## Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/cerenyildiran/EducationSurvey.git
   cd EducationSurvey

2.Install the required Python packages:
pip install -r requirements.txt

3.Install the required Node.js packages (if applicable):
npm install

4.Run the application:
python run.py

5.Run the Node.js server: Start the Node.js server to serve the frontend or backend of the application:
node index.js

## Dependencies

The application relies on the following Python libraries, listed in the `requirements.txt`:

- **pyfiglet (1.0.2)**: Used to create large text banners in ASCII art, enhancing CLI output.
- **cachetools (5.3.1)**: Provides various cache mechanisms that can be used to manage temporary data.
- **google-auth (2.23.3)** and **google-auth-oauthlib (1.1.0)**: Handle authentication with Google APIs.
- **gspread (5.11.3)**: Simplifies interacting with Google Sheets for data storage and retrieval.
- **oauthlib (3.2.2)**, **requests-oauthlib (1.3.1)**: Extends requests to support OAuth for secure data access.
- **pyasn1 (0.5.0)**, **pyasn1-modules (0.3.0)**: Implements ASN.1 types and codecs, supporting the encoding and decoding of data.
- **rsa (4.9)**: Provides algorithms for RSA encryption, decryption, and signature verification.


## Deployment to Heroku

This guide provides step-by-step instructions on how to deploy the Education Satisfaction Survey Application to Heroku.

### Prerequisites

- A Heroku account. Sign up [here](https://signup.heroku.com/) if you don't have one.
- The Heroku CLI installed. Download it from [here](https://devcenter.heroku.com/articles/heroku-cli).

### Steps for Deployment

1. **Login to Heroku CLI:**
   Open your terminal and enter the following command to log in to the Heroku CLI:
 
```bash
heroku login
````
2. Create a Heroku App: To create a new app on Heroku with a unique name, type:
```bash
heroku create your-app-name
```
3. Set up Remote Repository: To add Heroku as a remote to your local git repository, enter:
```bash
git remote add heroku https://git.heroku.com/your-app-name.git

```
4. Add Config Vars: To set environment variables for your application on Heroku, use:
```bash
heroku config:set SOME_API_KEY=your_api_key

```
5. Deploy Your Application: Deploy your application to Heroku by pushing your code:
```bash
git push heroku master
```
6. Ensure Dynos are Running: After deploying, ensure that your app's dynos are running with:
```bash
heroku ps:scale web=1
```
7. Open Your Application: To open your deployed application in a web browser, use:
```bash
heroku open
```
### Verifying the Deployment
To verify that your application is running as expected, visit the URL provided by Heroku. If you encounter any issues, you can view the logs for troubleshooting with:
```bash
heroku logs --tail
```

## User Roles
The survey is tailored to three types of users:

- **Teachers:** Evaluate the curriculum, teaching methods, and overall learning environment.
- **Parents:** Provide feedback on their child's learning experience, communication with teachers, and support provided by the school.
- **Students:** Share their opinions on class engagement, teaching effectiveness, and personal development.

Choose your role when starting the survey to ensure the questions are relevant to your experience.

## Project Description
This project includes an education satisfaction survey application designed for teachers, parents, and students. The application can be used to assess the education experience, gather feedback, and improve the education processes.

## Demo

You can use the Heroku link to see the working version of the project.

https://edu-survey-9349e08d9a85.herokuapp.com

---

## How to use

1. Open your web browser and navigate to http://localhost:8000. This will take you to the web interface of the Education Satisfaction Survey Application.
![1](https://raw.githubusercontent.com/swecery/EducationSurvey/main/img/Screenshot1.png)

2. Examples are provided to facilitate user understanding in case of incorrect input.
![6](https://raw.githubusercontent.com/swecery/EducationSurvey/main/img/Screenshot6.png)

4. Depending on your role (teacher, parent, or student), you can choose the appropriate action.
![2](https://raw.githubusercontent.com/swecery/EducationSurvey/main/img/Screenshot2.png)

5. Answer the survey questions honestly and submit your responses.
![3](https://raw.githubusercontent.com/swecery/EducationSurvey/main/img/Screenshot3.png)

6. Press 'q' to exit the program at any time.
![4](https://raw.githubusercontent.com/swecery/EducationSurvey/main/img/Screenshot5.png)

7. After the survey is completed, the results are saved to the google sheets file.
![5](https://raw.githubusercontent.com/swecery/EducationSurvey/main/img/Screenshot4.png)

The Education Satisfaction Survey Application allows teachers, parents, and students to assess the educational experience, gather feedback, and make improvements to the education process.

## Code Quality and Standards

Our project is fully compliant with PEP8 standards, ensuring high-quality, readable, and maintainable code. We regularly run PEP8 checks to maintain these standards across the development lifecycle.

- **PEP8 Compliance:** We use tools like `flake8` and `black` to ensure our code adheres to PEP8 standards. This commitment to quality helps us ensure that our code is consistent and error-free.

![7](https://raw.githubusercontent.com/swecery/EducationSurvey/main/img/Screenshot7.png)

## User Value

The "Education Satisfaction Survey Application" is crafted to enhance the educational experience by leveraging feedback from key stakeholders: educational institutions, teachers, students, and parents. This application facilitates a dynamic feedback loop, enabling continuous improvement in educational quality and relevance.

### Benefits for Educational Institutions
- **Targeted Insights**: Gain actionable insights into the perception of courses and programs to enhance educational offerings.
- **Quality Control**: Regular feedback helps uphold and elevate educational standards, ensuring competitiveness in the evolving academic landscape.

### Benefits for Teachers
- **Professional Growth**: Feedback identifies strengths and areas for improvement, aiding professional development and teaching effectiveness.
- **Responsive Teaching**: Adapt teaching methods based on direct feedback to better meet student needs and enhance engagement.

### Benefits for Students
- **Empowered Participation**: Students have a direct say in their educational journey, encouraging active engagement and ownership of their learning process.
- **Optimized Learning Environments**: Feedback leads to adjustments that create more supportive and effective learning environments.

### Benefits for Parents
- **Informed Engagement**: Understand the educational setting more clearly to engage constructively with educators and institutions.
- **Advocacy for Standards**: Voice expectations and concerns to advocate for higher educational standards and better resources.

### Leveraging Technology
- **Global Access**: The online platform allows for feedback from any location at any time, overcoming geographical and temporal barriers.
- **Real-Time Adaptation**: Quick data processing enables swift responses to feedback, ensuring the educational ecosystem is agile and student-centric.

In essence, the "Education Satisfaction Survey Application" not only deepens the understanding of educational dynamics but also cultivates a collaborative environment where improvements are continually driven by direct stakeholder input. This approach ensures that educational experiences evolve and are consistently aligned with the needs and expectations of all involved parties.


## Roadmap

- **Q2 2024:**
  - Implement machine learning algorithms to analyze survey responses.
  - Add multilingual support for the survey.

- **Q3 2024:**
  - Develop a mobile app version of the survey.
  - Expand the types of roles to include school administrators.

## Contributing
We welcome contributions to improve this project! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code follows the PEP8 guidelines and includes appropriate documentation.

## Accreditation

This project was developed as part of the curriculum at Code Institute, focusing on real-world application of software development skills. The project has been rigorously evaluated and approved by Code Institute, ensuring it meets their high standards for educational quality and relevance.

### Code Institute

Code Institute is dedicated to providing industry-relevant education and training in software development, equipping students with the skills needed to succeed in the tech industry. This project aligns with their commitment to practical, hands-on learning experiences.

For more information about Code Institute and their programs, visit [Code Institute's website](https://codeinstitute.net).

