# wikipedia-scraper
Project wikipedia-scraper by [Alex Kim](https://github.com/alexandrejeonghwankim-lab) and [Sooyoung Lee](https://github.com/patoobyte)

🧰 Built with 🧰  
<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python logo" style="width:20%; height:auto;">

---

## ✨ Description ✨

A program that builds a JSON file with the political leaders of each country you get from an [API](https://country-leaders.onrender.com/docs):  

The file includes, for each leader:  
	- Full name  
	- Date of birth  
	- Date of death (if applicable)  
	- Mandate period  
	- Wikipedia page URL  
	- First paragraph of their Wikipedia page  

## 🗃️ Structure 🗃️

```
./wikipedia-scraper/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── dev/
│   ├── Alex_sandbox_notebook.ipynb
│   └── sooyoung_sandbox.ipynb
└── src/
    ├── __init__.py
    ├── api_client.py
    └── html_scraper.py
```

## 💻 Installation & Usage 🔨

(add installation steps)

1. Clone the repository to your local machine.

2. Run the script with  
```
python main.py
```
or 
```
python3 main.py
```

3. The script:  
	- Connects to the Country Leaders API
	- Requests a valid API cookie
	- Retrieves the list of supported countries
	- Retrieves the leaders for each country
		- If the cookie expires, the script requests a new one
	- Visits each leader's Wikipedia page
	- Extracts the first biographical paragraph
	- Cleans the extracted text
		- Removes citation brackets and extra whitespace
	- Adds the cleaned paragraph to each leader's data
	- Stores the final result in a `.json` file

## 🏃 Timeline 🏃

The project was completed over 3 days.

## 🐈‍⬛ Personal Situation 🐈‍⬛

The project was done as part of the AI & Data Science bootcamp at BeCode.org.
