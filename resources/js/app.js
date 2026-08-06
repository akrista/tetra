import '../css/app.css'

document.querySelectorAll('.password-toggle').forEach((btn) => {
  btn.addEventListener('click', () => {
    const input = document.getElementById(btn.dataset.target)
    if (!input) return
    const show = input.type === 'password'
    input.type = show ? 'text' : 'password'
    btn.textContent = show ? 'Ocultar' : 'Mostrar'
    btn.setAttribute('aria-pressed', String(show))
    btn.setAttribute('aria-label', show ? 'Ocultar contraseña' : 'Mostrar contraseña')
  })
})
