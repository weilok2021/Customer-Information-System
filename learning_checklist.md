# 🧠 Learning Checklist — Customer Information System

Use this checklist to measure your progress as you build your project.  
Your goal: be able to **answer every question** confidently with your own code as proof.

---

## 1️⃣ Request Flow
- [ ] Can I explain the journey of a `POST /customers` request from route → service → repository → DB?
- [ ] Do I know where request parsing and validation happen?
- [ ] Can I describe what gets returned to the client?

**Ask yourself:**
- What function gets called first when I hit the endpoint?
- How does data move through each layer?
- What would break if the repository failed?

---

## 2️⃣ Data Storage & Retrieval
- [ ] Do I understand how the `Customer` model maps to the database table?
- [ ] Can I perform CRUD with ORM and raw SQL?
- [ ] Do I know how and when data is committed or rolled back?

**Ask yourself:**
- How is a customer created and persisted?
- What happens if a transaction fails halfway?
- How do indexes or unique constraints affect performance?

---

## 3️⃣ Business Logic
- [ ] Do I know what rules belong in `service.py` vs `repository.py`?
- [ ] Can I explain validations (e.g., unique emails)?
- [ ] Can I extend the logic to support features like “deactivate customer”?

**Ask yourself:**
- What validations happen before saving a customer?
- How would I add a new rule without touching the API?
- How can I unit-test business rules?

---

## 4️⃣ Failure Handling
- [ ] Do I handle 404, 400, and 500 errors clearly?
- [ ] Are errors logged in a readable, structured way?
- [ ] Do I know what exceptions the DB or framework might raise?

**Ask yourself:**
- What happens if the database connection fails?
- How do I prevent the app from crashing due to invalid input?
- How can I log errors for debugging in production?

---

## 5️⃣ Testing
- [ ] Can I run all my tests from a single command (e.g., `pytest` or `unittest`)?
- [ ] Do my tests cover both happy paths and error cases?
- [ ] Can I run tests without a real database (using mocks)?

**Ask yourself:**
- What’s the difference between a unit test and an integration test?
- How can I verify my endpoint returns correct responses?
- How do I know when I’ve tested “enough”?

---

## 6️⃣ Deployment
- [ ] Can I run the system with `docker-compose up`?
- [ ] Can I configure different environments using `.env` files?
- [ ] Do I know how to view logs and debug issues in a deployed app?

**Ask yourself:**
- How does the app load environment variables?
- How do I rebuild and redeploy quickly?
- What’s the difference between dev and prod configs?

---

## ✅ Milestone: “I can build and deploy a working backend.”
You can:
- Design folder structure and flow from scratch  
- Implement CRUD operations end-to-end  
- Write and run tests confidently  
- Deploy your system in a containerized environment  

---

## 🌱 Stretch Goals
- [ ] Add pagination and search for customers
- [ ] Implement authentication and user roles
- [ ] Add email or SMS notification integration
- [ ] Explore caching or async background jobs
