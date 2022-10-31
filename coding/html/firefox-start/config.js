// ╔╗ ╔═╗╔╗╔╔╦╗╔═╗
// ╠╩╗║╣ ║║║ ║ ║ ║
// ╚═╝╚═╝╝╚╝ ╩ ╚═╝
// ┌─┐┌─┐┌┐┌┌─┐┬┌─┐┬ ┬┬─┐┌─┐┌┬┐┬┌─┐┌┐┌
// │  │ ││││├┤ ││ ┬│ │├┬┘├─┤ │ ││ ││││
// └─┘└─┘┘└┘└  ┴└─┘└─┘┴└─┴ ┴ ┴ ┴└─┘┘└┘

const CONFIG = {
    // ┌┐ ┌─┐┌─┐┬┌─┐┌─┐
    // ├┴┐├─┤└─┐││  └─┐
    // └─┘┴ ┴└─┘┴└─┘└─┘

    // General
    name: 'Nqtural',
    imageBackground: false,
    openInNewTab: true,
    twelveHourFormat: false,

    // Greetings
    greetingMorning: 'Good morning,',
    greetingAfternoon: 'Good afternoon,',
    greetingEvening: 'Good evening,',
    greetingNight: 'Good night,',

    // Layout
    bentoLayout: 'bento', // 'bento', 'lists', 'buttons'

    // Weather
    weatherKey: '4699e17c4d6b50d0f84272714dcdaba2', // Write here your API Key
    weatherUnit: 'C', // 'F', 'C'
    language: 'en', // More languages in https://openweathermap.org/current#multi

    trackLocation: false, // If false or an error occurs, the app will use the lat/lon below
    defaultLatitude: '58.1603741',
    defaultLongitude: '11.692778',

    // ┌┐ ┬ ┬┌┬┐┌┬┐┌─┐┌┐┌┌─┐
    // ├┴┐│ │ │  │ │ ││││└─┐
    // └─┘└─┘ ┴  ┴ └─┘┘└┘└─┘

    buttonsContainer: [
        {
            id: '1',
            name: 'Github',
            icon: 'github',
            link: 'https://github.com/nqtural',
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
