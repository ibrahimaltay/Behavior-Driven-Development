from behave import *
from reservation import *

@Given('the user is owner')
def step(context):
    context.user = User()
    context.reservation = Reservation(context.user)

@Given('the user is not owner')
def step(context):
    context.user = User()
    context.actual_owner = User()
    context.reservation = Reservation(context.actual_owner)

@Given('the user is not admin')
def step(context):
    context.user = User(False)

@Given('the user is admin')
def step(context):
    context.user = User(True)

@Given('the reservation is valid')
def step(context):
    context.reservation.valid = True

@Given('the reservation is invalid')
def step(context):
    context.reservation.valid = False

@When('the user tries to cancel the reservation')
def step(context):
    try:
        context.reservation.cancel(context.user)
    except Exception as e:
        context.exception = e

@Then('the system allows')
def step(context):
    assert context.failed is False

@Then('the system does not allow')
def step(context):
    assert context.exception is not None