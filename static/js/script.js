let img_url = "/static/img/profile.jpg";
const fireinput = (ev) => {
    ev.preventDefault();
    const input = document.getElementById('id_profile')
    input.click();
}
const input = document.getElementById('id_profile')

input.addEventListener('change', function() {
    const file = this.files[0];
    const img = document.getElementById('select-img')
    const url = URL.createObjectURL(file);
    img_url = url;
    img.setAttribute('src',url);
    const text = document.getElementById('btn-text');
    text.innerText = 'Change Image'
})

document.addEventListener('DOMContentLoaded',()=>{
    document.getElementById('img-btn').addEventListener('click',fireinput);
})




