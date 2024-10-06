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
