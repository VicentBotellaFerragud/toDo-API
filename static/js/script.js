//Global variables:
let toDosContainer = document.getElementById('toDosContainer');
let titleInput = document.getElementById('titleInput');
let descriptionInput = document.getElementById('descriptionInput');

async function createToDo(token, user) {

    if (titleInput.value !== '' && descriptionInput.value !== '') {

        let fd = new FormData();
        /* let token = document.querySelector('[name=csrfmiddlewaretoken]').value; */ //This is another way to get the value of the token.

        fd.append('toDoTitle', titleInput.value);
        fd.append('toDoDescription', descriptionInput.value);
        fd.append('csrfmiddlewaretoken', token);

        try {

            toDosContainer.innerHTML += `

                <div class="toDo-container" id="beforeResponse">
                    <span class="title-span" style="color: blue"><b>${titleInput.value}:</b></span>
                    <span class="description-span"><i>${descriptionInput.value}</i></span>
                </div>

            `;

            //This is the post call.
            let response = await fetch('/board/', {
                method: 'POST',
                body: fd
            });

            //This is the response from the backend server.
            let responseAsJson = await response.json();

            let parsedJson = JSON.parse(responseAsJson);

            console.log(parsedJson.pk);

            let id = parsedJson.pk;

            let beforeResponse = document.getElementById('beforeResponse');

            beforeResponse.remove();

            toDosContainer.innerHTML += `
            
                <div class="toDo-container">
                    <span class="title-span"><b>${titleInput.value}:</b></span>
                    <span class="description-span"><i>${descriptionInput.value}</i></span>
                </div>
                
            `;

            titleInput.value = '';
            descriptionInput.value = '';

        } catch (e) {

            console.log(e);

        }

    } else {

        alert('Your toDo needs both a title and a description');

    }

}