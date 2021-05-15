# DevOps Core Fundamental Project Specification

## Introduction
---
The purpose of this document is to outline the Fundamental project
specification that you will be working on during the training. It will
be treated as the document that outlines your project and sets the
expectations.

This project will involve concepts from all core training modules; more
specifically, this will involve:

- Project Management
- Python Fundamentals
- Python Testing
- Git
- Basic Linux
- Python Web Development
- Continuous Integration
- Cloud Fundamentals
- Databases

This is an individual project and can be on any subject you deem fit
of encapsulating all aspects of the aforementioned modules. This could
be a business case, such as a library or supermarket system, or
something to do with a hobby of yours.

This is purposefully open as we want to endorse creativity and give you
an opportunity to do a project that you have full command over. It is in
your interest do something you are passionate about, as past experience
has shown these to be the best projects.

You should treat this project as a piece of work that you must
personally complete, you must not collaborate with your peers to
complete this project.

## Objective
---
Your overall objective with this project is the following:

- To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.
As Trainers, this enables us too:

- Objectively assess your capability with the technologies and
concepts you have been taught.
- Assess your development against SFIA.

## Scope
---
The requirements set for the project are below. Note that these are a
minimum set of requirements that you can add to during the project.

The requirements of the project are as follows:

- A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.
- A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
- Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
- A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board
- Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
- A functioning front-end website and integrated API's, using Flask.
- Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

You should consider the concept of MVP (Minimum Viable Product) as you
plan your project, completing all the requirements above before you add
extra functionality that is not specified above.

## Constraints
---
Your application needs to be CRUD functional, however as part of your
training you will create a CRUD functional Flask Blog complete with
Registration and Login Functionality. If you choose to include this
Registration and Login functionality in your Project it **will not count
towards your final score.**

When creating the entities for your project, you must create **at least
2 tables that share a relationship.** During your training you will
create a system that use Users and Posts, **you must create 2 different
entities with a different relationship.**

In layman's terms, the Flask Blog project should be used as a reference
architecture, not as the foundation for your project.

The time constraint of this application will be discussed when the
specification is given out, as this can fluctuate based on several
factors.

The other constraint for this is certain technology that needs to be
used. The application needs to utilise the technology discussed during
the training modules. The tech stack required would be the following:

- Kanban Board: Trello or an equivalent Kanban Board
- Database: GCP SQL Server or other Cloud Hosted managed Database.
- Programming language: Python
- Unit Testing with Python (Pytest)
- Integration Testing with Python (Selenium)
- Front-end: Flask (HTML)
- Version Control: Git
- CI Server: Jenkins
- Cloud server: GCP Compute Engine

## Deliverable
---
The final deliverable for this project is the completed application with
full documentation around utilisation of supporting tools. The
Documentation must be provided as a **README.md** at the root of your
folder structure. This will require a fully functional application based
on the domain that you have chosen.

A presentation of work may also be required towards the end of the
deadline. However, you will be required to produce weekly reports of any
designs and work created throughout the duration of the project.