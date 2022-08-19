product = document.querySelectorAll(".product");
result = document.querySelector(".result");
surname = document.querySelector('[name="surname"]')
firstname = document.querySelector('[name="firstname"]')

let total = 0;
let price = 0;
let content = [];

product.forEach(element => { element.addEventListener("change", function()
    {
        //console.log(element.children[1].name) //кол-во
        //console.log(element.children[0].children[0].name) //цена

        content = []

        total = 0;

        if(element.children[0].children[0].checked)
        {
            if(parseInt(element.children[1].value) <= 0)
            {
                element.children[1].value = 1;
            }
            else if(element.children[1].value == "")
            {
                element.children[1].value = 1;
            }
            else if(element.children[1].value >= 1)
            {
                element.children[1].value = element.children[1].value;
            }
            else
            {
                element.children[1].value = 1;
            }

        }
        else
        {
            element.children[1].value = 0;
        }

        for(let pr of product)
        {
            if(pr.children[0].children[0].checked)
            {
                price = parseInt(pr.children[0].children[0].value) * parseInt(pr.children[1].value);
                content.push(`${pr.children[0].children[1].textContent} ${pr.children[1].value} шт.`)
                total += price;
            }
        }

        result.textContent = total;
    });
});


function btnClick()
{
    if(total > 0)
    {
        if(surname.value == "")
        {
           surname.value = "Неизвестен";
        }

        if(firstname.value == "")
        {
           firstname.value = "Неизвестен";
        }

        let fullName = `${surname.value} ${firstname.value}`;
        if(confirm(`Заказчик: ${fullName}\nИтого: ${total} руб.`))
        {
            window.location.href = `/success/${fullName}/${content}/${total}`;
        }
    }
    else
    {
        alert("Вы ничего не выбрали!")
    }
}