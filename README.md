## Internship assignment
### TapCheif Search

[Cloud Deployment](https://tapcheifassignment.herokuapp.com)
Enter a passage or a pdf to form a Invereted Index
on the document and search any word in O(1) time.
Search, Storing and inverted indexing is done on Server Side
to untask the client-side.
- Indexing is automatically perform as soon as a passage/pdf is uploaded.
- Searching is integrated in the same page and called via AJAX calls from seamless experience.
- Index is cleared automatically cleared upp submitting an empty passage.
- No data is stored in the server side, and Cross-site request forgery is implemented to ensure security of data.
- Note: pdf parsing can only be used in local machine for now, since herou doesn't allow media files to be uploaded.

Tech Stack used -> Python(Django), Vanilla Frontend.


Setup
```
git clone https://github.com/xritzx/tapcheif_assignment.git
cd tapcheif_assignment
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 
HEAD TO http://127.0.0.1:8000/
```
