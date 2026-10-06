const formulario = document.getElementById("formulario");
const lista = document.getElementById("lista");

formulario.addEventListener("submit", async (event) => {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;

    const respuesta = await fetch("http://127.0.0.1:8000/usuarios", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nombre: nombre,
            email: email
        })
    });

    const datos = await respuesta.json();

    alert(datos.mensaje);

    formulario.reset();
    cargarUsuarios();
});


async function cargarUsuarios() {
    const respuesta = await fetch("http://127.0.0.1:8000/usuarios");
    const usuarios = await respuesta.json();

    lista.innerHTML = "";

    usuarios.forEach(usuario => {
        const elemento = document.createElement("li");

        elemento.textContent =
            `${usuario.nombre} - ${usuario.email}`;

        lista.appendChild(elemento);
    });
}


cargarUsuarios();