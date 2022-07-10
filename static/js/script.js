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
                    <span class="title-span" style="color: red"><i><b>${titleInput.value}:</b></i></span>
                    <span class="description-span" style="color: red"><i>${descriptionInput.value}</i></span>
                </div>

            `;

            //This is the post call.
            let response = await fetch('/board/', { 
                /* If I fetch 'https://vicentbotellaferragud.pythonanywhere.com/toDos/', I get the error '"toDo.user" must be a 
                "User" instance' when sendind the POST request */
                method: 'POST',
                body: fd
            });

            //This is the response from the backend server.
            let responseAsJson = await response.json();

            let parsedJson = JSON.parse(responseAsJson);

            //This could be removed if I don't use it in the future.
            console.log(parsedJson.pk);
            let id = parsedJson.pk;

            let beforeResponse = document.getElementById('beforeResponse');

            beforeResponse.remove();

            toDosContainer.innerHTML += `
            
                <div class="toDo-container">
                    <span class="title-span"><b>${titleInput.value}:</b></span>
                    <span class="description-span">${descriptionInput.value}</span>
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