const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
let timeout = null;

function checkPasswordStrength() {
    const scale = document.getElementById('scale').value;
    const scalelabel = document.getElementById('scale-label');
    const special = document.getElementById('special');
    const simple = document.getElementById('simple');
    

    const password = document.getElementById('password').value;
    const passphrase = document.getElementById('passphrase').value;
    const passphrase_created = document.getElementById('passphrase_created');
    const passphrase_created_label = document.getElementById('passphrase_created_label');
    const range_password_label = document.getElementById('range_password_label');
    console.log('Typing passphrase:', passphrase);

    // Clear the previous timeout
    clearTimeout(timeout);

    // Set a new timeout
    timeout = setTimeout(() => {
        console.log('Sending passphrase:', passphrase);

        const progress_range = document.getElementById('progress_range');
        const progress_check = document.getElementById('progress_check');
        const striped_range = document.getElementById('striped_range');
        const striped_check = document.getElementById('striped_check');
        const strengthTextRange = document.getElementById('strength-text-range');
        const strengthTextCheck = document.getElementById('strength-text-check');

        fetch("/genpass_print/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrftoken
            },
            body: new URLSearchParams({
                'passphrase_created_label' : passphrase_created_label,
                'passphrase_created' : passphrase_created,
                'passphrase': passphrase,
                'password': password,
                'scale': scale,
                'special': special.checked,
                'simple': simple.checked
            }),
            mode: 'same-origin'
        })
        .then(response => response.json())
        .then(data => {
            console.log('Received data:', data);
            console.log(simple, passphrase);
            simple.checked = data['simple'];
            special.checked = data['special'];
            striped_check.style.width = data['percent'] + '%';
            progress_check.setAttribute('aria-valuenow', data['percent']);
            striped_check.classList.remove('bg-danger', 'bg-warning', 'bg-info', 'bg-success', 'bg-dark');
            striped_check.classList.add(data['colorClass']);
            strengthTextCheck.textContent = data['message'];
            striped_range.style.width = data['percent_range'] + '%';
            progress_range.setAttribute('aria-valuenow', data['percent_range']);
            striped_range.classList.remove('bg-danger', 'bg-warning', 'bg-info', 'bg-success', 'bg-dark');
            striped_range.classList.add(data['colorClassRange']);
            strengthTextRange.textContent = data['message_range'];
            scalelabel.textContent = 'Taille du mot de passe : ' + data['scale'];
            range_password_label.textContent = data['range_password'];
            passphrase_created_label.textContent = data['passphrase_created'];
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }, 400);
}
