setTimeout(() => {
    recuperar_codigo_url()
    create_event_submit()
}, 10);

function create_event_submit(){
    let form = document.getElementById('formulario_asignar_recurso')
    form.addEventListener('submit',()=>{
        desbloquear_select('id_recurso')
    })
}

function recuperar_codigo_url() {
    array = location.pathname.split('/').filter((e)=> e.trim() !== '')
    codigo_string = array[array.length - 1]

    try {
        codigo =  parseInt(codigo_string)
        if(Number.isInteger(codigo)){
            bloquear_select('id_recurso')
        }
    } catch (error) {
        
    }
}

function bloquear_select(id) {
    let select = document.getElementById(id)
    select.disabled = true
}

function desbloquear_select(id) {
    let select = document.getElementById(id)
    select.disabled = false
}