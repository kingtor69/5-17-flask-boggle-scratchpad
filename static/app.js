console.log('page refresh')

const form = document.querySelector('#because');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log(e)
})