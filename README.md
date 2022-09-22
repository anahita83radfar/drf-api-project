# DRF API project

DRF API project is the backend API for the front-end React app [Friends](https://friends-4hk0.onrender.com), using Django REST Framework to return HTML documents, only JSON data. This lets users LIST, SEARCH, CREATE, RETRIEVE, UPDATE and DELETE the resource inter alia the profiles, posts, comments, likes, and followers. For instance, the user will be able to CREATE a new comment, RETRIEVE, UPDATE or DELETE a previously created one, or LIST and SEARCH all of the comments.

 # Features
 
- ### The Home page
 ![The Home page](/media/images/readme/home.jpg)
 
 The Home page url path : https://drf-api-project.onrender.com

- ### The Profiles page
 ![The Profiles page](/media/images/readme/profiles.jpg)

 The Profiles page url path : https://drf-api-project.onrender.com/profiles

 On this page, the user can see the list and number of profiles created by data that comes from the front-end React app [Friends](https://friends-4hk0.onrender.com). Each profile includes the id of the profile, owner of the profile which is an instance of user username, profile created and updated date, profile owner name, email, image, and profile content, number of posts created by the profile owner, the number of followers and following, id of profile that profile owner follows and check if the currently logged in user is the owner of the profile.

 - ### The Posts page
 ![The Posts page](/media/images/readme/posts.jpg)

 The Posts page url path : https://drf-api-project.onrender.com/posts

 On this page, the user can see the list and number of posts created by the users of the front-end React app [Friends](https://friends-4hk0.onrender.com). Each post includes the id of the post, owner of the post which is an instance of user username, the post created and updated date, post title, excerpt, content and image, the profile id and image of post owner, post image filter, number of likes and comments, id of liked post by post owner and check if the currently logged in user is the owner of the post.

  - ### The Comments page
 ![The Comments page](/media/images/readme/comments.jpg)

 The Comments page url path : https://drf-api-project.onrender.com/comments

 On this page, the user can see the list and number of comments on the posts created by the users of the front-end React app [Friends](https://friends-4hk0.onrender.com). Each comment includes the id of the comment, the owner of the comment which is an instance of the user username, the id of the post that the user leaves a comment, the comment created and updated date, the content of the comment, the profile id and image of the owner of the comment, check if the comment is active and the currently logged in user is the owner of the comment.

  - ### The Likes page
 ![The Likes page](/media/images/readme/likes.jpg)

  The Likes page url path : https://drf-api-project.onrender.com/likes

  On this page, the user can see the list and number of likes on the posts created by the users of the front-end React app [Friends](https://friends-4hk0.onrender.com). Each like includes the id of the like, the owner of the like which is an instance of the user username, the id of the post that the user liked, and the like created date.

  - ### The Followers page
 ![The Followers page](/media/images/readme/followers.jpg)

 The Followers page url path : https://drf-api-project.onrender.com/followers
 
On this page, the user can see the list and number of users followers. It includes the id, the owner that follows, the profile id and name of the follower, and the following created date.

# Database Model

![Diagram](/media/images/readme/database.jpg)

# Dependencies

The libraries below have been used for this project:

- django-cloudinary-storage

   To connect the project to Cloudinary for the upload and storage of images
- Pillow

   To add image processing capabilities
- django-filter

   To apply filters based on a specific condition
- dj-rest-auth

   To handle authentication and add JSON Web Tokens to the project
- dj-rest-auth[with_social]

   To enable a standard registration process
- djangorestframework-simplejwt

   To use JWT authentication
- dj-database-url psycopg2

   To use Heroku Postgres database
- Gunicorn

   To run the project on a suitable server for production
- django-cors-headers

   To deal with CORS, which stands for cross-origin-resource-sharing

# Testing

   - ### Manual test case template
   The document below demonstrates the individual test cases and shows that the expected results are gotten.

  ![Manual test case template](/media/images/readme/Manual-Test-Case-Template.jpg)

### Validator Testing

- PEP8
   - No errors were returned from PEP8online.com

# Deployment
[DRF API project](https://drf-api-project.onrender.com) was deployed to Heroku.
- Steps for deployment:
  - Create a Virtual Environment
  - Install Project Dependencies
  - Update Local Database Schema
  - Run a Local Development Server
  - Fork or clone this repository
  - Create a new Heroku app
  - Update Remote Database Schema
  - Link the Heroku app to the repository
  - Click on **Deploy**

# Credits
### Content
- The commented code in the project is taken from CI [drf-api](https://github.com/Code-Institute-Solutions/drf-api/tree/2c0931a2b569704f96c646555b0bee2a4d883f01) project.