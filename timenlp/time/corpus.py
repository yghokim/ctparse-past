corpus = [
    # ruleYear
    ("Time[]{2019-X-X X:X (X/X)}", "2018-03-07T12:43", ["2019"]),
    # ruleToday
    (
        "Time[]{2018-03-07 X:X (X/X)}",
        "2018-03-07T12:43",
        ["today"],
    ),
    # ruleNow
    (
        "Time[]{2018-03-07 12:43 (X/X)}",
        "2018-03-07T12:43",
        ["rightnow", "just now"],
    ),
    # ruleTomorrow
    ("Time[]{2019-01-01 X:X (X/X)}", "2018-12-31T12:43", ["tomorrow"]),
    # ruleTomorrow + time
    (
        "Time[]{2019-01-01 19:25 (X/X)}",
        "2018-12-31T12:43",
        ["tomorrow 7.25 pm"],
    ),
    # ruleYesterday
    # test on a leap-year
    ("Time[]{2020-02-29 X:X (X/X)}", "2020-03-01T12:43", ["yesterday"]),
    # ruleBeforeYesterday
    # ruleEOM
    (
        "Time[]{2018-03-31 X:X (X/X)}",
        "2018-03-07T12:43",
        ["end of the month"],
    ),
    # ruleEOY
    (
        "Time[]{2018-12-31 X:X (X/X)}",
        "2018-03-07T12:43",
        ["end of the year"],
    ),
    # ruleNamedDOW
    ("Time[]{2018-03-12 X:X (X/X)}", "2018-03-07T12:43", ["monday"]),
    (
        "Time[]{2018-03-13 X:X (X/X)}",
        "2018-03-07T12:43",
        ["tuesday"],
    ),
    (
        "Time[]{2018-03-11 X:X (X/night)}",
        "2018-03-07T12:43",
        ["sunday night"],
    ),
    # ruleNamedMonth
    ("Time[]{X-01-X X:X (X/X)}", "2018-03-07T12:43", ["Januar", "Jan."]),
    ("Time[]{X-04-X X:X (X/X)}", "2018-03-07T12:43", ["April", "apr."]),
    ("Time[]{X-07-X X:X (X/X)}", "2018-03-07T12:43", ["Juli", "July", "Jul."]),
    (
        "Time[]{X-12-X X:X (X/X)}",
        "2018-03-07T12:43",
        ["December", "Dec."],
    ),
    # ruleAtDOW
    ("Time[]{2018-03-13 X:X (X/X)}", "2018-03-07T12:43", ["on Tuesday"]),
    (
        "Time[]{2018-03-14 X:X (X/X)}",
        "2018-03-07T12:43",
        ["this Wednesday"],
    ),
    # ruleNextDOW
    (
        "Time[]{2018-03-16 X:X (X/X)}",
        "2018-03-07T12:43",
        [
            "next Friday",
            "Friday next week",
            "on the following Friday",
        ],
    ),
    # ruleDOYYear, ruleDDMM, ruleDDMMYYYY
    (
        "Time[]{2017-05-08 X:X (X/X)}",
        "2018-03-07T12:43",
        [
            "8th May",
            "8th of May",
            "May 8th",
            "at 8th May",
            "on 8th of May",
            "this May 8th",
            "may 8",
        ],
    ),
    # ruleDOWDOM
    (
        "Time[]{2018-05-08 X:X (X/X)}",
        "2018-03-07T12:43",
        ["Tuesday 8th", "Tuesday the 8th", "Dienstag der 8."],
    ),
    (
        "Time[]{2018-06-02 X:X (X/X)}",
        "2018-03-07T12:43",
        ["Saturday 2nd", "Jun 2nd", "am 2ten Juni"],
    ),
    # ruleDOWDate, ruleDateDOW
    (
        "Time[]{2018-05-08 X:X (X/X)}",
        "2018-03-07T12:43",
        ["Tuesday, 8.5.", "8.5. Tuesday"],
    ),
    # rulePOD, ruleLatentPOD
    (
        "Time[]{2018-03-08 X:X (X/morning)}",
        "2018-03-07T12:43",
        ["early", "morning"],
    ),
    (
        "Time[]{2018-03-08 X:X (X/earlymorning)}",
        "2018-03-07T12:43",
        ["early morning"],
    ),
    (
        "Time[]{2018-03-08 X:X (X/forenoon)}",
        "2018-03-07T12:43",
        ["forenoon"],
    ),
    # before noon case
    (
        "Interval[]{None - 2018-03-08 X:X (X/noon)}",
        "2018-03-07T12:43",
        ["before noon"],
    ),
    (
        "Time[]{2018-03-08 X:X (X/afternoon)}",
        "2018-03-07T12:43",
        ["afternoon"],
    ),
    # past noon case
    (
        "Interval[]{2018-03-08 X:X (X/noon) - None}",
        "2018-03-07T12:43",
        ["after noon"],
    ),
    ("Time[]{2018-03-08 X:X (X/noon)}", "2018-03-07T12:43", ["mittags", "noon"]),
    (
        "Time[]{2018-03-07 X:X (X/evening)}",
        "2018-03-07T12:43",
        ["late"],
    ),
    (
        "Time[]{2018-03-07 X:X (X/lateevening)}",
        "2018-03-07T12:43",
        ["very late", "late evening"],
    ),
    (
        "Time[]{2018-03-08 X:X (X/veryearlyafternoon)}",
        "2018-03-07T12:43",
        ["very early afternoon"],
    ),
    (
        "Time[]{2018-03-07 X:X (X/night)}",
        "2018-03-07T12:43",
        ["this night"],
    ),
    # First/Last
    (
        "Time[]{2018-03-08 X:X (X/first)}",
        "2018-03-07T12:43",
        [
            "tomorrow first",
            "tomorrow earliest possible",
        ],
    ),
    (
        "Time[]{2018-03-08 X:X (X/last)}",
        "2018-03-07T12:43",
        [
            "tomorrow last",
            "tomorrow as late as possible",
        ],
    ),
    (
        "Time[]{2018-03-09 X:X (X/first)}",
        "2018-03-07T12:43",
        ["Friday first"],
    ),
    (
        "Time[]{2018-03-13 X:X (X/last)}",
        "2018-03-07T12:43",
        ["Tuesday last"],
    ),
    # Date + POD
    (
        "Time[]{2017-01-25 X:X (X/evening)}",
        "2018-03-07T12:43",
        [
            "25.01.2017 abends",
            "evening of January 25th 2017",
            "25.01.2017 late",
            "25.01.2017 spät",
            "25.01.2017 (spät)",
        ],
    ),
    (
        "Time[]{2017-01-25 X:X (X/lateafternoon)}",
        "2018-03-07T12:43",
        [
            "25.01.2017 spät nachmittags",
            "am 25. Januar 2017 am späten Nachmittag",
            "am 25. Januar 2017 am späten Nachmittag",
            "am 25. Januar 2017 am späten Nachmittag",
            "late afternoon of January 25th 2017",
        ],
    ),
    (
        "Time[]{2020-01-25 X:X (X/evening)}",
        "2018-03-07T12:43",
        [
            "25.01.2020 abends",
            "25.01.2020 late",
            "25.01.2020 spät",
            "25. Januar 2020 abends",
            "abends 25.01.2020",
            "evening of January 25th 2020",
        ],
    ),
    (
        "Time[]{2018-03-25 X:X (X/evening)}",
        "2018-03-07T12:43",
        ["evening of the 25th", "am 25. abends", "abends am 25."],
    ),
    # ruleTODPOD
    (
        "Time[]{X-X-X 08:00 (X/X)}",  # next day since moning is already over
        "2018-03-07T12:43",
        ["at 8 late morning", "at 8 very late morning"],
    ),
    (
        "Time[]{X-X-X 16:30 (X/X)}",
        "2018-03-07T12:43",
        ["um 4:30 nachmittags", "at 4:30 in the afternoon"],
    ),
    # rulePODTOD
    (
        "Time[]{X-X-X 08:00 (X/X)}",  # next day since moning is already over
        "2018-03-07T12:43",
        ["late morning at 8"],
    ),
    (
        "Time[]{X-X-X 16:30 (X/X)}",
        "2018-03-07T12:43",
        ["afternoon at 16:30", "afternoon at around 16:30"],
    ),
    # ruleDateTOD
    (
        "Time[]{2018-08-05 08:00 (X/X)}",
        "2018-03-07T12:43",
        [
            "5. August um 8",
            "August 5th at 8",
            "august 5 at 8am",
            "5. Aug gegen 8",
            "05.08.2018 8Uhr",
            "05.08.2018 (8 Uhr)",
        ],
    ),
    # ruleTODDate
    (
        "Time[]{2018-08-05 08:00 (X/X)}",
        "2018-03-07T12:43",
        ["um 8 am 5. August", "at 8 on August 5th"],
    ),
    # ruleDateDate, ruleDOMDate, ruleDateDOM
    (
        "Interval[]{2018-08-05 X:X (X/X) - 2018-08-16 X:X (X/X)}",
        "2018-03-07T12:43",
        [
            "5.8. - 16.8.",
            "August 5th - August 16th",
            "Aug 5 - 16",
            "from Aug 5 to 16",
            "5 to 16 Aug",
            "from 5 to 16 Aug",
            "5. - 16.8.",
            "5.8. - 16.8.2018",
            "5.8. bis 16.8.2018",
            "5.8. - 16.8.",
            "5.8. bis 16.8.",
            "5. - 16.8.",
            "5.8. - 16.8.2018",
            "5.8. bis 16.8.2018",
            "5.8. - 16.8.",
            "5.8. bis 16.8.",
            "5. bis zum 16.8.",
            "vom 05.08.2018 zum 16.08.2018",
        ],
    ),
    # ruleDOYDate
    (
        "Interval[]{2017-08-05 X:X (X/X) - 2017-08-16 X:X (X/X)}",
        "2018-03-07T12:43",
        ["5.8. - 16.8.2017", "Samstag 5.8. - Mittwoch 16.8.2017"],
    ),
    # ruleDateTimeDateTime
    (
        "Interval[]{2018-08-05 08:00 (X/X) - 2018-08-16 13:00 (X/X)}",
        "2018-03-07T12:43",
        ["5.8. 8Uhr - 16.8. 13Uhr", "August 5th 8h - August 16th 13h"],
    ),
    (
        "Interval[]{X-X-X 08:00 (X/X) - X-X-X 13:00 (X/X)}",
        "2018-03-07T12:43",
        ["08:00 - 13:00", "8Uhr - 13Uhr", "8h to 13h"],
    ),
    # rulePODPOD
    (
        "Interval[]{X-X-X X:X (X/evening) - X-X-X X:X (X/night)}",
        "2018-05-08T10:32",
        ["evening/night"],
    ),
    # ruleAfterTime
    (
        "Interval[]{2017-11-26 08:00 (X/X) - None}",
        "2018-03-07T12:43",
        ["26.11.2017 ab 08:00 Uhr"],
    ),
    (
        "Interval[]{2018-11-26 08:00 (X/X) - None}",
        "2018-03-07T12:43",
        [
            "26.11.2018 ab 08:00 Uhr",
            "26.11. ab 08:00 Uhr",
            "26.11. frühestens um 08:00 Uhr",
            "November 26th earliest 08:00 Uhr",
            "November 26th earliest after 08:00 Uhr",
            "November 26th from earliest 08:00 Uhr",
            "26.11. nicht vor 08:00 Uhr",
        ],
    ),
    # ruleBeforeTime
    (
        "Interval[]{None - 2017-11-26 08:00 (X/X)}",
        "2018-03-07T12:43",
        [
            "26.11.2017 vor 08:00 Uhr",
            "26.11.2017 bis spätestens 08:00 Uhr",
            "26.11.2017 spätestens bis 08:00 Uhr",
        ],
    ),
    (
        "Interval[]{None - 2018-11-26 08:00 (X/X)}",
        "2018-03-07T12:43",
        ["26.11.2018 vor 08:00 Uhr", "26.11. vor 08:00 Uhr", "26.11. not after 08:00"],
    ),
    # ruleHHMM
    (
        "Time[]{X-X-X 08:00 (X/X)}",
        "2018-03-07T00:00",
        ["8h", "8 Uhr", "8:00", "8h00", "8am"],
    ),
    (
        "Time[]{X-X-X 20:00 (X/X)}",
        "2018-03-07T00:00",
        ["20h", "20 Uhr", "20:00", "20pm", "20am"],
    ),  # <-- ignore am, since this makes no sense
    # ruleMonthDOM
    (
        "Time[]{2018-04-07 X:X (X/X)}",
        "2018-03-07T00:00",
        ["april 7", "april 7th", "7. April"],
    ),
    # ruleAbsorbOnTime
    (
        "Time[]{X-X-X 20:00 (X/X)}",
        "2018-03-07T00:00",
        ["at 8pm", "um 20h", "gegen 20:00", "about 8pm", "at around 8pm"],
    ),
    # ruleAbsorbOnTime + X
    (
        "Time[]{2018-06-21 08:00 (X/X)}",
        "2018-03-07T00:00",
        [
            "Jun 21 at 8am",
            "Jun 21 about 8am",
            "Jun 21 at about 8am",
            "Jun 21 on 8am",
            "21. Juni um 8",
        ],
    ),
    # ruleDateInterval
    (
        "Interval[]{2018-11-13 13:30 (X/X) - 2018-11-13 15:35 (X/X)}",
        "2018-03-07T00:00",
        [
            "Mon, Nov 13 1:30 PM - 3:35 PM",
            "Montag, 13. November von 13:30 bis 15:35",
            "Nov 13 13:30 - 15:35",
        ],
    ),
    (
        "Interval[]{2018-11-13 13:30 (X/X) - None}",
        "2018-03-07T00:00",
        [
            "Mon, Nov 13 after 1:30 PM",
            "Montag, 13. November nach 13:30",
            "Montag, 13. November 2018 nach 13:30",
            "13.11. ab 13:30",
        ],
    ),
    (
        "Interval[]{2016-11-13 13:30 (X/X) - None}",
        "2018-03-07T00:00",
        [
            "Mon, Nov 13 2016 after 1:30 PM",
            "Montag, 13. November 2016 nach 13:30",
            "Montag, 13. November 2016 nach 13:30",
            "13.11.16 ab 13:30",
        ],
    ),
    (
        "Interval[]{2018-03-11 X:X (X/noon) - None}",
        "2018-03-07T00:00",
        ["Sunday after noon", "Sonntag ab Mittag", "Sonntag, 11. März 2018 ab Mittag"],
    ),
    (
        "Interval[]{2018-03-11 09:00 (X/X) - None}",
        "2018-03-07T00:00",
        [
            "Sunday Mar 11 after 9",
            "Sonntag, 11. März 2018 nach 9",
            "Sonntag, der 11. Mrz. nach 9",
        ],
    ),
    (
        "Interval[]{2016-03-11 09:00 (X/X) - None}",
        "2018-03-07T00:00",
        [
            "Sunday Mar 11 2016 after 9",
            "Sonntag, 11. März 2016 nach 9",
            "Sonntag, der 11. Mrz 2016 nach 9",
        ],
    ),
    # ruleDateInterval - day wrap
    (
        "Interval[]{2018-11-13 23:30 (X/X) - 2018-11-14 03:35 (X/X)}",
        "2018-03-07T00:00",
        ["Mon, Nov 13 11:30 PM - 3:35 AM", "Nov 13 23:30 - 3:35"],
    ),
    # ruleAbsorbDOWComma -- deleted, comma should be removed by caller
    (
        "Time[]{2018-07-27 X:X (X/X)}",
        "2018-07-26T00:00",
        ["Freitag, dem 27.", "Freitag, 27ter", "Fri, the 27th"],
    ),
    # ruleNamedHour
    ("Time[]{X-X-X 09:00 (X/X)}", "2018-07-26T00:00", ["neun", "nine"]),
    # ruleQuarterBeforeHH
    (
        "Time[]{X-X-X 07:45 (X/X)}",
        "2018-07-26T00:00",
        ["viertel vor acht", "viertel vor 8", "quarter to eight"],
    ),
    # ruleQuarterBeforeHH midnight wrap
    ("Time[]{X-X-X 23:45 (X/X)}", "2018-07-26T00:00", ["viertel vor 0"]),
    # ruleQuarterAfterHH
    (
        "Time[]{X-X-X 08:15 (X/X)}",
        "2018-07-26T00:00",
        ["viertel nach acht", "viertel nach 8", "quarter past eight"],
    ),
    # ruleHalfBeforeHH
    (
        "Time[]{X-X-X 07:30 (X/X)}",
        "2018-07-26T00:00",
        ["halb acht", "halb 8", "half eight"],
    ),
    # ruleHalfBeforeHH not when minutes are present
    ("Time[]{X-X-X 07:35 (X/X)}", "2018-07-26T00:00", ["halb 7:35"]),
    # ruleHalfBeforeHH midnight wrap
    ("Time[]{X-X-X 23:30 (X/X)}", "2018-07-26T00:00", ["halb mitternacht"]),
    # ruleHalfAfterHH
    (
        "Time[]{X-X-X 08:30 (X/X)}",
        "2018-07-26T00:00",
        ["halb nach acht", "halfe past eight"],
    ),
    # ruleHalfAfterHH not when minutes are present
    ("Time[]{X-X-X 08:32 (X/X)}", "2018-07-26T00:00", ["halb nach 8:32"]),
    # rulePODInterval
    (
        "Interval[]{None - 2018-09-17 22:00 (X/X)}",
        "2018-07-26T00:00",
        ["am 17.9. abends vor 10", "at Sep 17th in the evening before 10"],
    ),
    (
        "Interval[]{X-X-X 22:00 (X/X) - None}",
        "2018-07-26T00:00",
        ["abends nach 10", "in the evening after 10", "in the evening after 22h"],
    ),
    (
        "Interval[]{X-X-X 20:00 (X/X) - X-X-X 21:00 (X/X)}",
        "2018-07-26T00:00",
        ["in the evening between 8 and 9", "Jul 26th between 20 and 21"],
    ),
    (
        "Interval[]{X-X-X 08:00 (X/X) - X-X-X 09:00 (X/X)}",
        "2018-07-26T00:00",
        ["in the morning between 8 and 9", "Jul 26th between 8 and 9"],
    ),
    # rule
    #
    # -----------------------------------------------------------------------------
    # OLD CORPUS
    # -----------------------------------------------------------------------------
    #
    (
        "Interval[]{2017-12-19 09:30 (X/X) - 2017-12-19 10:45 (X/X)}",
        "2017-12-18T12:34",
        [
            "tomorrow 09:30 - 10:45",
            "tomorrow 0930 - 1045",
            "19. Dezember von 09:30 bis 10:45",
            "19th of December from 09:30 til 10:45",
            "19.12. 09:30 - 10:45",
            "19.12.17 09:30 - 10:45",
            "19.12.2017 09:30 - 19.12.2017 10:45",
            "19.12.2017 09:30 - 10:45",
            "19 dec 0930-1045",
            "Dec 19th between 9.30 and 10.45",
        ],
    ),
    (
        "Interval[]{2018-02-16 X:X (X/X) - 2018-02-21 X:X (X/X)}",
        "2017-12-18T12:34",
        ["16.02.2018 - 21.02.2018", "16. bis 21.02.2018"],
    ),
    (
        "Interval[]{2018-08-07 X:X (X/X) - 2018-08-10 X:X (X/X)}",
        "2017-12-18T12:34",
        ["07.-10.08.2018"],
    ),
    # ('Range[]{2018-12-09 - 2018-12-13}',
    #  '2017-12-18T12:34',
    #  [
    #      '09.-13.12.2018 von Samstag bis Donnerstag'
    #  ]),
    # ('Range[]{2018-04-27 - 2018-04-30}',
    #  '2017-12-18T12:34',
    #  [
    #      # 'from the 27th to the 30th of April 2018',
    #      '27.-30.04.2018 von Freitag bis Montag'
    #  ]),
    (
        "Time[]{2018-01-13 X:X (X/X)}",
        "2017-12-18T12:34",
        ["am 13.1.", "am 13.01.", "am 13. Januar", "13.01", "13.1", "13th Jan"],
    ),
    (
        "Time[]{2017-12-19 X:X (X/X)}",
        "2017-12-18T12:34",
        [
            "am Dienstag",
            "am 19.12",
            "Dienstag 19.12",
            "Tuesday 19th of December",
            "Tuesday December 19th",
            "Dienstag 19. Dezember",
            "Dienstag Dezember 19.",
            "Dienstag",
        ],
    ),
    (
        "Time[]{2018-03-01 14:30 (X/X)}",
        "2017-12-18T12:34",
        [
            # mm/dd does not work yet
            # '03/01/2018 at 2:30 pm',
            "am 01.03.2018 um 14:30",
            "Mar. 1st 2:30 pm",
            "1. März um 1430 Uhr",
            "01.03.2018 14:30",
        ],
    ),
    (
        "Time[]{2018-01-03 14:30 (X/X)}",
        "2017-12-18T12:34",
        [
            # mm/dd does not work yet
            # '01/03/2018 at 2:30 pm',
            "am 03.01.2018 um 14:30",
            "Jan. 3rd 2:30 pm",
            "3. Januar 1430 Uhr",
            "03.01.2018 14:30",
            "3. Jan. 2018 14:30",
        ],
    ),
    ("Time[]{2018-04-23 11:00 (X/X)}", "2017-12-18T12:34", ["23.04.2018 11:00"]),
    ("Time[]{2018-11-19 18:00 (X/X)}", "2017-12-18T12:34", ["19.11.2018 18:00"]),
    (
        "Time[]{2017-12-20 X:X (X/morning)}",
        "2017-12-18T12:34",
        ["Wednesday, 20th December morning", "december 20 morning"],
    ),
    (
        "Time[]{2018-12-06 X:X (X/morning)}",
        "2018-03-07T12:43",
        [
            "december 6 early",
            "december 6th morning",
        ],
    ),
    (
        "Time[]{2018-12-06 X:X (X/earlymorning)}",
        "2018-03-07T12:43",
        ["december 6 early morning"],
    ),
    (
        "Time[]{2018-12-06 X:X (X/forenoon)}",
        "2018-03-07T12:43",
        ["december 6th forenoon"],
    ),
    (
        "Time[]{2018-12-06 X:X (X/afternoon)}",
        "2018-03-07T12:43",
        ["december 6 afternoon"],
    ),
    (
        "Time[]{2018-12-06 X:X (X/noon)}",
        "2018-03-07T12:43",
        ["december 6 noon"],
    ),
    (
        "Time[]{2018-12-06 X:X (X/evening)}",
        "2018-03-07T12:43",
        ["december 6 late"],
    ),
    (
        "Time[]{2018-12-06 X:X (X/lateevening)}",
        "2018-03-07T12:43",
        ["december 6 late evening"],
    ),
    (
        "Time[]{2018-12-06 X:X (X/veryearlyafternoon)}",
        "2018-03-07T12:43",
        ["december 6 very early afternoon"],
    ),
    # ('DateTime[]{2017-12-20Tmorning}',
    #  '2017-12-18T12:34',
    #  ['Wednesday, morning, 20.12.17']),
    # ('DateTime[]{2017-12-20Tafternoon}',
    #  '2017-12-18T12:34',
    #  ['Wednesday, afternoon, 20.12.17']),
    # ('DateTime[]{2017-12-20 XX:XX (X/evening)}',
    #  '2017-12-18T12:34',
    #  ['Wednesday, evening, 20.12.17']),
    (
        "Interval[]{2018-06-21 11:00 (X/X) - 2018-06-21 13:00 (X/X)}",
        "2017-12-18T12:34",
        ["Jun 21st between 11am and 1pm"],
    ),
    # Military time tests
    ("Time[]{2020-02-03 X:X (X/X)}", "2020-02-25T12:34", ["3 Feb 2020"]),
    # Duration tests
    (
        "Duration[]{1 nights}",
        "2020-02-25T12:34",
        ["one night", "1 night"],
    ),
    ("Duration[]{30 days}", "2020-02-25T12:34", ["30 days"],),
    ("Duration[]{7 weeks}", "2020-02-25T12:34", ["7 weeks"],),
    (
        "Duration[]{20 minutes}",
        "2020-02-25T12:34",
        ["20 minutes", "twenty minutes"],
    ),
    ("Duration[]{1 months}", "2020-02-25T12:34", ["1 month", "one month"]),
    (
        "Duration[]{30 minutes}",
        "2020-02-25T12:34",
        ["half an hour", "half hour", "1/2 hour", "1/2h", "1/2 h", "0.5 hour"],
    ),
    # ruleTimeDuration
    (
        "Interval[]{2020-02-27 X:X (X/X) - 2020-02-28 X:X (X/X)}",
        "2020-02-25T12:34",
        ["on the 27th for one day", "on the 27th for one night"],
    ),
    (
        "Interval[]{2020-02-25 15:00 (X/X) - 2020-02-25 16:00 (X/X)}",
        "2020-02-25T12:34",
        ["today 15:00 for one hour"],
    ), 
    ( #added by Young-Ho
        "Interval[]{2022-03-03 11:05 (X/X) - 2022-03-03 14:05 (X/X)}",
        "2022-03-03T14:05",
        ["for 3 hours", "for 3 hours until now", "for 3 hours so far", "for about 3 hours so far"]
    ),
    ( #added by Young-Ho
        "Interval[]{X-X-X 11:00 (X/X) - X-X-X 12:00 (X/X)}",
        "2022-03-03T13:30",
        ["from 11 a.m. for an hour", "since 11 a.m. for 1 hour", "from eleven for 1 hour", "from eleven for an hour", "since eleven for about an hour"]
    ),
    ( #added by Young-Ho
        "Interval[]{2022-03-03 11:00 (X/X) - 2022-03-03 12:00 (X/X)}",
        "2022-03-04T12:30",
        ["from 11 a.m. yesterday for an hour", "from 11 a.m. yesterday for 1 hour", "from eleven yesterday for one hour"]
    ),
    ( #added by Young-Ho
        "Interval[]{X-X-X 13:00 (X/X) - X-X-X 16:00 (X/X)}",
        "2022-03-03T18:30",
        ["since 1 pm for 3 hours", "since 1 pm for about 3 hours"]
    ),


    ( #added by Young-Ho
        "Interval[]{X-X-X 11:30 (X/X) - X-X-X 12:15 (X/X)}",
        "2022-03-03T18:30",
        ["since 11:30 for 45 minutes"]
    ),


    ( #added by Young-Ho
        "Interval[]{2022-03-03 18:20 (X/X) - 2022-03-03 19:05 (X/X)}",
        "2022-03-03T18:30",
        ["since 10 minutes ago for approximately 45 minutes"]
    ),

    #Compound duration
    ( #added by Young-Ho
        "Duration[]{36 hours}",
        "2022-03-03T18:30",
        ["1 and a half days", "1.5 days", "one and 0.5 days", "one and a half days"]
    ),

    ( #added by Young-Ho
        "Duration[]{45 minutes}",
        "2022-03-03T18:30",
        ["3 quarters of an hour", "three quarter an hour", "3/4 of an hour"]
    ),


    ( #added by Young-Ho
        "Duration[]{195 minutes}",
        "2022-03-03T18:30",
        ["3 and 1/4 of an hour"]
    ),


    ( #added by Young-Ho
        "Duration[]{15 minutes}",
        "2022-03-03T18:30",
        ["quarter hour", "a quarter of an hour"]
    ),

    ( #added by Young-Ho
        "Duration[]{90 minutes}",
        "2022-03-03T18:30",
        ["1 and a half hours", "1.5 hours", "one and 0.5 hours", "one and a half hours", "an hour and a half", "one hour and a half"]
    ),

    ( #added by Young-Ho
        "Duration[]{90 minutes}",
        "2022-03-03T18:30",
        ["1 hour and 30 minutes", "an hour and 30 minutes", "an hour and thirty minutes"]
    ),

    ( #added by Young-Ho
        "Duration[]{30 minutes}",
        "2022-03-03T18:30",
        ["thirty minutes"]
    ),
    
    # ruleDurationInterval, ruleIntervalDuration
    (
        "Interval[]{2020-11-15 X:X (X/X) - 2020-11-18 X:X (X/X)}",
        "2020-02-25T12:34",
        ["3 days 15-18 Nov", "15-18 Nov 3 Nächte", "15-18 Nov für 3 Nächte"],
    ),
]