// ╔╗ ╔═╗╔╗╔╔╦╗╔═╗
// ╠╩╗║╣ ║║║ ║ ║ ║
// ╚═╝╚═╝╝╚╝ ╩ ╚═╝
// ┌─┐┌─┐┌┐┌┌─┐┬┌─┐┬ ┬┬─┐┌─┐┌┬┐┬┌─┐┌┐┌
// │  │ ││││├┤ ││ ┬│ │├┬┘├─┤ │ ││ ││││
// └─┘└─┘┘└┘└  ┴└─┘└─┘┴└─┴ ┴ ┴ ┴└─┘┘└┘

// =============================================================================================
// ========================================= IMPORTANT =========================================
// =============================================================================================
// Enter your information below and configure as you like, then rename this file to 'config.js'

const CONFIG = {
    // ┌┐ ┌─┐┌─┐┬┌─┐┌─┐
    // ├┴┐├─┤└─┐││  └─┐
    // └─┘┴ ┴└─┘┴└─┘└─┘

    // General
    name: 'YourName',
    imageBackground: false,
    openInNewTab: true,
    twelveHourFormat: false,
    iconColor: 'gruvbox', // Available: gruvbox dracula catppuccin-mocha

    // Greetings
    greetingMorning: 'Good morning,',
    greetingAfternoon: 'Good afternoon,',
    greetingEvening: 'Good evening,',
    greetingNight: 'Good night,',

    // Weather
    weatherKey: 'apikey', // Write your API key here (Get it from https://openweathermap.org/)
    weatherUnit: 'C', // 'F', 'C'
    language: 'en', // More languages in https://openweathermap.org/current#multi

    trackLocation: true, // If false or an error occurs, the app will use the lat/lon below
    defaultLatitude: '0',
    defaultLongitude: '0',

    // ┌┐ ┬ ┬┌┬┐┌┬┐┌─┐┌┐┌┌─┐
    // ├┴┐│ │ │  │ │ ││││└─┐
    // └─┘└─┘ ┴  ┴ └─┘┘└┘└─┘

    buttonsContainer: [
        {
            id: '1',
            name: 'Github',
            icon: 'github',
            link: 'https://github.com/',
        },
        {
            id: '2',
            name: 'Mail',
            icon: 'mail',
            link: 'https://outlook.live.com/mail/0/',
        },
        {
            id: '5',
            name: 'Odysee',
            icon: 'youtube',
            link: 'https://odysee.com/',
        },
        {
            id: '3',
            name: 'r/Unixporn',
            icon: 'terminal',
            link: 'https://reddit.com/r/unixporn',
        },
        {
            id: '4',
            name: 'Mediafire',
            icon: 'file-up',
            link: 'https://app.mediafire.com/myfiles',
        },
        {
            id: '6',
            name: 'Arch Linux Wiki',
            icon: 'book',
            link: 'https://wiki.archlinux.org/',
        },
    ],

    // ┬  ┬┌─┐┌┬┐┌─┐
    // │  │└─┐ │ └─┐
    // ┴─┘┴└─┘ ┴ └─┘

    // Lists Container
    listsContainer: [
        {
            icon: 'palette',
            id: '1',
            links: [
                {
                    name: 'Dracula',
                    link: 'https://github.com/dracula/dracula-theme',
                },
                {
                    name: 'Gruvbox',
                    link: 'https://github.com/morhetz/gruvbox',
                },
                {
                    name: 'Catppuccin',
                    link: 'https://github.com/catppuccin/catppuccin',
                },
                {
                    name: 'Solarized',
                    link: 'https://github.com/altercation/solarized',
                },
            ],
        },
        {
            icon: 'coffee',
            id: '2',
            links: [
                {
                    name: 'Linkedin',
                    link: 'https://www.linkedin.com',
                },
                {
                    name: 'Dribbble',
                    link: 'https://www.dribbble.com',
                },
                {
                    name: 'Trello',
                    link: 'https://www.trello.com',
                },
                {
                    name: 'Slack',
                    link: 'https://www.slack.com',
                },
            ],
        },
    ],
};
