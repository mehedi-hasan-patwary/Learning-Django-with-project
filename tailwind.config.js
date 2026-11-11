/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html",          //Template at the project lvl
    "./**/templates/**/*.html",   //         tem inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

