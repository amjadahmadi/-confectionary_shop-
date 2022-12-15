async function load_products(category_id){
    const result = await fetch('http://127.0.0.1:8000/product/product_list/'+category_id)
    const json_result = await result.json()
    console.log(`1 = ${json_result[0].product_name}`)
    json_result.forEach(element=>{
    const html = `          <div class="d-flex flex-row  mt-4 mb-4" style="min-width: 400px; max-width: 600px; height: 210px;">

            <div class="card ">

                <div class="d-flex flex-row h-100">
        <div class="d-flex flex-column col-7">

            <div class="d-flex flex-row-reverse m-2" style="height: 20%;"><p class="">${element['product']['product_name']}</p></div>
        <div class="d-flex flex-row-reverse m-2" style="height: 40%;">${element['product']['description']}
        </div>
        <div class="d-flex flex-row-reverse m-2" style="height: 20%;">${element['price']}
        </div>
        <div class="d-flex  flex-row-reverse justify-content-around " style="height: 20%;">
         <div class="d-flex flex-colum">
            <select id="menu" style="height: 25px;width: 100px;">
                <option>number</option>
                <option>wheight(kilos)</option>
            </select>

         </div>

         <div class="d-flex flex-column">
                <input type="number" step="0.5" id="inputPassword2" placeholder="count" size="7" style="height: 25px;width: 100px;">
            </div>
            <div class="d-flex flex-column">
                <i class="fa fa-plus" aria-hidden="true" style="font-size:24px;"></i>

             </div>
        </div>
        </div>
        <div class="d-flex flex-column col-5 ">
            <img class="card-img-top w-100 h-100" src="${element['product']['img']}" alt="Card image cap">

        </div>
                </div>
            </div>

        </div>`
       document.getElementById('products').innerHTML += html
    })
}