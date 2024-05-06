/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["webinar/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: false,
  },
  safelist: [{ pattern: /alert-+/ }],
  plugins: [require("daisyui")],
};
