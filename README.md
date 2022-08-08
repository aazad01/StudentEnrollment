<h1>Total of 27 tests</h1>
<b>2 Failures</b>
- 1. Allowed to add a student without a last name
- 2. Allowed to add a student without a nationality

<h2>Technical Test:</h2>
<h3>API Test</h3>
<p>Using Cucumber/Behave test scripts, BDD approach</p>
<b>Restful API Requirements:</b>

- Add new student
- Update existing student
- Delete existing student
- Fetch student data
  - can fetch all student
  - can fetch students based on student id
  - can fetch all student in a class
  - can fetch with student id and class together
______________________________
<h3>WebUI Test</h3>
<b>UI Requirements:</b>

- login feature 
______________________________


Known Issue: 
- Both the web.feature and api.feature are executed one after the other. 
Only one works properly.  Suspecting a yeild is need.  
Just run it a few times to get the other results.  

Todo:
- Fix known issue
- add a environment.py to the api/features folder, for additional fixtures
- generate a report.


