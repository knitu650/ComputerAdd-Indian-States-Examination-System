// This script can be run with `mongoimport` or a custom seeding script.
// Example: mongoimport --db user-db --collection users --file userSeeds.json --jsonArray

[
  {
    "username": "student1",
    "email": "student1@example.com",
    "password": "hashed_password_1", // In a real scenario, this would be properly hashed
    "role": "student",
    "createdAt": { "$date": "2023-10-01T10:00:00Z" }
  },
  {
    "username": "admin1",
    "email": "admin1@example.com",
    "password": "hashed_password_admin",
    "role": "admin",
    "createdAt": { "$date": "2023-10-01T09:00:00Z" }
  }
]