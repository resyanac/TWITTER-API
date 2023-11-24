


# Introduction
Hello, Resya here! 23 years old girl in +8 GMT (East Borneo) timezone. I am a Tax Collector and software engineer. 

# Twitter API

This is a simplified version of a Twitter-like API built with Flask. The API includes features for user registration, login, posting tweets, following/unfollowing users, and retrieving user profiles.

## Routes

### Registration and Login

- **Registration**
  - **Endpoint:** POST `/auth/registration`
  - **Description:** Register a new user with a unique username, password, and bio (maximum 200 characters).

- **Login**
  - **Endpoint:** POST `/auth/login`
  - **Description:** Log in with valid credentials to obtain an authentication token.
![Screenshot 2023-11-24 at 20 27 39](https://github.com/RevoU-FSSE-2/Week-21-resyanac/assets/135514670/261f6718-841c-46e5-ba5d-b3cea8c5e563)
![Screenshot 2023-11-24 at 20 27 54](https://github.com/RevoU-FSSE-2/Week-21-resyanac/assets/135514670/1c8f4f26-01eb-41cc-9daf-2eb48cb922b2)

### User Profile

- **Get User Profile**
  - **Endpoint:** GET `/user/`
  - **Description:** Retrieve the user profile of the currently logged-in user. Includes username, bio, followers, following statistics, and the 10 most recent tweets.

![Screenshot 2023-11-24 at 20 28 04](https://github.com/RevoU-FSSE-2/Week-21-resyanac/assets/135514670/2c67f281-0932-40bd-a998-72260f323d2a)


### Tweets

- **Post a Tweet**
  - **Endpoint:** POST `/tweet/`
  - **Description:** Post a new tweet with a maximum of 150 characters.

![Screenshot 2023-11-24 at 20 28 14](https://github.com/RevoU-FSSE-2/Week-21-resyanac/assets/135514670/92c5da07-b9e3-45c0-b95b-359424d6d3e6)


### Following/Unfollowing Users

- **Follow/Unfollow User**
  - **Endpoint:** POST `/following/:id`
  - **Description:** Follow or unfollow a user identified by their `id`. Validation prevents users from following themselves.
![Screenshot 2023-11-24 at 20 28 23](https://github.com/RevoU-FSSE-2/Week-21-resyanac/assets/135514670/716ddf4c-5580-4045-9662-124526736bb8)

## Technologies Used

- Flask
- PostgreSQL (Supabase.com)
- SQLAlchemy
- Token-based authentication

## Project Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Set up a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   flask run
   ```

Enjoy using this simple Twitter API! If you encounter any issues or have suggestions, feel free to contribute or raise an issue.
