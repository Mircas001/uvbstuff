from silly.modules.webclient_nojs.view import views

views.update({
    "kiwi_list": {
        "type": "list",
        "model": "kiwi",
        "fields": [
            {
                "name": "ID",
                "field": "id",
            },
            {
                "name": "Active",
                "field": "active",
            },
            {
                "name": "Fallback",
                "field": "fallback",
            },
            {
                "name": "URL",
                "field": "url",
            },
            {
                "name": "Timeout",
                "field": "timeout",
            },
            {
                "name": "Timelimit",
                "field": "timelimit",
            },
            {
                "name": "Start Hour",
                "field": "hour_start",
            },
            {
                "name": "End hour",
                "field": "hour_end",
            },
            {
                "name": "Notes",
                "field": "notes",
            },
            {
                "name": "State: Last Update",
                "field": "state_last_update",
            },
            {
                "name": "State: Is Alive?",
                "field": "state_alive",
            },
            {
                "name": "State: Usage (0-100%)",
                "field": "state_usage",
            },
            {
                "name": "State: SNR",
                "field": "state_snr",
            },
        ],
        "pagination": {
            "default_page_size": 5,
        },
        "form_view_id": "kiwi_form",
    },
    "kiwi_form": {
        "type": "form",
        "model": "kiwi",
        "fields": [
            {
                "name": "Active",
                "field": "active",
                "type": "bool",
            },
            {
                "name": "Fallback",
                "field": "fallback",
                "type": "bool",
            },
            {
                "name": "URL",
                "field": "url",
                "type": "str",
            },
            {
                "name": "Timeout",
                "field": "timeout",
                "type": "int",
            },
            {
                "name": "Timelimit",
                "field": "timelimit",
                "type": "int",
            },
            {
                "name": "Start Hour",
                "field": "hour_start",
                "type": "int",
            },
            {
                "name": "End hour",
                "field": "hour_end",
                "type": "int",
            },
            {
                "name": "Notes",
                "field": "notes",
                "type": "str",
                "widget": {
                    "type": "textarea",
                },
            },
        ],
        "actions": [],
    },
    "kiwi_timeslot_list": {
        "type": "list",
        "model": "kiwi_timeslot",
        "fields": [
            {
                "name": "ID",
                "field": "id",
            },
            {
                "name": "Start Time",
                "field": "start",
            },
            {
                "name": "End Time",
                "field": "end",
            },
            {
                "name": "Related KiwiSDR ID",
                "field": "kiwi",
            },
        ],
        "pagination": {
            "default_page_size": 5,
        },
    },
    "kiwi_frequency_config": {
        "type": "form",
        "model": "kiwi_frequency",
        "fields": [
            {
                "name": "Station name",
                "field": "stationName",
                "type": "str"
            },
            {
                "name": "Modulation",
                "field": "stationModulation",
                "type": "str"
            },
            {
                "name": "Frequency does not change (0 or 1)",
                "field": "frequencyDoesNotChange",
                "type": "int"
            },
            {
                "name": "Frequency during the day",
                "field": "frequencyDay",
                "type": "float"
            },
            {
                "name": "Frequency at night",
                "field": "frequencyNight",
                "type": "float"
            },

            { "name": "Start time of day frequency (January)", "field": "startDayJan", "type": "int" },
            { "name": "Start time of night frequency (January)", "field": "startNightJan", "type": "int" },

            { "name": "Start time of day frequency (February)", "field": "startDayFeb", "type": "int" },
            { "name": "Start time of night frequency (February)", "field": "startNightFeb", "type": "int" },

            { "name": "Start time of day frequency (March)", "field": "startDayMar", "type": "int" },
            { "name": "Start time of night frequency (March)", "field": "startNightMar", "type": "int" },

            { "name": "Start time of day frequency (April)", "field": "startDayApr", "type": "int" },
            { "name": "Start time of night frequency (April)", "field": "startNightApr", "type": "int" },

            { "name": "Start time of day frequency (May)", "field": "startDayMay", "type": "int" },
            { "name": "Start time of night frequency (May)", "field": "startNightMay", "type": "int" },

            { "name": "Start time of day frequency (June)", "field": "startDayJun", "type": "int" },
            { "name": "Start time of night frequency (June)", "field": "startNightJun", "type": "int" },

            { "name": "Start time of day frequency (July)", "field": "startDayJul", "type": "int" },
            { "name": "Start time of night frequency (July)", "field": "startNightJul", "type": "int" },

            { "name": "Start time of day frequency (August)", "field": "startDayAug", "type": "int" },
            { "name": "Start time of night frequency (August)", "field": "startNightAug", "type": "int" },

            { "name": "Start time of day frequency (September)", "field": "startDaySep", "type": "int" },
            { "name": "Start time of night frequency (September)", "field": "startNightSep", "type": "int" },

            { "name": "Start time of day frequency (October)", "field": "startDayOct", "type": "int" },
            { "name": "Start time of night frequency (October)", "field": "startNightOct", "type": "int" },

            { "name": "Start time of day frequency (November)", "field": "startDayNov", "type": "int" },
            { "name": "Start time of night frequency (November)", "field": "startNightNov", "type": "int" },

            { "name": "Start time of day frequency (December)", "field": "startDayDec", "type": "int" },
            { "name": "Start time of night frequency (December)", "field": "startNightDec", "type": "int" }
        ],
        "actions": [],
    },

  "kiwi_frequency_list": {
        "type": "list",
        "model": "kiwi_frequency",
        "fields": [
            {
                "name": "Station name",
                "field": "stationName"
            },
            {
                "name": "Frequency does not change",
                "field": "frequencyDoesNotChange"
            },
            {
                "name": "Frequency during the day",
                "field": "frequencyDay"
            },
            {
                "name": "Frequency at night",
                "field": "frequencyNight"
            },

            { "name": "Start time of day frequency (January)", "field": "startDayJan", "type": "int" },
            { "name": "Start time of night frequency (January)", "field": "startNightJan", "type": "int" },

            { "name": "Start time of day frequency (February)", "field": "startDayFeb", "type": "int" },
            { "name": "Start time of night frequency (February)", "field": "startNightFeb", "type": "int" },

            { "name": "Start time of day frequency (March)", "field": "startDayMar", "type": "int" },
            { "name": "Start time of night frequency (March)", "field": "startNightMar", "type": "int" },

            { "name": "Start time of day frequency (April)", "field": "startDayApr", "type": "int" },
            { "name": "Start time of night frequency (April)", "field": "startNightApr", "type": "int" },

            { "name": "Start time of day frequency (May)", "field": "startDayMay", "type": "int" },
            { "name": "Start time of night frequency (May)", "field": "startNightMay", "type": "int" },

            { "name": "Start time of day frequency (June)", "field": "startDayJun", "type": "int" },
            { "name": "Start time of night frequency (June)", "field": "startNightJun", "type": "int" },

            { "name": "Start time of day frequency (July)", "field": "startDayJul", "type": "int" },
            { "name": "Start time of night frequency (July)", "field": "startNightJul", "type": "int" },

            { "name": "Start time of day frequency (August)", "field": "startDayAug", "type": "int" },
            { "name": "Start time of night frequency (August)", "field": "startNightAug", "type": "int" },

            { "name": "Start time of day frequency (September)", "field": "startDaySep", "type": "int" },
            { "name": "Start time of night frequency (September)", "field": "startNightSep", "type": "int" },

            { "name": "Start time of day frequency (October)", "field": "startDayOct", "type": "int" },
            { "name": "Start time of night frequency (October)", "field": "startNightOct", "type": "int" },

            { "name": "Start time of day frequency (November)", "field": "startDayNov", "type": "int" },
            { "name": "Start time of night frequency (November)", "field": "startNightNov", "type": "int" },

            { "name": "Start time of day frequency (December)", "field": "startDayDec", "type": "int" },
            { "name": "Start time of night frequency (December)", "field": "startNightDec", "type": "int" }
        ],
        "pagination": {
            "default_page_size": 5,
        },
        "form_view_id": "kiwi_frequency_config",
    },
    },
)


 

