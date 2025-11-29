document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('cadastroForm');
    const emailInput = document.getElementById('email');
    const senhaInput = document.getElementById('senha');
    const confirmarSenhaInput = document.getElementById('confirmarSenha');
    const resumoDadosList = document.getElementById('resumoDados');
    const btnConfirmarCadastro = document.getElementById('btnConfirmarCadastro');
  
    const confirmacaoModal = new bootstrap.Modal(document.getElementById('confirmacaoModal'));
    const sucessoModal = new bootstrap.Modal(document.getElementById('sucessoModal'));

    let dadosCadastro = {};
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    emailInput.addEventListener('input', function() {
        if (!emailRegex.test(emailInput.value)) {
            emailInput.classList.add('is-invalid');
            document.getElementById('feedbackEmail').textContent = 'Por favor, insira um email válido (ex: nome@gmail.com).';
        } else {
            emailInput.classList.remove('is-invalid');
            emailInput.classList.add('is-valid');
        }
    });

    function validarSenhas() {
        const senhasConferem = senhaInput.value === confirmarSenhaInput.value;
        
        if (confirmarSenhaInput.value.length > 0) {
            if (senhasConferem) {
                confirmarSenhaInput.classList.remove('is-invalid');
                confirmarSenhaInput.classList.add('is-valid');
            } else {
                confirmarSenhaInput.classList.add('is-invalid');
                confirmarSenhaInput.classList.remove('is-valid');
                document.getElementById('feedbackConfirmarSenha').textContent = 'As senhas não conferem.';
            }
        }
        return senhasConferem;
    }

    confirmarSenhaInput.addEventListener('input', validarSenhas);
    senhaInput.addEventListener('input', validarSenhas);
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        event.stopPropagation();
        form.classList.add('was-validated');
        const formValido = form.checkValidity() && validarSenhas() && emailRegex.test(emailInput.value);

        if (formValido) {
            coletarDados();
            exibirResumoModal();
        }
    }, false);

    function coletarDados() {
        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;
        const telefone = document.getElementById('telefone').value || 'Não informado';
        const interessesSelecionados = Array.from(document.querySelectorAll('input[type="checkbox"]:checked'))
            .filter(cb => cb.id.startsWith('interesse'))
            .map(cb => cb.value);
        dadosCadastro = {
            nome: nome,
            email: email,
            telefone: telefone,
            interesses: interessesSelecionados.length > 0 ? interessesSelecionados.join(', ') : 'Nenhum selecionado'
        };
    }

    function exibirResumoModal() {
        resumoDadosList.innerHTML = '';
        resumoDadosList.innerHTML += `<li class="list-group-item"><strong>Nome:</strong> ${dadosCadastro.nome}</li>`;
        resumoDadosList.innerHTML += `<li class="list-group-item"><strong>Email:</strong> ${dadosCadastro.email}</li>`;
        resumoDadosList.innerHTML += `<li class="list-group-item"><strong>Telefone:</strong> ${dadosCadastro.telefone}</li>`;
        resumoDadosList.innerHTML += `<li class="list-group-item"><strong>Interesses:</strong> ${dadosCadastro.interesses}</li>`;
        confirmacaoModal.show();
    }

    btnConfirmarCadastro.addEventListener('click', function() {
        console.log('Dados a serem enviados:', dadosCadastro);
        confirmacaoModal.hide();
        sucessoModal.show();
        form.reset();
        form.classList.remove('was-validated');
        document.querySelectorAll('.is-valid').forEach(el => el.classList.remove('is-valid'));
    });
});