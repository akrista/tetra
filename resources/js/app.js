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

const root = document.documentElement

document.querySelectorAll('[data-theme-toggle]').forEach((btn) => {
  btn.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark'
    root.dataset.theme = next
    try { localStorage.setItem('tetra-theme', next) } catch (e) {}
  })
})

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches

const easeOutExpo = (t) => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t))

const formatES = (value, decimals) =>
  value.toLocaleString('es-VE', {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  })

const countUp = (el) => {
  const target = parseFloat(el.dataset.countTo)
  const decimals = parseInt(el.dataset.countDecimals || '0', 10)
  const prefix = el.dataset.countPrefix || ''
  if (reduceMotion || !Number.isFinite(target)) {
    el.textContent = prefix + formatES(target, decimals)
    return
  }
  const duration = 1400
  const start = performance.now()
  const tick = (now) => {
    const progress = Math.min((now - start) / duration, 1)
    el.textContent = prefix + formatES(target * easeOutExpo(progress), decimals)
    if (progress < 1) requestAnimationFrame(tick)
  }
  requestAnimationFrame(tick)
}

document.querySelectorAll('[data-count-to]').forEach(countUp)
