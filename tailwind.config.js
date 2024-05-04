/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["webinar/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
