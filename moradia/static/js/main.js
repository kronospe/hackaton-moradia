// Máscara de CPF
const cpfInput = document.getElementById("cpf");
if (cpfInput) {
  cpfInput.addEventListener("input", function () {
    let v = this.value.replace(/\D/g, "").slice(0, 11);
    v = v.replace(/(\d{3})(\d)/, "$1.$2");
    v = v.replace(/(\d{3})(\d)/, "$1.$2");
    v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
    this.value = v;
  });
}

// Máscara de telefone
const telInput = document.getElementById("telefone");
if (telInput) {
  telInput.addEventListener("input", function () {
    let v = this.value.replace(/\D/g, "").slice(0, 11);
    if (v.length <= 10) {
      v = v.replace(/(\d{2})(\d{4})(\d{0,4})/, "($1) $2-$3");
    } else {
      v = v.replace(/(\d{2})(\d{5})(\d{0,4})/, "($1) $2-$3");
    }
    this.value = v;
  });
}

// Scroll suave para âncoras
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener("click", function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute("href"));
    if (target) target.scrollIntoView({ behavior: "smooth" });
  });
});
