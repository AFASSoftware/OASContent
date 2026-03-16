Preferably use this endpoint to modify leave bookings. You can find the AbsenceId via a GetConnector.
When making a PUT request, **only include the field `Id`** and **the fields you want to update**. The precise behavior of the connector depends on the type of schedule the employee has.

### Shortening or Extending Leave

#### Schedule type: working hours

With this type of schedule, the employee works according to a fixed schedule with a start and end time. For a leave booking, both start and end times are filled in.

- `Id`: This is the AbsenceId
- `LeDt`: False if the leave consists of full days only.
- `DaBe`: Start date/time. The time portion is ignored if `LeDt` = False.
- `DaEn`: End date/time. The time portion is ignored if `LeDt` = False.

#### Schedule type: hours per day

With this type of schedule, it is known which days are worked, but not when the hours are worked. In the leave booking, both start and end times are always set to 00:00:00.

- `Id`: This is the AbsenceId
- `LeDt`: False if the leave consists of full days only.
- `DaBe`: Start date/time. The time portion is ignored.
- `DaEn`: End date/time. The time portion is ignored.
- `DuBe`: Leave (in **minutes**) on the start date. This field is ignored if `LeDt` = False.
- `DuEn`: Leave (in **minutes**) on the end date. This field is ignored if `LeDt` = False.

#### Schedule type: hours per week

With this type of schedule, it is not known which days are worked, and it is also not known when the hours are worked. You must specify exactly how much leave is taken. In the leave booking, both start and end times are always set to 00:00:00.

- `Id`: This is the AbsenceId
- `LeDt`: False if the leave consists of full days only.
- `DaBe`: Start date/time. The time portion is ignored.
- `DaEn`: End date/time. The time portion is ignored.
- `DuRa`: Leave duration (in **minutes**). This field is ignored if `LeDt` = False.

### Known issue: shortening or extending leave where `LeDt` = False

If you want to modify leave that only consists of full days, `LeDt` will be set to False.
If you want to shorten such leave by a few hours, for example, you need to make two requests.

1. In the first request, set `LeDt` to True.
2. In the second request, specify the changed `DaBe`, `DaEn`, `DuBe`, or `DuEn`.

