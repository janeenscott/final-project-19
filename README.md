# Kind Regards

Kind Regards is a pen pal matching system that pairs students of the 
same age who come from different backgrounds and provides a platform for 
them to build a friendship.

When students sign up, they enter their age and select their city, and 
gain access to their profile page which provides more in-depth data about 
their city, pulled from the [Teleport API](https://developers.teleport.org/api/).

Once the singup window has closed, an admin must log in and use a custom 
admin action to run the pairing program. Once pen pals are assigned, 
the user can see their pen pal on their profile, can view information about 
both cities, and has access to a messaging feature.

The pairing program matches students who are the same age, but who's 
quality-of-life scores for their cities differ significantly. The hope is 
that by creating a platform for these students to talk and build a friendship, 
they will become more globally engaged, empathetic, and compassionate citizens.

## Technologies, Libraries, and APIs Used

* Python/Django
* JavaScript/React
* Django Rest Framework
* React Draft Wysiwyg Editor
* Amazon S3 Buckets
* Bootstrap
* Pillow
* Teleport API

The landing page, user authentication, about, and profile pages are written in  
Python using the Django framework. The messaging piece of the application 
was written in JavaScript using the React library.
