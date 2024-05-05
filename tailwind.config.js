/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["webinar/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: false,
  },
  plugins: [require("daisyui")],
};
