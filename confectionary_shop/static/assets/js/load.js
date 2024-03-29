async function load_category(){

    const result = await fetch('http://127.0.0.1:8000/product/category_list/')
    const json_result = await result.json()

    const cat = document.createElement('div')
    cat.className = 'cat'
    cat.style.width ='200px'
    const img_div = document.createElement('div')
    img_div.className = 'd-flex row align-content-center justify-content-center'
    img_div.style.height = '120px'
    const img = document.createElement('img')
    img.className = 'rounded-circle'
    img.style.width = '120px'
    img.style.height = '100px'
    img.alt = 'avatar'
    img.src ='http://127.0.0.1:8000/media/draw1.png'
    img_div.append(img)
    const category_name = document.createElement('div')
    category_name.className = 'd-flex row align-content-center text-center justify-content-center'
    category_name.style.height = '40px'
    const p = document.createElement('p')
    p.innerHTML = 'همه'
    category_name.append(p)
    cat.append(img_div,category_name)
    cat.addEventListener("click", function () {
    load_products('all');})
    document.getElementById('category').append(cat)
    json_result.forEach(element=>{
    const cat = document.createElement('div')
    cat.className = 'cat'
    cat.style.width ='200px'
    const img_div = document.createElement('div')
    img_div.className = 'd-flex row align-content-center justify-content-center'
    img_div.style.height = '120px'
    const img = document.createElement('img')
    img.className = 'rounded-circle'
    img.style.width = '120px'
    img.style.height = '100px'
    img.alt = 'avatar'+element.id
    img.src = element.img
    img_div.append(img)
    const category_name = document.createElement('div')
    category_name.className = 'd-flex row align-content-center text-center justify-content-center'
    category_name.style.height = '40px'
    const p = document.createElement('p')
    p.innerHTML = element.category_name
    category_name.append(p)
    cat.append(img_div,category_name)
    cat.addEventListener("click", function () {
    load_products(element.id);
});
    document.getElementById('category').append(cat)
    })


}


