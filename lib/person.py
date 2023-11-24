#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job = "Admin"):
        self.job = job
        self.name = name

    def get_name(self):
        print("Getting Name...")
        return self._name

    def set_name(self, name):
        print("setting name....")
        if 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name)

    def get_job(self):
        print("Retrieving Job...")
        return self._job

    def set_job(self, job):
        print("Setting job...")
        if job in APPROVED_JOBS:
            self._job = job
        else: 
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
