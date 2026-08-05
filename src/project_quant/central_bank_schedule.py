from datetime import date


class CentralBankSchedule:
    def __init__(self, meeting_dates: list[date]):
        if not meeting_dates:
            raise ValueError("Meeting schedule cannot be empty.")

        self.meeting_dates = sorted(meeting_dates)
    def number_of_meetings(self, start_date: date, end_date: date) -> int:
        """
        Count the number of central bank meetings between two dates.

        Parameters
        ----------
        start_date : date
            The start date of the period.
        end_date : date
            The end date of the period.

        Returns
        -------
        int
            The number of central bank meetings between the two dates.
        """
        if start_date > end_date:
            raise ValueError("Start date must be before or equal to end date.")
        
        count = 0
        for meeting_date in self.meeting_dates:
            if start_date <= meeting_date <= end_date:
                count += 1
        return count
    def meetings_between(self, start_date: date, end_date: date) -> list[date]:
        """
        Get a list of central bank meeting dates between two dates.

        Parameters
        ----------
        start_date : date
            The start date of the period.
        end_date : date
            The end date of the period.

        Returns
        -------
        list[date]
            A list of central bank meeting dates between the two dates.
        """
        if start_date > end_date:
            raise ValueError("Start date must be before or equal to end date.")
        
        meetings = []
        for meeting_date in self.meeting_dates:
            if start_date <= meeting_date <= end_date:
                meetings.append(meeting_date)
        return meetings