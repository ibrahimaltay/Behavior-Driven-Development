Feature: Reservation Page

    Scenario: Owner tries to cancel valid reservation

        Given the user is owner
        And the user is not admin
        And the reservation is valid
        When the user tries to cancel the reservation
        Then the system allows

    Scenario: Admin tries to cancel valid reservation

        Given the user is admin
        And the user is not owner
        And the reservation is valid
        When the user tries to cancel the reservation
        Then the system allows

    Scenario: Owner tries to cancel invalid reservation

        Given the user is owner
        And the user is not admin
        And the reservation is invalid
        When the user tries to cancel the reservation
        Then the system does not allow

    Scenario: Admin tries to cancel invalid reservation

        Given the user is admin
        And the user is not owner
        And the reservation is invalid
        When the user tries to cancel the reservation
        Then the system does not allow

    Scenario: Not owner tries to cancel valid reservation

        Given the user is not owner
        And the user is not admin
        And the reservation is valid
        When the user tries to cancel the reservation
        Then the system does not allow
